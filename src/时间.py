from datetime import datetime
def format_time_diff(time1: datetime, time2: datetime) ->str:
    '''
    计算两个时间点的差值，完整显示天、小时、分钟、秒（包括0值）
    输出格式：d天h小时m分s秒
    '''
    # 计算时间差（取绝对值）
    time_diff = abs(time2 - time1)
    
    # 拆分总秒数为各单位
    total_seconds = int(time_diff.total_seconds())
    days = total_seconds // (24 * 3600)
    remaining_seconds = total_seconds % (24 * 3600)
    
    hours = remaining_seconds // 3600
    remaining_seconds %= 3600
    
    minutes = remaining_seconds // 60
    seconds = remaining_seconds % 60
    
    # 强制显示所有单位，无论是否为0
    return f"{days}天{hours}小时{minutes}分{seconds}秒"


# 示例使用
if __name__ == "__main__":
    # 测试1：普通时间差
    t1 = datetime(2024, 5, 1, 10, 30, 0)
    t2 = datetime(2024, 5, 3, 15, 45, 30)
    print(format_time_diff(t1, t2))  # 输出：2天5小时15分30秒
    
    # 测试2：部分单位为0
    t3 = datetime(2024, 5, 1, 10, 0, 0)
    t4 = datetime(2024, 5, 1, 10, 30, 0)
    print(format_time_diff(t3, t4))  # 输出：0天0小时30分0秒
    
    # 测试3：所有单位为0
    t5 = datetime(2024, 5, 1, 10, 0, 0)
    t6 = datetime(2024, 5, 1, 10, 0, 0)
    print(format_time_diff(t5, t6))  # 输出：0天0小时0分0秒