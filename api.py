from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
from notes import Note
from config import SERVERS

app = Flask(__name__)
CORS(app)

# Đồng bộ dữ liệu với các server khác
def sync_data(endpoint, method="POST", data=None):
    for server in SERVERS:
        try:
            url = f"{server}{endpoint}"
            if method == "POST":
                requests.post(url, json=data)
            elif method == "DELETE":
                requests.delete(url)
        except Exception as e:
            print(f"Lỗi đồng bộ với {server}: {e}")

# API lấy danh sách ghi chú
@app.route('/notes', methods=['GET'])
def get_notes():
    notes = Note.list_all()
    return jsonify(notes), 200

# API thêm ghi chú và đồng bộ với server khác
@app.route('/notes', methods=['POST'])
def add_note():
    data = request.json
    if "title" not in data or "content" not in data:
        return jsonify({"error": "Thiếu tiêu đề hoặc nội dung"}), 400

    note = Note(data["title"], data["content"])
    if note.save():
        sync_data("/notes", "POST", data)  # Gửi dữ liệu đến server khác
        return jsonify({"message": "Ghi chú đã được lưu"}), 201
    return jsonify({"error": "Không thể lưu ghi chú"}), 500

# API lấy chi tiết ghi chú
@app.route('/notes/<title>', methods=['GET'])
def get_note(title):
    note = Note.get(title)
    if note:
        return jsonify(note), 200
    return jsonify({"error": "Không tìm thấy ghi chú"}), 404

# API xóa ghi chú và đồng bộ với server khác
@app.route('/notes/<title>', methods=['DELETE'])
def delete_note(title):
    if Note.delete(title):
        sync_data(f"/notes/{title}", "DELETE")  # Gửi yêu cầu xóa đến server khác
        return jsonify({"message": "Ghi chú đã được xóa"}), 200
    return jsonify({"error": "Không tìm thấy ghi chú"}), 404

# API xuất dữ liệu ra file
@app.route('/export', methods=['GET'])
def export_notes():
    notes = Note.list_all()
    with open("exported_notes.json", "w", encoding="utf-8") as f:
        json.dump(notes, f, ensure_ascii=False, indent=4)
    return jsonify({"message": "Dữ liệu đã được xuất ra file!"}), 200



if __name__ == "__main__":
    app.run(port=5002, debug=True)  # Chạy server trên cổng 5001
