from flask import Flask, render_template, redirect, url_for, session
from auth import auth_bp
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)
app.register_blueprint(auth_bp)

@app.route('/')
def index():
    if 'user_id' not in session:
        return redirect(url_for('auth.login'))
    return render_template('dashboard.html', user=session)

if __name__ == '__main__':
    app.run(debug=True)
