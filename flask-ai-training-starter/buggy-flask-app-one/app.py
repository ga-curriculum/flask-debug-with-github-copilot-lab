from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

# Bug 1: Missing configuration for database
users_db = []

@app.route('/')
def home():
    # Bug 2: Template file doesn't exist
    return render_template('index.html')

@app.route('/api/health')
def health_check():
    # Fixed: Consistent response format for health check
    return jsonify({'status': 'healthy', 'message': 'Service is running'})

@app.route('/api/data')
def get_data():
    # Bug 4: Global variable without initialization check
    if not users_db:
        users_db.append({'id': 1, 'name': 'Alice', 'email': 'alice@example.com'})
        users_db.append({'id': 2, 'name': 'Bob', 'email': 'bob@example.com'})
        users_db.append({'id': 3, 'name': 'Charlie', 'email': 'charlie@example.com'})
    
    return jsonify({
        'users': users_db,
        'count': len(users_db)  # Bug 5: Inconsistent key name (count vs total_count)
    })

@app.route('/api/user/<user_id>')
def get_user(user_id):
    # Bug 6: No input validation - user_id could be non-numeric
    user = next((u for u in users_db if u['id'] == user_id), None)
    if user:
        return jsonify(user)
    else:
        # Bug 7: Should return proper HTTP status code
        return jsonify({'error': 'User not found'})

@app.route('/api/user', methods=['POST'])
def create_user():
    data = request.get_json()
    
    # Bug 8: No input validation
    new_user = {
        'id': len(users_db) + 1,  # Bug 9: Poor ID generation strategy
        'name': data['name'],
        'email': data['email']
    }
    
    users_db.append(new_user)
    return jsonify(new_user)

if __name__ == '__main__':
    # Bug 10: Debug mode enabled in production-like settings
    app.run(debug=True, host='0.0.0.0')