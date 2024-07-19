import feedparser
import datetime
import os

rss_urls = [
    "https://www.voachinese.com/api/zm_yqebbyi"
]

if os.path.exists("Push.html"):
    with open("Push.html", "r", encoding="utf-8") as f:
        last_generated = f.readline().strip()
        if last_generated.startswith("生成時間: "):
            last_generated = last_generated.replace("生成時間: ", "")
            last_generated = datetime.datetime.strptime(last_generated, "%Y-%m-%d %H:%M:%S")

            if (datetime.datetime.now() - last_generated).days > 0:
                pass
            else:
                exit()

current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

with open("Push.html", "w", encoding="utf-8") as f:
    f.write(f"生成時間: {current_time}\n")
    f.write(f"<meta charset=\"utf-8\">")

    for rss_url in rss_urls:
        try:
            NewsFeed = feedparser.parse(rss_url)
            print(f"Number of RSS posts from {rss_url}: {len(NewsFeed.entries)}")

            for entry in NewsFeed.entries:
                f.write(f"<h2>{entry.title}</h2>\n")
                f.write(f"{entry.summary_detail.value}\n")
                f.write(f"<a href='{entry.link}'>閱讀全文</a><br><br>\n")
        except:
            print("Error!")