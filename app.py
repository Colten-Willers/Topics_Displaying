from flask import Flask, render_template, request, jsonify
import json
import os

app = Flask(__name__)


current_dir = os.path.dirname(os.path.abspath(__file__))
print(current_dir)
data_file_path = os.path.join(current_dir, "Database", "Data.json")

with open(data_file_path, "r") as f:
    data = json.load(f)


@app.route('/')
def index():
    return render_template('index.html', topics=data.keys(), data=data)

@app.route('/get_data', methods=['POST'])
def get_data():
    try:
        selected_topics = request.json.get('topics', [])
        filtered_data = {topic: data[topic] for topic in selected_topics}
        return jsonify(filtered_data)
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)