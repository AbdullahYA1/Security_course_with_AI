"""Local classroom demo. All keys here are inert training strings."""

import os

from flask import Flask, jsonify, render_template, request


app = Flask(__name__)


@app.get("/")
def index():
    return render_template("index.html", repaired=False)


@app.get("/repaired")
def repaired():
    return render_template("index.html", repaired=True)


@app.post("/api/summary")
def browser_key_summary():
    # Demonstrates the browser sending a key. Never use this pattern for a real key.
    if not request.headers.get("X-Demo-Key"):
        return jsonify(error="Training key missing"), 401
    return jsonify(summary="ركّز هذا الأسبوع على إنهاء واجهة التسجيل وتجربة استعادة كلمة المرور. اجتماع الفريق يوم الخميس لمراجعة النسخة الأولى.")


@app.post("/api/v2/summary")
def server_key_summary():
    # The browser sends no key; a real provider call would use a server-side setting.
    if not os.environ.get("DEMO_SERVER_KEY"):
        return jsonify(error="Set DEMO_SERVER_KEY on the server first"), 503
    return jsonify(summary="ركّز هذا الأسبوع على إنهاء واجهة التسجيل وتجربة استعادة كلمة المرور. اجتماع الفريق يوم الخميس لمراجعة النسخة الأولى.")


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5016, debug=False)
