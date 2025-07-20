import requests

def get_book_info(title):
    url = "https://www.googleapis.com/books/v1/volumes"
    params = {"q": f"intitle:{title}", "maxResults": 1}
    response = requests.get(url, params=params)
    if response.status_code != 200:
        return None
    data = response.json()
    if "items" not in data or not data["items"]:
        return None
    info = data["items"][0]["volumeInfo"]
    publisher = info.get("publisher", "정보 없음")
    authors = ", ".join(info.get("authors", ["정보 없음"]))
    return publisher, authors

if __name__ == "__main__":
    while True:
        title = input("책 제목을 입력하세요: ")
        result = get_book_info(title)
        if result:
            publisher, authors = result
            print(f"출판사: {publisher}")
            print(f"글쓴이: {authors}")
        else:
            print("책 정보를 찾을 수 없습니다.")

        end = input("끝낼까요? (네/아니오): ")
        if end.strip() in ["네", "예", "y", "Y"]:
            print("프로그램을 종료합니다.")
            break