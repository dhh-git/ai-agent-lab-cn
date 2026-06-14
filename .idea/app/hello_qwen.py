import os

from banks.extensions.docs import completion
from networkx.algorithms.operators.unary import complement
from openai import OpenAI

try:
    client = OpenAI(
        # 阿里云百炼：api-key:
        api_key = os.getenv("qwen-api-key"),
        base_url = os.getenv("qwen-base-url"),
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