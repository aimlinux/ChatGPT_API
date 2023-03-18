import os

import openai


# APIキーの設定
openai.api_key = os.environ["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"]


response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": "大谷翔平について教えて"},
    ],
)
print(response.choices[0]["message"]["content"].strip())