from datetime import datetime

def get_current_time():
    return  datetime.now().strftime("%Y-%m-%d %H-%M-%S")


USER = {
    "1001":{"id" : "1001","name" : "张三"},
    "1002":{"id":"1002","name":"李四"},
    "1003":{"id":"1003","name":"王二"},
    "1004":{"id":"1004","name":"淑瑶"},
    "1005":{"id":"1005","name":"南枝"},
    "1006":{"id":"1006","name":"淑柔"},
    "1007":{"id":"1007","name":"阿嬷"}
}

def query_user(user_id):
    return USER.get(user_id, "查无此人")