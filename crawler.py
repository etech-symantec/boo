import requests
import json

# 여러 단지 한번에 처리 가능
COMPLEX_LIST = ["3748"]


def get_articles(complex_no):
    url = "https://new.land.naver.com/api/articles"

    params = {
        "complexNo": complex_no,
        "tradeType": "A1",   # 매매
        "realEstateType": "APT",
        "page": 1
    }

    headers = {
        "User-Agent": "Mozilla/5.0",
        "Referer": "https://new.land.naver.com/"
    }

    res = requests.get(url, params=params, headers=headers)
    data = res.json()

    result = []

    for item in data.get("articleList", []):
        result.append({
            "complexNo": str(complex_no),
            "dong": item.get("buildingName"),
            "floor": item.get("floorInfo"),
            "area": item.get("areaName"),
            "price": item.get("dealOrWarrantPrc"),
            "type": item.get("tradeTypeName"),
            "agent": item.get("realtorName"),
            "link": f"https://new.land.naver.com/articles/{item.get('articleNo')}"
        })

    return result


def main():
    all_data = []

    for c in COMPLEX_LIST:
        all_data.extend(get_articles(c))

    with open("data.json", "w", encoding="utf-8") as f:
        json.dump(all_data, f, ensure_ascii=False, indent=2)

    print("data.json 업데이트 완료")


if __name__ == "__main__":
    main()
