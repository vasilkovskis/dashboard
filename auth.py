from flask import Blueprint, render_template, request, redirect, url_for, session, flash
import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash

auth_bp = Blueprint('auth', __name__, url_prefix='/auth')

def get_db():
    conn = sqlite3.connect('users.db')
    conn.row_factory = sqlite3.Row
    return conn

@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = generate_password_hash(request.form['password'])
        role = 'admin'  # Default role; you can expand later to choose roles

        conn = get_db()
        cur = conn.cursor()
        cur.execute("INSERT INTO users (name, email, password, role) VALUES (?, ?, ?, ?)", (name, email, password, role))
        conn.commit()
        conn.close()
        return redirect(url_for('auth.login'))

    return render_template('register.html')


@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        conn = get_db()
        cur = conn.cursor()
        cur.execute("SELECT * FROM users WHERE email = ?", (email,))
        user = cur.fetchone()
        conn.close()

        if user and check_password_hash(user['password'], password):
            session['user_id'] = user['id']
            session['user_name'] = user['name']
            session['user_role'] = user['role']
            return redirect(url_for('index'))
        else:
            flash('Invalid credentials')
            return redirect(url_for('auth.login'))

    return render_template('login.html')


@auth_bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('auth.login'))


@auth_bp.route('/users')
def user_list():
    if session.get('user_role') != 'admin':
        return render_template('access_denied.html')
    conn = get_db()
    cur = conn.cursor()
    cur.execute("SELECT * FROM users")
    users = cur.fetchall()
    conn.close()
    return render_template('users.html', users=users)


@auth_bp.route('/users/add', methods=['GET', 'POST'])
def add_user():
    if session.get('user_role') != 'admin':
        return render_template('access_denied.html')

    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = generate_password_hash(request.form['password'])
        role = request.form['role']

        conn = get_db()
        cur = conn.cursor()
        cur.execute("INSERT INTO users (name, email, password, role) VALUES (?, ?, ?, ?)", (name, email, password, role))
        conn.commit()
        conn.close()
        return redirect(url_for('auth.user_list'))

    return render_template('add_user.html')


@auth_bp.route('/users/edit/<int:user_id>', methods=['GET', 'POST'])
def edit_user(user_id):
    if session.get('user_role') != 'admin':
        return render_template('access_denied.html')

    conn = get_db()
    cur = conn.cursor()
    cur.execute("SELECT * FROM users WHERE id = ?", (user_id,))
    user = cur.fetchone()

    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        role = request.form['role']
        cur.execute("UPDATE users SET name = ?, email = ?, role = ? WHERE id = ?", (name, email, role, user_id))
        conn.commit()
        conn.close()
        return redirect(url_for('auth.user_list'))

    return render_template('edit_user.html', user=user)


@auth_bp.route('/users/delete/<int:user_id>')
def delete_user(user_id):
    if session.get('user_role') != 'admin':
        return render_template('access_denied.html')

    conn = get_db()
    cur = conn.cursor()
    cur.execute("DELETE FROM users WHERE id = ?", (user_id,))
    conn.commit()
    conn.close()
    return redirect(url_for('auth.user_list'))
