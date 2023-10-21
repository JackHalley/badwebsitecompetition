from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

# Configure SQLite database
DATABASE = "submissions.db"

def create_table():
    conn = sqlite3.connect(DATABASE)
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS submissions (id INTEGER PRIMARY KEY, name TEXT, email TEXT, website TEXT, description TEXT, submission_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP);")
    conn.commit()
    conn.close()

create_table()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/submit", methods=["POST"])
def submit():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        website = request.form["website"]
        description = request.form["description"]

        conn = sqlite3.connect(DATABASE)
        cur = conn.cursor()
        cur.execute("INSERT INTO submissions (name, email, website, description) VALUES (?, ?, ?, ?)", (name, email, website, description))
        conn.commit()
        conn.close()

        return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)
