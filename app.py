from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>DevOps Demo</title>
        <style>
            body {
                margin: 0;
                height: 100vh;
                display: flex;
                justify-content: center;
                align-items: center;
                background: #120b3d;
                color: white;
                font-family: Arial, sans-serif;
                text-align: center;
            }

            .container {
                background: #261b70;
                padding: 50px;
                border-radius: 20px;
                box-shadow: 0 0 30px #9d42ff;
            }

            h1 {
                color: #ff4fc3;
                font-size: 50px;
            }

            p {
                font-size: 20px;
                color: #ddddff;
            }
        </style>
    </head>

    <body>
        <div class="container">
            <h1>Welcome to DevOps Demo 🚀</h1>
            <p>Python Flask application running inside Docker.</p>
            <p>Deployed on AWS EC2.</p>
        </div>
    </body>
    </html>
    """


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
