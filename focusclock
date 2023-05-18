import time

def focus_timer(minutes):
    seconds = minutes * 60
    end_time = time.time() + seconds
    
    print(f"专注时钟已启动，持续时间为 {minutes} 分钟.")
    
    while time.time() < end_time:
        remaining_time = int(end_time - time.time())
        print(f"剩余时间: {remaining_time // 60:02d}:{remaining_time % 60:02d}", end="\r", flush=True)
        time.sleep(1)
    
    print("\n专注时间结束！")

# 设置专注时长为 25 分钟
focus_timer(25)
