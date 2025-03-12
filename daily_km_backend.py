from flask import Flask
from routes.tracker import tracker_bp  # Import Blueprint

app = Flask(__name__)

# Register Blueprint
app.register_blueprint(tracker_bp, url_prefix='/tracker')

@app.route('/')
def home():
    return "Daily KM Tracker is Running!"

if __name__ == '__main__':
    import os
    port = int(os.environ.get("PORT", 5000))  # Use dynamic port for Render
    app.run(host="0.0.0.0", port=port)
