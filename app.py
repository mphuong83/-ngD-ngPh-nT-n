from notes import Note

def main():
    while True:
        print("\n--- Quản lý ghi chú ---")
        print("1. Thêm ghi chú")
        print("2. Xem danh sách ghi chú")
        print("3. Xem chi tiết ghi chú")
        print("4. Xóa ghi chú")
        print("5. Thoát")
        choice = input("Chọn thao tác: ")

        if choice == "1":
            title = input("Nhập tiêu đề ghi chú: ")
            content = input("Nhập nội dung ghi chú: ")
            note = Note(title, content)
            if note.save():
                print("Ghi chú đã được lưu thành công!")
            else:
                print("Lỗi khi lưu ghi chú!")

        elif choice == "2":
            notes = Note.list_all()
            if notes:
                print("\nDanh sách ghi chú:")
                for note in notes:
                    print(f"- {note['title']} (Ngày: {note['created_at']})")
            else:
                print("Chưa có ghi chú nào.")

        elif choice == "3":
            title = input("Nhập tiêu đề ghi chú cần xem: ")
            note = Note.get(title)
            if note:
                print("\n--- Chi tiết ghi chú ---")
                print(f"Tiêu đề: {note['title']}")
                print(f"Nội dung: {note['content']}")
                print(f"Ngày tạo: {note['created_at']}")
            else:
                print("Không tìm thấy ghi chú.")

        elif choice == "4":
            title = input("Nhập tiêu đề ghi chú cần xóa: ")
            if Note.delete(title):
                print("Ghi chú đã được xóa.")
            else:
                print("Không tìm thấy ghi chú.")

        elif choice == "5":
            print("Thoát chương trình.")
            break
        else:
            print("Lựa chọn không hợp lệ, vui lòng thử lại!")

if __name__ == "__main__":
    main()
