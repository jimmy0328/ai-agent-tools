from tinydb import TinyDB
from datetime import datetime

db = TinyDB(f"history/chat-{datetime.now().isoformat()}.json")


def add_message(content=None, role="user"):
    if content is not None:
        return db.insert(
            {
                "role": role,
                "content": content,
                "created_at": datetime.now().isoformat(),
            }
        )


def get_messages():
    return [
        {
            "role": item["role"],
            "content": item["content"],
        }
        for item in db
    ]


def init_message(content=None):
    db.truncate()

    if content is not None:
        add_message(role="developer", content=content)
