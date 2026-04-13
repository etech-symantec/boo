import requests
import time
import random

def get_articles(complex_no):
    url = "https://new.land.naver.com/api/articles"

    headers = {
        "User-Agent": random.choice([
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)"
        ]),
        "Referer": f"https://new.land.naver.com/complexes/{complex_no}",
        "Accept-Language": "ko-KR,ko;q=0.9",
    }

    params = {
        "complexNo": complex_no,
        "tradeType": "A1",
        "realEstateType": "APT",
        "page": 1
    }

    time.sleep(random.uniform(3, 7))  # 핵심

    res = requests.get(url, params=params, headers=headers)

    print("status:", res.status_code)

    if res.status_code != 200:
        return []

    return res.json().get("articleList", [])
