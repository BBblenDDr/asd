from openai import OpenAI
import asyncio

version = 'deepseek/deepseek-v3-0324'
ap_key = 'sk_o79if-QTqR06T2_qxpxj8Ms90hKDFPnyCDqY7QGtXsY'
base_url = "https://api.novita.ai/v3/openai"


from openai import OpenAI

client = OpenAI(
    base_url="https://api.novita.ai/v3/openai",
    # Get the Novita AI API Key from: https://novita.ai/settings/key-management.
    api_key=ap_key,
)


async def get_answer(question):
    model = 'deepseek/deepseek-v3-0324'
    stream = True  # or False
    max_tokens = 512
    chat_completion_res = client.chat.completions.create(
        model=version,
        messages=[
            {
                "role": "system",
                "content": "Отвечай только доступными вариантами ответа, без объяснений, кратко и по существу."
                },
                {
                    "role": "user",
                    "content": question,
                }
            ],
            stream=stream,
            max_tokens=max_tokens,
        )

    if stream:
        full_reply = ""
        for chunk in chat_completion_res:
            content = getattr(chunk.choices[0].delta, "content", "")
            if content:
                full_reply += content
        return full_reply.strip()
    else:
        return chat_completion_res.choices[0].message.content