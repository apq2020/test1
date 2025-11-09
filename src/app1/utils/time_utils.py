from datetime import datetime


def format_time(time_input=None):
    """
    将时间格式化为 'YYYY-MM-DD HH:MM:SS' 格式

    参数:
        time_input: 可选的时间输入，可以是：
            - None (默认值，使用当前时间)
            - datetime 对象
            - 时间戳（整数/浮点数）
            - 时间字符串（ISO格式或常见格式）

    返回:
        str: 格式化后的时间字符串，格式为 'YYYY-MM-DD HH:MM:SS'
    """
    if time_input is None:
        # 使用当前时间
        dt = datetime.now()
    elif isinstance(time_input, datetime):
        # 直接使用 datetime 对象
        dt = time_input
    elif isinstance(time_input, (int, float)):
        # 将时间戳转换为 datetime 对象（本地时间）
        dt = datetime.fromtimestamp(time_input)
    else:
        # 尝试解析时间字符串
        try:
            # 尝试解析 ISO 格式（如 "2023-01-01 12:00:00"）
            dt = datetime.fromisoformat(time_input)
        except ValueError:
            try:
                # 尝试解析常见格式（如 "01/01/2023 12:00:00"）
                dt = datetime.strptime(time_input, "%m/%d/%Y %H:%M:%S")
            except ValueError:
                raise ValueError(
                    "无法解析的时间格式，请使用 datetime 对象、时间戳或时间字符串"
                )

    # 格式化为指定格式
    return dt.strftime("%Y-%m-%d %H:%M:%S")
