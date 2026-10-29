# -*- coding: utf-8 -*-
"""
디자인 작업 이미지를 내려받아 사이트에 자체 호스팅합니다.
(기본 상태는 네이버 원본 주소를 불러오는 방식이라, 네이버가 외부 참조를 막으면 이미지가 보이지 않습니다.)

사용:
    python _build/localize_images.py

결과:
    assets/design/<slug>-01.jpg ... 로 저장되고,
    design/*.html 과 index.html 의 이미지 주소가 로컬 경로로 바뀝니다.
"""
import os
import urllib.request

from design import D, IMG, ROOT

OUT = os.path.join(ROOT, "assets", "design")
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/125.0 Safari/537.36",
    "Referer": "https://blog.naver.com/lucid631",
}


def ext(url):
    path = url.split("?")[0].lower()
    return ".png" if path.endswith(".png") else ".jpg"


def download(url, dst):
    if os.path.exists(dst) and os.path.getsize(dst) > 1024:
        return False
    req = urllib.request.Request(url, headers=HEADERS)
    with urllib.request.urlopen(req, timeout=40) as r, open(dst, "wb") as f:
        f.write(r.read())
    return True


def main():
    os.makedirs(OUT, exist_ok=True)
    mapping = {}
    for p in D:
        for i, url in enumerate(IMG[p["slug"]], 1):
            name = f"{p['slug']}-{i:02d}{ext(url)}"
            dst = os.path.join(OUT, name)
            try:
                if download(url, dst):
                    print("saved   ", name)
                else:
                    print("skipped ", name)
                mapping[url] = "assets/design/" + name
            except Exception as e:
                print("failed  ", name, e)

    for p in D:
        path = os.path.join(ROOT, "design", p["slug"] + ".html")
        s = open(path, encoding="utf-8").read()
        for url, local in mapping.items():
            s = s.replace(url, "../" + local)
        open(path, "w", encoding="utf-8").write(s)

    idx = os.path.join(ROOT, "index.html")
    s = open(idx, encoding="utf-8").read()
    for p in D:
        first = IMG[p["slug"]][0]
        if first in mapping:
            s = s.replace(first, mapping[first])
    open(idx, "w", encoding="utf-8").write(s)
    print("done:", len(mapping), "images")


if __name__ == "__main__":
    main()
