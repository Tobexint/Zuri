from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

@app.route('/api', methods=['GET'])
def get_info():
    slack_name = request.args.get('slack_name')
    track = request.args.get('track')
    github_file_url = 'https://github.com/Tobexint/Zuri/blob/main/app.py'
    github_repo_url = 'https://github.com/tobexint/Zuri'

    utc_time = datetime.utcnow()
    if utc_time.hour < 22 and utc_time.hour > 2:
        return jsonify({
            'slack_name': slack_name,
            'current_day': "Monday",
            'utc_time': str(utc_time),
            'track': track,
            'status': 'Error',
            'message': 'The current UTC time is not within +/- 2 hours.'
            }), 400
    else:
        day_of_week = datetime.utcnow().strftime('%A')
        return jsonify({
            'slack_name': slack_name,
            'current_day': "Monday",
            'utc_time': str(utc_time),
            'track': track,
            'github_url_file': github_file_url,
            'github_repo_url': github_repo_url,
            'status_code': 200,
            }), 200

if __name__ == '__main__':
    app.run(debug=True)
