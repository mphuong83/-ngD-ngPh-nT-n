import time
import json
from db_manager import Database

db = Database()

class Note:
    def __init__(self, title, content):
        self.title = title
        self.content = content
        self.created_at = time.strftime("%Y-%m-%d %H:%M:%S")

    def save(self):
        """Lưu ghi chú vào database"""
        note_data = {
            "title": self.title,
            "content": self.content,
            "created_at": self.created_at
        }
        return db.set(self.title, json.dumps(note_data))

    @staticmethod
    def get(title):
        """Lấy ghi chú từ database"""
        note_json = db.get(title)
        if note_json:
            return json.loads(note_json)
        return None

    @staticmethod
    def delete(title):
        """Xóa ghi chú"""
        return db.delete(title)

    @staticmethod
    def list_all():
        """Lấy danh sách tất cả các ghi chú"""
        keys = db.get_all_keys()
        notes = []
        for key in keys:
            notes.append(json.loads(db.get(key)))
        return notes
