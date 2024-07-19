import feedparser
import datetime
import os

rss_urls = [
    "https://www.voachinese.com/api/zm_yqebbyi"
]

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
