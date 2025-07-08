"""
业务核心逻辑---光线折射逻辑 (计算折射角、轨迹)
核心模块不执行任何输入输出，只专注于物理和几何计算，这使得它易于单元测试
"""
"""
折射角计算：
    利用斯涅尔定律公式 n₁·sinθ₁ = n₂·sinθ₂ 计算折射角 θ₂注意角度需转换为弧度以使用 math 或 numpy 三角函数计算。
    若发生全内反射（无法求实数 θ₂），则需要在结果中标记这种情况（例如返回 None 或特殊标记）。
光线路径：
    确定光线在界面上的交点和传播方向。可以假定介质界面为水平直线（如 y=0），入射光来自上方介质。
    core 模块可根据入射角计算入射光线和折射光线的直线方程或一组坐标点，以便后续绘图模块使用。
    典型地，可设定入射光线在界面上的入射点坐标（例如原点 (0,0)），根据入射角反推光源点或延展入射线路径坐标。
    同样，根据折射角计算折射线在界面下方的延展。
数据输出：
    core 模块应将计算结果和必要的光线参数封装成数据结构返回，例如使用一个 Python 字典或自定义对象，
    其中包含：入射角度（可能区分输入的度/弧度）、折射角度、是否全内反射标志、入射光线坐标点列表、折射光线坐标点列表、
    以及界面法线方向等信息。这样有助于 visualization 模块绘制，并方便测试模块断言结果正确。
"""

import math

def snell_refract(n1: float, n2: float, theta1: float) -> float:
    """根据斯涅尔定律计算折射角（弧度）。theta1 为入射角（弧度）。"""
    sin_theta2 = n1 * math.sin(theta1) / n2
    if abs(sin_theta2) > 1:
        # 全内反射，无折射角
        return None
    theta2 = math.asin(sin_theta2)
    return theta2

def compute_ray_path(n1, n2, theta1_deg):
    """计算光线在界面上的路径，返回包含入射线和折射线坐标的结构。"""
    # 将入射角从度数转为弧度
    theta1 = math.radians(theta1_deg)
    theta2 = snell_refract(n1, n2, theta1)
    result = {
        "incident_angle": theta1_deg,
        "refracted_angle": None,
        "incident_ray": [],   # 入射线坐标点列表
        "refracted_ray": []   # 折射线坐标点列表
    }
    # 计算折射角（以度为单位便于理解）
    if theta2 is not None:
        result["refracted_angle"] = math.degrees(theta2)
    # 假定入射点在 (0,0)，法线垂直向上
    # 计算入射线（从界面往回延伸一定长度）
    # ...（此处根据几何关系计算坐标）
    # 计算折射线（从界面往下延伸）
    # ...（此处根据几何关系计算坐标）
    return result

