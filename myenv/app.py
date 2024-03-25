from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

NOTES_FILE = "notes.txt"

def read_notes():
    try:
        with open(NOTES_FILE, "r") as file:
            return file.readlines()
    except FileNotFoundError:
        return []

def write_notes(notes):
    with open(NOTES_FILE, "w") as file:
        file.writelines(notes)

@app.route('/')
def index():
    notes = read_notes()
    return render_template('index.html', notes=notes)

@app.route('/add_note', methods=['POST'])
def add_note():
    note = request.form.get('note')
    if note:
        with open(NOTES_FILE, "a") as file:
            file.write(note + "\n")
    return redirect(url_for('index'))

@app.route('/edit_note/<int:index>', methods=['POST'])
def edit_note(index):
    new_note = request.form.get('new_note')
    notes = read_notes()
    if 0 <= index < len(notes):
        notes[index] = new_note + "\n"
        write_notes(notes)
    return redirect(url_for('index'))

@app.route('/delete_note/<int:index>')
def delete_note(index):
    notes = read_notes()
    if 0 <= index < len(notes):
        del notes[index]
        write_notes(notes)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
