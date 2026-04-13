import requests
import json

COMPLEX_LIST = ["3748"]


def get_articles(complex_no):
    url = "https://new.land.naver.com/api/articles"

    params = {
        "complexNo": complex_no,
        "tradeType": "A1",   # 매매
        "realEstateType": "APT",
        "tag": "::::::::",
        "rentPriceMin": 0,
        "rentPriceMax": 900000000,
        "priceMin": 0,
        "priceMax": 900000000,
        "areaMin": 0,
        "areaMax": 999999,
        "page": 1
    }

    headers = {
        "User-Agent": "Mozilla/5.0",
        "Referer": f"https://new.land.naver.com/complexes/{complex_no}",
        "Accept-Language": "ko-KR,ko;q=0.9"
    }

    res = requests.get(url, params=params, headers=headers)

    print("status:", res.status_code)
    print("response:", res.text[:200])  # 디버깅용

    if res.status_code != 200:
        return []

    data = res.json()

    article_list = data.get("articleList", [])

    if not article_list:
        print("❗ 매물 없음 (파라미터 문제 가능)")

    result = []

    for item in article_list:
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
        data = get_articles(c)
        print(f"{c} → {len(data)}개 수집")
        all_data.extend(data)

    with open("data.json", "w", encoding="utf-8") as f:
        json.dump(all_data, f, ensure_ascii=False, indent=2)

    print("✅ data.json 업데이트 완료")


if __name__ == "__main__":
    main()
