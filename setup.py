"""打包和安装配置。和pyproject.toml两者择一使用,Pyproject.toml 是当前推荐的方式，可以更清晰地声明配置且避免执行代码。
在教学项目中，可提供 setup.py 方便理解，同时附带 pyproject.toml 引导学生了解新风向。"""
# 传统的 setup.py：包含 setuptools 的配置，如包名、版本、作者、依赖等
from setuptools import setup, find_packages
setup(
    name="light-refraction-sim",
    version="0.1.0",
    author="Your Name",
    python_requires=">=3.10",
    install_requires=[
        "numpy>=1.20",
        "matplotlib>=3.5",
        "PyYAML>=6.0"
    ],
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    entry_points={
        "console_scripts": [
            "light-refraction-sim=cli.main:main"
        ]
    },
)
