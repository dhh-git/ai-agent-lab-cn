import os

from banks.extensions.docs import completion
from networkx.algorithms.operators.unary import complement
from openai import OpenAI

try:
    client = OpenAI(
        # 阿里云百炼：api-key:
        # sk-ws-H.REHDXYX.9VoL.MEUCIDx4dvFWKCb9AkYpSaCXDsvyEOsK0UNbY0WmUlGyYdIWAiEAmDlcSMqLa7oMG0dn0-7hqBOhQLfoemxdAjOss1TJhqE
        api_key = "sk-ws-H.REHDXYX.9VoL.MEUCIDx4dvFWKCb9AkYpSaCXDsvyEOsK0UNbY0WmUlGyYdIWAiEAmDlcSMqLa7oMG0dn0-7hqBOhQLfoemxdAjOss1TJhqE",
        base_url = "https://dashscope.aliyuncs.com/compatible-mode/v1",
    )

    completion = client.chat.completions.create(
        model= "qwen-plus",
        messages= [
            {'role' : 'system', 'content' : 'You are a helpful assistant.'},
            {'role' : 'user', 'content' : '你是谁？'}
        ]
    )
    print(completion.choices[0].message.content)
except Exception as e:
    print(f"错误信息：{e}")
    print("请参考文档：https://help.aliyun.com/model-studio/developer-reference/error-code")