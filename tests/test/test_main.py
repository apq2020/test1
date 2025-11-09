from app1.utils import read_file, format_time


def main():
    """
    This is the main function.
    """
    print("read file:", read_file())

    # 1. 使用当前时间
    print(format_time())  # 输出类似: 2023-11-15 14:30:45


if __name__ == "__main__":
    main()
