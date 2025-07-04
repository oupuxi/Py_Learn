"""
让文件夹变成 Python “包”
在 Python 中，只有包含 __init__.py 的文件夹才被视为“包”，可以 import mypackage.xxx。
"""
from .core import compute
from .utils import helper_func

__all__ = ["compute", "helper_func"]# __all__ 指定可以被 import 的模块，就可以直接from mypackage import compute