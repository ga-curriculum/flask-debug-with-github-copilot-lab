from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/health')
def health_check():
    return jsonify({'status': 'healthy', 'message': 'Flask app is running'})

@app.route('/api/data')
def get_data():
    sample_data = {
        'users': [
            {'id': 1, 'name': 'Alice', 'email': 'alice@example.com'},
            {'id': 2, 'name': 'Bob', 'email': 'bob@example.com'},
            {'id': 3, 'name': 'Charlie', 'email': 'charlie@example.com'}
        ],
        'total_count': 3
    }
    return jsonify(sample_data)

if __name__ == '__main__':
    app.run(debug=True)