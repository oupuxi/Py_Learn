"""即main()，项目的运行入口"""
# scripts/run_demo.py
from mypackage.core import compute
from mypackage.logger import setup_logger

logger = setup_logger(__name__)

def main():
    logger.info("开始运行 demo")
    result = compute(3, 4)
    print("结果是：", result)

if __name__ == "__main__":
    main()
