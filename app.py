from flask import Flask, request, render_template, jsonify, redirect, session, url_for
from flask_session import Session
import time
import subprocess
import os

app = Flask(__name__)
app.config['SESSION_PERMANENT'] = False
app.config['SESSION_TYPE'] = "filesystem"
Session(app)

os.makedirs("uploads", exist_ok=True)
os.makedirs("logs", exist_ok=True)

def compileAndRun(uploadedFile):
    filename = uploadedFile.filename
    if not filename.endswith(".c"):
        return {
            "success": False,
            "error": "Only .c files are allowed",
            "filename": filename
        }

    uploadPath = os.path.join("uploads", filename)
    execPath = os.path.join("uploads", "program")
    logPath = os.path.join("logs", "output.txt")

    uploadedFile.save(uploadPath)

    result = subprocess.run(["gcc", uploadPath, "-o", execPath], capture_output=True, text=True)
    if result.returncode != 0:
        return {
            "success": False,
            "error": "Compilation failed",
            "stderr": result.stderr,
            "filename": filename
        }

    start = time.time()
    run_result = subprocess.run(["./sandbox", execPath, logPath])
    duration = round(time.time() - start, 2)

    with open(logPath, "r") as file:
        output = file.read()

    return {
        "success": True,
        "filename": filename,
        "output": output,
        "exit_code": run_result.returncode,
        "execution_time_sec": duration,
        "status": "Safe" if run_result.returncode == 0 else "Crashed or Unsafe"
    }

@app.route("/run", methods=["GET", "POST"])
def runCode():
    if request.method == "POST":
        if "code" not in request.files:
            return render_template("index.html", output="Error: No file uploaded.")

        result = compileAndRun(request.files["code"])

        if not result["success"]:
            return render_template("index.html", output=f"Error: {result['error']}\n{result.get('stderr', '')}")

        status = f"{result['status']} | Execution Time: {result['execution_time_sec']}s | Exit Code: {result['exit_code']}"
        return render_template("index.html", output=result["output"], filename=result["filename"], status=status)

    return render_template("index.html")

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/api/run", methods=["POST"])
def apiCode():
    if "code" not in request.files:
        return jsonify({"success": False, "error": "No file uploaded"}), 400

    result = compileAndRun(request.files["code"])

    if not result["success"]:
        return jsonify(result), 400

    return jsonify(result), 200

if __name__ == "__main__":
    app.run(debug=True)
