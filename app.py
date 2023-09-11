from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

@app.route('/info', methods=['GET'])
def get_info():
    name = request.args.get('name')
    track = request.args.get('track')
    github_file_url = 'https://github.com/tobexint'
    github_repo_url = 'https://github.com/tobexint/Zuri'

    current_utc_time = datetime.utcnow()
    if current_utc_time.hour < 22 and current_utc_time.hour > 2:
        return jsonify({
            'slack_name': name,
            'current_day': "Monday",
            'current_utc_time': str(current_utc_time),
            'track': track,
            'status': 'Error',
            'message': 'The current UTC time is not within +/- 2 hours.'
            }), 400
    else:
        day_of_week = datetime.utcnow().strftime('%A')
        return jsonify({
            'slack_name': name,
            'current_day': "Monday",
            'current_utc_time': str(current_utc_time),
            'track': track,
            'github_url_file': github_file_url,
            'github_repo_url': github_repo_url,
            'status_code': 200,
            }), 200

if __name__ == '__main__':
    app.run(debug=True)
