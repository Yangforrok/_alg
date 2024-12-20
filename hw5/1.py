import threading

def run_with_timeout(func, timeout, *args, **kwargs):
    result = [None]  
    error = [None]   

    def wrapper():
        try:
            result[0] = func(*args, **kwargs)
        except Exception as e:
            error[0] = str(e)

    thread = threading.Thread(target=wrapper)
    thread.daemon = True
    thread.start()
    thread.join(timeout) 

    if thread.is_alive():
        return False, "Timeout: Function did not stop within the time limit."
    if error[0]:
        return False, f"Error: {error[0]}"
    return True, result[0]

# 測試目標函數
def test_function(n):
    while n % 2 != 0:  # 如果 n 是奇數，無窮迴圈
        pass
    return "Stopped successfully!"


if __name__ == "__main__":
    n = 1  
    timeout_seconds = 5  
    will_stop, message = run_with_timeout(test_function, timeout_seconds, n)
    print(f"是否停止: {will_stop}, 訊息: {message}")
