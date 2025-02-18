const API_URL = "http://127.0.0.1:5001/notes";

async function fetchNotes() {
    const response = await fetch(API_URL);
    const notes = await response.json();
    document.getElementById("notes-list").innerHTML = notes.map(note => `
        <div>
            <h3>${note.title}</h3>
            <p>${note.content}</p>
            <p><strong>Ngày tạo:</strong> ${note.created_at}</p>
            <button onclick="deleteNote('${note.title}')">Xóa</button>
        </div>
    `).join("");
}

async function addNote() {
    const title = document.getElementById("title").value;
    const content = document.getElementById("content").value;

    await fetch(API_URL, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ title, content })
    });

    fetchNotes();
}

async function deleteNote(title) {
    await fetch(`${API_URL}/${title}`, { method: "DELETE" });
    fetchNotes();
}

async function searchNotes() {
    const keyword = document.getElementById("search").value.toLowerCase();
    const response = await fetch(API_URL);
    const notes = await response.json();
    const filteredNotes = notes.filter(note => note.title.toLowerCase().includes(keyword));
    
    document.getElementById("notes-list").innerHTML = filteredNotes.map(note => `
        <div>
            <h3>${note.title}</h3>
            <p>${note.content}</p>
            <button onclick="deleteNote('${note.title}')">Xóa</button>
        </div>
    `).join("");
}

fetchNotes();
