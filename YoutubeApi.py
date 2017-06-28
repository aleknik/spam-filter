import json
import urllib.parse
import urllib.request


def get_comments(videoId):
    comments = []

    params = urllib.parse.urlencode(
        {'videoId': videoId, 'part': 'snippet', "key": "AIzaSyBrh01_Coeu5x0qxG5KMP26TuG2nr9gitA", "order": "time"})
    content = urllib.request.urlopen("https://www.googleapis.com/youtube/v3/commentThreads?" + params).read()

    response = json.loads(content.decode('utf-8'))
    next_page = response["nextPageToken"]
    for thread in response["items"]:
        comment = thread["snippet"]["topLevelComment"]["snippet"]
        comments.append(comment["textOriginal"])

    for i in range(5):
        params = urllib.parse.urlencode(
            {'videoId': videoId, 'part': 'snippet', "key": "AIzaSyBrh01_Coeu5x0qxG5KMP26TuG2nr9gitA", "order": "time",
             "pageToken": next_page})
        content = urllib.request.urlopen("https://www.googleapis.com/youtube/v3/commentThreads?" + params).read()

        response = json.loads(content.decode('utf-8'))
        next_page = response["nextPageToken"]
        for thread in response["items"]:
            comment = thread["snippet"]["topLevelComment"]["snippet"]
            comments.append(comment["textOriginal"])
    return comments


if __name__ == "__main__":
    print(get_comments("H_tA_pc05f8"))
