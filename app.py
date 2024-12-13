from flask import Flask, request, jsonify, render_template
import mysql.connector

app = Flask(__name__)

# Database configuration
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'Anita@123',
    'database': 'proj'
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit_score', methods=['POST'])
def submit_score():
    try:
        data = request.json
        score = data['score']
        game_type = data['game_type']

        # Create a new database connection for each request
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()

        # Insert score into the database
        query = "INSERT INTO game_scores (score, game_type) VALUES (%s, %s)"
        cursor.execute(query, (score, game_type))
        conn.commit()

        # Close the cursor and connection
        cursor.close()
        conn.close()

        return jsonify({'message': 'Score submitted successfully!'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
