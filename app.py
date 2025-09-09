from flask import Flask, request, jsonify
import tool_logic

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return "✅ HR Tool is Live!"

@app.route("/run", methods=["POST"])
def run_tool():
    data = request.json
    result = tool_logic.run_tool(data)
    return jsonify({"output": result})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
