Secure C Code Sandbox
A lightweight, cloud-hosted sandbox environment that securely compiles and runs untrusted C code with CPU and memory restrictions — fully built in C and Flask, deployed on Amazon EC2.
Live Demo
🔗 Try it now

Upload a .c file and see it compiled, executed securely, and logged — in real-time.

🛠️ Features
✅ Upload .c files via web UI or REST API

✅ Compiles code with gcc and logs output

✅ Executes inside a custom-built sandbox in C

✅ Enforces strict resource limits:

CPU Time: 2 seconds

Memory: 100 MB

✅ Handles:

Infinite loops

Memory bombs

Segfaults

✅ Web UI + REST API for programmatic access

✅ Cloud-deployed on Amazon EC2

📁 File Structure
bash
Copy
├── sandbox.c            # The secure execution sandbox written in C
├── app.py               # Flask backend (upload + compile + run)
├── index.html           # Frontend UI
├── test_programs/       # Example C files: hello, badMem, infinite loop
├── uploads/             # Uploaded source files (runtime)
├── logs/                # Output logs from executed programs
├── Makefile             # Build automation for sandbox
🧪 Test Programs Included
Test File	Purpose
hello.c	Simple hello world test
badMem.c	Tries to allocate 100 GB
infiniteloop.c	Infinite while loop (CPU abuse)
🧠 Tech Stack
C – Low-level sandbox runner

Flask (Python) – Web server + API

HTML/Jinja2 – UI rendering

Amazon EC2 – Deployed on Ubuntu Linux

GCC – Runtime compilation of uploaded code

##REST API
POST /api/run
Upload a .c file to compile and run.

Request:
multipart/form-data with a field named code
Response (JSON):

json
Copy
{
  "success": true,
  "filename": "hello.c",
  "output": "Hello!",
  "exit_code": 0,
  "execution_time_sec": 0.01,
  "status": "Safe"
}
##Security Considerations
Programs are isolated in a separate process

Resource limits (setrlimit) are enforced before execution

Output is redirected to log files and sanitized before display

Execution timeout prevents infinite loops

Author
Prisha Priyadarshini
📧 Contact Me: prishapriya31@gmail.com
🌐 LinkedIn: https://www.linkedin.com/in/prisha-priyadarshini-ba0519267/
💻 Sophomore CS Major @ TCNJ

📜 License
MIT License – feel free to fork and build upon it!
