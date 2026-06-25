import json
import pandas as pd
import matplotlib.pyplot as plt

# 解决matplotlib中文乱码
plt.rcParams["font.sans-serif"] = ["SimHei", "WenQuanYi Micro Hei"]
plt.rcParams["axes.unicode_minus"] = False

def start_analysis():
    # 读取问卷原始数据
    raw_data = json.load(open("data.json", "r", encoding="utf-8"))
    df = pd.DataFrame(raw_data)
    # 导出Excel汇总表格
    df.to_excel("问卷汇总数据.xlsx", index=False)

    # 创建画布，把4类统计放在一张图里
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))
    fig.suptitle("大学生线上学习问卷数据分析汇总", fontsize=16)

    # 1. 年级分布饼图
    df["grade"].value_counts().plot(kind="pie", autopct="%1.1f%%", ax=axes[0,0])
    axes[0,0].set_title("填写人年级分布")
    axes[0,0].set_ylabel("")

    # 2. 每周线上学习时长统计
    df["study_time"].value_counts().plot(kind="bar", color="#4285F4", ax=axes[0,1])
    axes[0,1].set_title("每周线上课程时长统计")

    # 3. 学习效果自评分布
    df["effect"].value_counts().plot(kind="bar", color="#34A853", ax=axes[1,0])
    axes[1,0].set_title("学习效果自评结果")

    # 4. 学习阻碍统计（拆分多选数据）
    barrier_total = []
    for item in df["barrier"]:
        barrier_total.extend(item)
    pd.Series(barrier_total).value_counts().plot(kind="bar", color="#EA4335", ax=axes[1,1])
    axes[1,1].set_title("线上学习阻碍统计")

    plt.tight_layout()
    # 生成汇总图片，和网页按钮文件名对应
    plt.savefig("数据分析汇总.png", dpi=150)
    plt.close()
    print("数据分析完成，已生成Excel表格和汇总统计图")

if __name__ == "__main__":
    start_analysis()
