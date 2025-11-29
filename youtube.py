from googleapiclient.discovery import build
import pandas as pd

api_key = "AIzaSyDm5qgRJM1buNLmZKHMm5lRSWqYb1N0VKI"
video_id = "245IOyfGr24"
youtube = build("youtube", "v3", developerKey=api_key)
comments = []
next_page_token = None
while True:
    request = youtube.commentThreads().list(
        part="snippet",
        videoId=video_id,
        maxResults=100,
        pageToken=next_page_token
    )
    response = request.execute()
    for item in response["items"]:
        comment = item["snippet"]["topLevelComment"]["snippet"]["textDisplay"]
        comments.append(comment)

    next_page_token = response.get("nextPageToken")
    if not next_page_token:
        break


df = pd.DataFrame({"comment": comments})
df.to_csv("comments.csv", encoding="utf-8", index=False)

print("Done! Total comments:", len(comments))
