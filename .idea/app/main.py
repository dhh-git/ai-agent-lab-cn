from agent import  agent
from agent_tool import  query_user, get_current_time


while True:
    user_input = input("用户：")
    if user_input == "exit":
        break

    result = agent("查询用户" + user_input);
    print("查询时间", get_current_time() , ";查询结果：", result)

