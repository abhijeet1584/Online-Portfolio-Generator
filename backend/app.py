from flask import Flask, request, send_file
from jinja2 import Environment, FileSystemLoader
from flask_cors import CORS
from weasyprint import HTML
import json

app = Flask(__name__)

CORS(app)

env = Environment(loader=FileSystemLoader("backend"))

@app.route("/generate", methods=["POST"])
def generate():
    data = request.json
    data["skills"] = data["skills"].split(",")

    template = env.get_template("template.html")
    html = template.render(data)

    with open("resume.html", "w") as f:
        f.write(html)

    HTML("resume.html").write_pdf("resume.pdf")
    # HTML(string=html).write_pdf("resume.pdf")


    return send_file("../resume.pdf", as_attachment=True)

if __name__ == "__main__":
    app.run()
