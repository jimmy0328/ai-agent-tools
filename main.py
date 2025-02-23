from config.openai import client
from db.message import add_message, get_messages, init_message

init_message("你好，我是吉米助理，請問有什麼我可以幫忙的嗎？")

try:
    while True:
        user_question = input("請輸入你的問題(輸入 exit or quit 可結束對話)：")

        if user_question.lower() in ["exit", "quit"]:
            print("感謝你的使用，再見！")
            break

        add_message(user_question.strip())

        completion = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=get_messages(),
        )

        content = completion.choices[0].message.content
        add_message(content, role="assistant")
        print(content)
except Exception as e:
    add_message("system", str(e))
    print("發生錯誤，請稍後再試。")
    print(e)
