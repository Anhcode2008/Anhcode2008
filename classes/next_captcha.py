from functions.thanhngang import thanh
class NextCaptcha:

    def __init__(self, apikey):
        self.apikey = apikey
        self.create_task_url = 'https://api.3xcaptcha.com/createTask'
        self.get_result_url = 'https://api.3xcaptcha.com/getTaskResult'

    def recaptchav2(self, sitekey, siteurl):
        data = {'clientKey': self.apikey, 'task': {
            'type': 'RecaptchaV2TaskProxyless', 'websiteURL': siteurl, 'websiteKey': sitekey}}
        try:
            response = requests.post(
                self.create_task_url, json=data, timeout=10).json()
            if response.get('errorId', 0) != 0:
                print(f'Lỗi tạo task: {response}')
                return (False, None)
            return (True, response.get('taskId'))
        except requests.RequestException as e:
            print(f'Lỗi khi gửi yêu cầu tạo task: {e}')
            return (False, None)

    def get_result(self, task_id, max_retries=10, delay=0):
        data = {'clientKey': self.apikey, 'taskId': task_id}
        for x in range(max_retries):
            try:
                response = requests.post(
                    self.get_result_url, json=data, timeout=10).json()
                if response.get('errorId', 0) != 0:
                    print(f'Lỗi lấy kết quả: {response}')
                    return (False, None)
                if response.get('status') == 'ready':
                    return (True, response['solution']['gRecaptchaResponse'])
                sleep(delay)
            except requests.RequestException as e:
                print(f'Lỗi khi lấy kết quả Captcha: {e}')
                return (False, None)
        print('Hết số lần thử, không có kết quả.')
        return (False, None)
