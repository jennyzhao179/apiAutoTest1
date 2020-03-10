# 封装获取测试结果并且返回断言结果的方法
import json


def assert_t_f(response, code ,message):
    """

    :param response:发送请求后的响应体
    :param code:返回的状态码
    :param message:返回msg
    :return:
    """
    status_code = response.status_code
    msg = response.json().get("message")
    if status_code == code and msg ==message:
        return True
    else:
        return False

def build_data(filepath):
    case_data = []
    with open(filepath,encoding="utf-8")as f:
        data=json.load(f)
        for e_data in data.values():
           case_data.append(list(e_data.values()))
           print(case_data)
    return case_data
