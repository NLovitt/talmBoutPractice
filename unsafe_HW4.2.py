from functools import wraps
from flask import Flask, request, jsonify


app = Flask(__name__)
app.secret_key = b'aee4a10f5'

@app.route('/', methods=['POST'])
def index():
    form = '''<form method="post"> <h1>Delete User Screen</h1>
    <input type="text" placeholder="Enter Username" name="u_name" required>
    <button type="submit">Delete User</button></form>'''

    if request.method == "POST":
        form = delete_account_unsafe()
        # form = delete_account_safe()
    return form

#UNSAFE CODE
def delete_account_unsafe():
    # Some code to delete user account
    user_id = request.form['u_name']
    return "User " + user_id + " deleted successfully"

#SAFE CODE
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not request.headers.get('Authorization'):
            return jsonify({'error': 'Authentication Required'}), 401
        return f(*args, **kwargs)
    return decorated_function

@login_required
def delete_account_safe():
    # Some code to delete user account
    user_id = request.form['u_name']
    print("User" + user_id + "deleted successfully")

if __name__ == '__main__':
    app.run(debug=True)

    