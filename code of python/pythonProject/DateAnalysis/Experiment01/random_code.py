import random
import string
import threading

class CaptchaManager:
    def __init__(self):
        self.generated_captchas = set()
        self.lock = threading.Lock()

    def generate_captcha(self):
        captcha = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
        return captcha

    def get_unique_captcha(self):
        with self.lock:
            while True:
                captcha = self.generate_captcha()
                if captcha not in self.generated_captchas:
                    self.generated_captchas.add(captcha)
                    return captcha

def simulate_user_request(captcha_manager, user_id):
    captcha = captcha_manager.get_unique_captcha()
    print(f"用户 {user_id} 的验证码是: {captcha}")

if __name__ == "__main__":
    captcha_manager = CaptchaManager()
    threads = []

    # 模拟多个用户同时获取验证码
    for i in range(5):  # 假设有5个用户请求
        thread = threading.Thread(target=simulate_user_request, args=(captcha_manager, i))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()
