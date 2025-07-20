import requests

def get_book_info_aladin(title, api_key):
    url = "http://www.aladin.co.kr/ttb/api/ItemSearch.aspx"
    params = {
        "ttbkey": api_key,
        "Query": title,
        "QueryType": "Title",
        "MaxResults": 1,
        "SearchTarget": "Book",
        "output": "js"
    }
    response = requests.get(url, params=params)
    if response.status_code != 200:
        return None
    data = response.json()
    if "item" not in data or not data["item"]:
        return None
    info = data["item"][0]
    publisher = info.get("publisher", "정보 없음")
    authors = info.get("author", "정보 없음")
    book_title = info.get("title", "정보 없음")
    return book_title, publisher, authors

# 사용 예시
api_key = "여기에_발급받은_API_KEY_입력"
result = get_book_info_aladin("파이썬", api_key)
print(result)