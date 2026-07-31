from flask import Flask, request, jsonify
from flask_cors import CORS
import downloader # Assuming your original logic is in here

app = Flask(__name__)
# This allows your GitHub Pages frontend to talk to this backend
CORS(app) 

@app.route('/download', methods=['POST'])
def download_media():
    data = request.json
    media_url = data.get('url')

    if not media_url:
        return jsonify({"error": "No URL provided"}), 400

    try:
        # Call the function from your original downloader.py
        # e.g., result = downloader.process_video(media_url)
        result_link = "URL_TO_YOUR_PROCESSED_FILE" 

        return jsonify({"success": True, "download_link": result_link})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
