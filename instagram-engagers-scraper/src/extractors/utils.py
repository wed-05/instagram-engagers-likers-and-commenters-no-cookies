thonimport json

def clean_data(data):
    cleaned_data = []
    for item in data:
        cleaned_item = {
            "type": item.get("type"),
            "link_post": item.get("link_post"),
            "comment_like_count": item.get("comment_like_count"),
            "created_at": item.get("created_at"),
            "hashtags": item.get("hashtags"),
            "like_count": item.get("like_count"),
            "mentions": item.get("mentions"),
            "text": item.get("text"),
            "link_user": item.get("link_user"),
            "user": item.get("user")
        }
        cleaned_data.append(cleaned_item)
    return cleaned_data