from app1.utils import read_file, write_file, format_time
def main():
    """
    This is the main function.
    """
    print("Hello from main")
    print(format_time())

""" 工具函数 -> 给所有层用
数据结构 (models) -> 所有服务层依赖它
服务层 (services) -> 只能依赖 utils 和 models
应用入口 (main) -> 依赖 services 
"""
if __name__ == "__main__":
    main()
