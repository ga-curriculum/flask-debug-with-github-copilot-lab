from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

# NOTE: Using an in-memory list as a mock database for demonstration purposes.
users_db = []

@app.route('/')
def home():
    # Bug 2: Template file doesn't exist
    return render_template('index.html')

@app.route('/api/health')
def health_check():
    return jsonify({'status': 'healthy', 'message': 'Flask app is running'})

@app.route('/api/data')
def get_data():
    # Bug 4: Global variable without initialization check
    if not users_db:
        users_db.append({'id': 1, 'name': 'Alice', 'email': 'alice@example.com'})
        users_db.append({'id': 2, 'name': 'Bob', 'email': 'bob@example.com'})
        users_db.append({'id': 3, 'name': 'Charlie', 'email': 'charlie@example.com'})
    
    return jsonify({
        'users': users_db,
        'total_count': len(users_db)
    })

@app.route('/api/user/<user_id>')
def get_user(user_id):
    try:
        user_id = int(user_id)
    except ValueError:
        return jsonify({'error': 'Invalid user ID'}), 400
    user = next((u for u in users_db if u['id'] == user_id), None)
    if user:
        return jsonify(user)
    else:
        return jsonify({'error': 'User not found'}), 404

@app.route('/api/user', methods=['POST'])
def create_user():
    data = request.get_json()

    if not data or 'name' not in data or 'email' not in data:
        return jsonify({'error': 'Invalid input'}), 400
    
    # Bug 8: No input validation
    new_user = {
        'id': len(users_db) + 1,  # Bug 9: Poor ID generation strategy
        'name': data['name'],
        'email': data['email']
    }
    
    users_db.append(new_user)
    return jsonify(new_user), 201

if __name__ == '__main__':
    # Bug 10: Debug mode enabled in production-like settings
    app.run(debug=True, host='0.0.0.0', port=5001)