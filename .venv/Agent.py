import asyncio
# from agents import Agent, Runner
from openai import AsyncOpenAI

import os


client = AsyncOpenAI(
    api_key="sk-ws-H.REHDXYX.H8xe.MEQCIDmCSeiu6w_sY4dym1W-79OmzcaTCk2DaZXkHfHeCFuXAiB6LcJDSFGendZjq6pq-JzfHj1RJLq8NPWNlIDBjUK2QQ",
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1"
)
async def main():
    resp = await client.chat.completions.create(
        model= "qwen3.7-plus",
        messages=[{'role': 'user', 'content': '你是谁？'}]
    )
    print(resp.choices[0].message.content)

if __name__ == "__main__":
    asyncio.run(main())