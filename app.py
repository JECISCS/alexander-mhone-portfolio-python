from pathlib import Path

from flask import Flask, render_template, send_from_directory
from data.profile import INNER_SKILLS, OUTER_SKILLS
from data.projects import PROJECTS

PUBLIC_STATIC = Path(__file__).resolve().parent / "public" / "static"
PUBLIC_DIRECTORY = PUBLIC_STATIC.parent

app = Flask(__name__, static_folder=None)

@app.route("/")
def home():
    return render_template(
        "index.html",
        projects=PROJECTS,
        outer_skills=OUTER_SKILLS,
        inner_skills=INNER_SKILLS,
    )

@app.route("/health")
def health():
    return {"status": "ok"}, 200


@app.get("/static/<path:filename>")
def local_static(filename: str):
    return send_from_directory(PUBLIC_STATIC, filename, conditional=True)


@app.get("/cv.pdf")
def local_cv():
    return send_from_directory(PUBLIC_DIRECTORY, "cv.pdf", conditional=True)


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
