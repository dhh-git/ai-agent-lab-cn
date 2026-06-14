from agent_tool import  query_user


def agent(user_input):
    if "查询用户" in user_input:
        user_id = user_input.replace("查询用户", "").strip()
        return query_user(user_id)

    return "无法处理"
