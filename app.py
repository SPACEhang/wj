from flask import Flask, render_template, request, jsonify
import json
import os

app = Flask(__name__)
DATA_FILE = "data.json"

# 初始化空数据文件
if not os.path.exists(DATA_FILE):
    json.dump([], open(DATA_FILE, "w", encoding="utf-8"), ensure_ascii=False, indent=2)

@app.route('/')
def index():
    return render_template('index.html')

# 问卷数据提交接口
@app.route('/submit', methods=["POST"])
def submit():
    try:
        new_info = request.get_json()
        all_data = json.load(open(DATA_FILE, "r", encoding="utf-8"))
        all_data.append(new_info)
        json.dump(all_data, open(DATA_FILE, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
        return jsonify({"code":200, "msg":"成功"})
    except Exception as err:
        return jsonify({"code":500, "msg":"失败", "error":str(err)}),500

if __name__ == '__main__':
    app.run(debug=True)
