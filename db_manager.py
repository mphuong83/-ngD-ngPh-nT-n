import pickledb

class Database:
    def __init__(self, db_file="notes.db", auto_dump=True):
        """Khởi tạo database PickleDB"""
        self.db = pickledb.load(db_file, auto_dump)

    def set(self, key, value):
        """Lưu dữ liệu vào database"""
        return self.db.set(key, value)

    def get(self, key):
        """Lấy dữ liệu từ database"""
        return self.db.get(key)

    def delete(self, key):
        """Xóa dữ liệu khỏi database"""
        return self.db.rem(key)

    def get_all_keys(self):
        """Lấy tất cả các key trong database"""
        return self.db.getall()

    def exists(self, key):
        """Kiểm tra xem key có tồn tại không"""
        return self.db.exists(key)
