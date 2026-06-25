from flask import Flask,render_template,request,jsonify
import json,os
app = Flask(__name__)
DATA_FILE = "data.json"
# 自动创建数据文件
if not os.path.exists(DATA_FILE):
    json.dump([], open(DATA_FILE,"w",encoding="utf-8"), ensure_ascii=False)

# 问卷首页
@app.route("/")
def index():
    return render_template("index.html")

# 接收提交数据
@app.route("/submit", methods=["POST"])
def submit():
    all_data = json.load(open(DATA_FILE,"r",encoding="utf-8"))
    all_data.append(request.get_json())
    json.dump(all_data, open(DATA_FILE,"w",encoding="utf-8"), indent=2, ensure_ascii=False)
    return jsonify({"msg":"提交成功"})

if __name__ == "__main__":
    app.run(debug=True)