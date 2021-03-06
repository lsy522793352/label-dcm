import json
from module.config import config
import math
import numpy
import os
from PIL import Image
from pydicom import dcmread
from PyQt5.QtCore import QPointF, QRectF

def is_file_exists(path: str):
    return os.path.exists(path)

def is_file_readable(path: str):
    return os.access(path, os.R_OK)

def is_file_writable(path: str):
    return os.access(path, os.W_OK)

def to_date(date: str):
    return date[0:4] + '年' + date[4:6] + '月' + date[6:8] + '日'

def to_age(age: str):
    res: str = ''
    if age[0] != '0':
        res = age[0:3]
    elif age[1] != '0':
        res = age[1:3]
    elif age[2] != '0':
        res = age[2]
    if age[3] == 'Y':
        return res + '岁'
    elif age[3] == 'M':
        return res + '月'
    elif age[3] == 'W':
        return res + '周'
    elif age[3] == 'D':
        return res + '天'
    return res

def get_dcm_img_and_md_info(imgPath: str):
    dcm = dcmread(imgPath)
    low = numpy.min(dcm.pixel_array)
    upp = numpy.max(dcm.pixel_array)
    # 16 Bit -> 8 Bit
    mat = numpy.floor_divide(dcm.pixel_array, (upp - low + 1) / 256)
    img = Image.fromarray(mat.astype(numpy.uint8)).toqpixmap()
    info = {
        '患者ID': dcm.PatientID, '姓名': dcm.PatientName, '出生日期': to_date(dcm.PatientBirthDate),
        '性别': dcm.PatientSex, '体重': dcm.PatientWeight, '检查开始日期': to_date(dcm.StudyDate),
        '检查日期': to_date(dcm.SeriesDate), '检查时患者年龄': to_age(dcm.PatientAge), '检查部位': dcm.BodyPartExamined
    }
    return img, '---\n\n'.join([f'{key}: {val}\n\n' for key, val in info.items()])

# Windows 10
# SystemDrive:\HomePath\Pictures\
def get_home_img_dir():
    homeImgDir = os.getcwd()
    if sysDriver := os.getenv('SystemDrive'):
        homeImgDir = sysDriver
        if homePath := os.getenv('HomePath'):
            homeImgDir = os.path.join(homeImgDir, homePath, 'Pictures')
    return homeImgDir

def load_from_json(path):
    with open(path, 'r') as file:
        return json.load(file)

def save_json_file(data: dict, path: str):
    with open(path, 'w') as file:
        json.dump(data, file, indent=config.indent)

def get_index_shift(A: QPointF):
    return QPointF(A.x() + config.indexShifting, A.y() - config.indexShifting)

def get_midpoint(A: QPointF, B: QPointF):
    return QPointF((A.x() + B.x()) / 2, (A.y() + B.y()) / 2)

def get_distance(A: QPointF, B: QPointF):
    distance = ((A.x() - B.x()) * (A.x() - B.x()) + (A.y() - B.y()) * (A.y() - B.y())) ** 0.5
    return distance if distance > config.eps else config.eps

def get_distance_shift(A: QPointF, B: QPointF, C: QPointF):
    if math.fabs(A.x() - B.x()) < config.eps:
        return QPointF(C.x() + config.distanceShifting, C.y())
    if math.fabs(A.y() - B.y()) < config.eps:
        return QPointF(C.x(), C.y() - config.distanceShifting)
    if (A.x() - B.x()) * (A.y() - B.y()) < 0:
        return QPointF(C.x() + config.distanceShifting, C.y() + config.distanceShifting)
    return QPointF(C.x() + config.distanceShifting, C.y() - config.distanceShifting)

def get_radius(A: QPointF, B: QPointF, C: QPointF):
    return min(get_distance(B, A), get_distance(B, C)) * config.ratioToRadius

def get_diag_points(A: QPointF, B: QPointF, C: QPointF):
    r = get_radius(A, B, C)
    return QPointF(B.x() - r, B.y() - r), QPointF(B.x() + r, B.y() + r)

def get_dis_point(A: QPointF, B: QPointF, dis: float):
    ratio = dis / get_distance(A, B)
    return QPointF(A.x() + (B.x() - A.x()) * ratio, A.y() + (B.y() - A.y()) * ratio)

def get_arc_midpoint(A: QPointF, B: QPointF, C: QPointF):
    return get_dis_point(
        B, get_midpoint(get_dis_point(B, A, config.base), get_dis_point(B, C, config.base)), get_radius(A, B, C)
    )

# BA · BC
def get_dot(A: QPointF, B: QPointF, C: QPointF):
    BA = (A.x() - B.x(), A.y() - B.y())
    BC = (C.x() - B.x(), C.y() - B.y())
    return BA[0] * BC[0] + BA[1] * BC[1]

# BA × BC
def get_cross(A: QPointF, B: QPointF, C: QPointF):
    BA = (A.x() - B.x(), A.y() - B.y())
    BC = (C.x() - B.x(), C.y() - B.y())
    return BA[0] * BC[1] - BC[0] * BA[1]

def get_degree(A: QPointF, B: QPointF, C: QPointF):
    return math.degrees(math.acos(min(1, max(-1, get_dot(A, B, C) / get_distance(B, A) / get_distance(B, C)))))

def get_begin_degree(A: QPointF, B: QPointF, C: QPointF):
    D = C if get_cross(A, B, C) > 0 else A
    deg = get_degree(D, B, QPointF(B.x() + config.base, B.y()))
    return 360 - deg if D.y() > B.y() else deg

def get_degree_shift(A: QPointF, B: QPointF):
    # Up
    if A.y() > B.y() + config.eps and math.fabs(A.x() - B.x()) < config.eps:
        return QPointF(B.x(), B.y() - config.degreeShiftingBase)
    # Down
    if A.y() + config.eps < B.y() and math.fabs(A.x() - B.x()) < config.eps:
        return QPointF(B.x(), B.y() + config.degreeShiftingBase)
    # Left
    if A.x() > B.x() + config.eps and math.fabs(A.y() - B.y()) < config.eps:
        return QPointF(B.x() - config.degreeShiftingMore, B.y())
    # Right
    if A.x() + config.eps < B.x() and math.fabs(A.y() - B.y()) < config.eps:
        return QPointF(B.x() + config.degreeShiftingBase, B.y())
    # Top Right
    if A.x() + config.eps < B.x() and A.y() > B.y() + config.eps:
        return QPointF(B.x() + config.degreeShiftingBase, B.y() - config.degreeShiftingBase)
    # Top Left
    if A.x() > B.x() + config.eps and A.y() > B.y() + config.eps:
        return QPointF(B.x() - config.degreeShiftingMore, B.y() - config.degreeShiftingBase)
    # Bottom Left
    if A.x() > B.x() + config.eps and A.y() + config.eps < B.y():
        return QPointF(B.x() - config.degreeShiftingMore, B.y() + config.degreeShiftingBase)
    # Bottom Right
    return QPointF(B.x() + config.degreeShiftingBase, B.y() + config.degreeShiftingBase)

def get_min_bounding_rect(A: QPointF, B: QPointF):
    r = get_distance(A, B)
    return QRectF(QPointF(A.x() - r, A.y() - r), QPointF(A.x() + r, A.y() + r))

def get_line_key(indexA: int, indexB: int):
    return (indexA, indexB) if indexA < indexB else (indexB, indexA)

def get_angle_key(indexA: int, indexB: int, indexC: int):
    return (indexA, indexB, indexC) if indexA < indexC else (indexC, indexB, indexA)

def is_on_a_line(A: QPointF, B: QPointF, C: QPointF):
    return math.fabs((A.x() - C.x()) * (A.y() - B.y()) - (A.x() - B.x()) * (A.y() - C.y())) < config.eps

# AB: ax + by + c = 0
def get_foot_point(A: QPointF, B: QPointF, C: QPointF):
    a = A.y() - B.y()
    b = B.x() - A.x()
    c = -a * A.x() - b * A.y()
    return QPointF(
        (b * b * C.x() - a * b * C.y() - a * c) / (a * a + b * b),
        (a * a * C.y() - a * b * C.x() - b * c) / (a * a + b * b)
    )

def is_on_segment(A: QPointF, B: QPointF, C: QPointF):
    return min(A.x(), B.x()) < C.x() + config.eps and C.x() < max(A.x(), B.x()) + config.eps
