"""# 使用Matplotlib绘制光线和界面"""
"""
绘制界面与法线、绘制入射光线和折射光线、标注参数、样式美化
通过 visualization 模块，用户无需关注绘图的底层细节，只需提供数据即可生成直观的光路图。
这种解耦也意味着如果以后要改用其他绘图库，只需修改 visualization 实现而不影响核心计算或 CLI 部分。
"""
import matplotlib.pyplot as plt


def draw_refraction(data: dict, output_path: str):
    """
    根据 core 模块返回的数据字典绘制折射图。
    """
    incident_pts = data["incident_ray"]  # 入射线坐标列表 [(x1,y1), (x2,y2)]
    refracted_pts = data["refracted_ray"]  # 折射线坐标列表
    theta1 = data["incident_angle"]
    theta2 = data["refracted_angle"]
    n1 = data["n1"]
    n2 = data["n2"]  # 介质折射率

    fig, ax = plt.subplots()
    # 绘制界面
    ax.axhline(0, color='black', linestyle='--', linewidth=1)  # 界面水平线
    # 绘制法线
    ax.axvline(0, color='gray', linestyle=':', linewidth=1)  # 界面法线
    # 绘制入射光线
    x_inc, y_inc = zip(*incident_pts)
    ax.plot(x_inc, y_inc, color='blue', linewidth=2, label='入射光')
    # 绘制折射光线（如果有折射）
    if refracted_pts:
        x_ref, y_ref = zip(*refracted_pts)
        ax.plot(x_ref, y_ref, color='red', linewidth=2, label='折射光')
    else:
        # 处理全内反射的情况：可以只绘制入射光线和反射光（本例未实现反射光）
        pass

    # 标注介质信息
    ax.text(-1.5, 0.5, f"介质1 (n1={n1})", color='blue')
    ax.text(-1.5, -0.5, f"介质2 (n2={n2})", color='red')
    # 设置图形显示范围
    ax.set_xlim(-2, 2);
    ax.set_ylim(-2, 2)
    ax.set_aspect('equal')
    ax.set_title("光线折射示意图")
    ax.legend()
    plt.savefig(output_path)
    plt.close()
