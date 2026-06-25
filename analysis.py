import json
import pandas as pd
import matplotlib.pyplot as plt
# 解决中文乱码
plt.rcParams["font.sans-serif"] = ["SimHei"]
plt.rcParams["axes.unicode_minus"] = False

def analysis():
    # 读取问卷数据
    raw = json.load(open("data.json","r",encoding="utf-8"))
    df = pd.DataFrame(raw)
    # 导出Excel汇总表
    df.to_excel("问卷汇总数据.xlsx", index=False)
    # 绘制3张统计图
    df["gender"].value_counts().plot(kind="pie", autopct="%1.1f%%")
    plt.title("填写人性别分布")
    plt.savefig("性别分布.png")
    plt.close()

    df["day"].value_counts().plot(kind="bar")
    plt.title("每周追剧天数统计")
    plt.savefig("追剧天数.png")
    plt.close()

    df["effect"].value_counts().plot(kind="bar", color="#ff7777")
    plt.title("追剧对学习影响统计")
    plt.savefig("学习影响.png")
    plt.close()
    print("数据分析完成，已生成Excel和三张图表")

if __name__ == "__main__":
    analysis()