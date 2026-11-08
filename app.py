from flask import Flask, render_template, request, redirect, url_for, session, flash
from werkzeug.security import generate_password_hash, check_password_hash
from database import get_connection_db

app = Flask(__name__)
app.secret_key = "This is a secret key for session management"

@app.route('/')
def Home():
    return render_template('home.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']

        hashed_password = generate_password_hash(password)

        conn = get_connection_db()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO users (username, email, password) VALUES (?, ?, ?)",
            (username, email, hashed_password)
        )
        conn.commit()
        flash("User registered successfully", "success")
        return redirect(url_for('login'))
        conn.close()

    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        conn = get_connection_db()
        cursor = conn.cursor()
        cursor.execute(
            "SELECT * FROM users WHERE email = ?", (email,)
        )
        user = cursor.fetchone()
        conn.close()

        if user and check_password_hash(user['password'], password):
            session['username'] = user['username']
            flash("Login successful", "success")

            return redirect(url_for('dashboard'))
        flash("Invalid email or password", "danger")
    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    if 'username' not in session:
        flash("Please log in first to access the dashboard", "danger")
        return redirect(url_for('login'))
    return render_template('dashboard.html')

@app.route('/logout')
def logout():
    session.clear()
    flash("You have been logged out successfully", "success")
    return redirect(url_for('login'))

if __name__  == "__main__":
    app.run(debug=True, port = 3000)