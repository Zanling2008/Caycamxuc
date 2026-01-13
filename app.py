from flask import Flask, render_template_string

app = Flask(__name__)

@app.route("/")
def home():
    with open("App1.html", encoding="utf-8") as f:
        return render_template_string(f.read())

if __name__ == "__main__":
    app.run()

