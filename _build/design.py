# -*- coding: utf-8 -*-
"""
디자인 작업 갤러리 생성기
- design/<slug>.html 생성
- index.html 의 DESIGN_CARDS_START / END 사이 카드 목록 갱신
사용: python _build/design.py
"""
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "design")
BLOG = "https://blog.naver.com/lucid631/"

IMG = {
    "holder": [
        "https://postfiles.pstatic.net/MjAyNDA0MzBfMTA2/MDAxNzE0NDYwMDYzODU3.d9mrK87cCRb_ntJtAulCyz5Atb5A6SNiyL2ZWUYQQfUg.bDkUC0p0-2NS6NACvVYGmL9ztc3PfZgtd8-W5CSGcuEg.PNG/%EB%B0%94%EB%94%94%EC%8A%AC%EB%A6%BD_%EC%A7%91%EA%B8%B0.png?type=w966",
        "https://postfiles.pstatic.net/MjAyNDA0MzBfMjMy/MDAxNzE0NDYwMDYzODM5.oeqiya8slsREqiexJjO0iDw4E6TDdkaH2b_Wt1EJiFog.SXDulfJGopcWLHSV78FeWw5ywoyiJ9euVLwucSgToFwg.PNG/20231209_211016.png?type=w966",
        "https://postfiles.pstatic.net/MjAyNDA0MzBfMjI5/MDAxNzE0NDYwMDgyOTk1.I72q0qahGMieO5WQz3HABAjfe6hulQR595Z6kTSp3twg.8SAS98BwRh_0b2aRZOAhIpI-0TZA0htbOcO6mJVs7aEg.PNG/%ED%8F%AC%EB%9D%BC,_%EC%98%A4%EB%AF%80%EB%A1%A0_%EA%B0%9C%EB%B3%84%EC%A7%91%EA%B8%B0_%EC%B7%A8%ED%95%A9%EB%82%B4%EC%9A%A9_0530.png?type=w966",
        "https://postfiles.pstatic.net/MjAyNDA0MzBfMjQ1/MDAxNzE0NDYwMDgyOTY3.y8u1QqxfbMYmnxBcWWk89GlM5HBDpxmZbdUASXEcsHcg.KLVXH8zD-_2k69F_nGBC6N36VSGOWukvcoCD9QHgxdQg.PNG/%EC%9D%B8%EB%B0%94%EB%94%94_%EA%B0%9C%EB%B3%84%EC%A7%91%EA%B8%B0_%EC%B7%A8%ED%95%A9%EB%82%B4%EC%9A%A9.png?type=w966",
        "https://postfiles.pstatic.net/MjAyNDA0MzBfMjU2/MDAxNzE0NDYwMDgyOTcx.tDKxztbRKjm9_BjzZZQ3GBnN8duqQxu8jeuCXl3KcJ8g.8KTAsYWsD7C_2KQmxHkpwVKQlcR39wpYET1zYAFtHLog.PNG/%ED%8F%AC%EB%9D%BC,_%EC%98%A4%EB%AF%80%EB%A1%A0_%EA%B0%9C%EB%B3%84%EC%A7%91%EA%B8%B0_%EC%B7%A8%ED%95%A9%EB%82%B4%EC%9A%A9_2.png?type=w966",
        "https://postfiles.pstatic.net/MjAyNDA0MzBfMzUg/MDAxNzE0NDYwMDk0MDkz.aC-bxuvtrNnia6JwbOucW5mgzILyv6o7KKHSLPCzyfYg.n89SF6OA0yHw2kOPGki1kkREP1RaNAXSNOowKrhUsKYg.PNG/231006_%ED%8E%98%ED%8E%99%ED%95%98%EC%9D%B4%EB%A7%88%ED%8A%B8_.png?type=w966",
        "https://postfiles.pstatic.net/MjAyNDA0MzBfMTk5/MDAxNzE0NDYwMDk0MDg2.YdW3_oUskl9VeANnSCc7Oe2Ydw-Bs_ylpMuIs7Ivdrcg.Ukmwdu821QEC31IyssLFD0D4Lnv8Zp92eJDjb-RVHd8g.PNG/231006_%ED%8E%98%ED%8E%99%ED%95%98%EC%9D%B4%EB%A7%88%ED%8A%B8_2.png?type=w966",
        "https://postfiles.pstatic.net/MjAyNDA0MzBfMTcx/MDAxNzE0NDYwMDk0MTA0.EG1DzhqRJVwv9KHM7nioWiIflR3R3HJ7SDd2WBQbp7cg.2Cy6JCpVq0u2v2Sligk7Cf-RWGfJQh70m6XL6E2Y7uwg.PNG/10.06_%EC%A5%AC%EB%B2%A0%EB%9D%BC_%EC%B5%9C%EC%A2%85.png?type=w966",
    ],
    "pop": [
        "https://postfiles.pstatic.net/MjAyNDA0MzBfNTUg/MDAxNzE0NDU5OTk5MjA0.jRmvX77De8KCoT3lTZXPb2SAKK9dwZLNiLbuzHmyxS4g.6DC_Wazc5YqTtD_7nAvM7ruPC8Cy1NiOBGr1hlReFo0g.JPEG/%EA%B3%A0%EC%9A%94%EC%9E%A0_POP.jpg?type=w966",
        "https://postfiles.pstatic.net/MjAyNDA0MzBfMjcw/MDAxNzE0NDU5OTk5MDMx.xQW30_65hIkm9j7Ld4dZpJn0ozGWdbuQqG2FxQ7PKlAg.NZ_8M8hLvEGCrdIWCA_4VdOmzt7MrbBWPn46XwxA3qQg.JPEG/%EA%B3%A0%EC%9A%94%EC%9E%A0s_POP.jpg?type=w966",
        "https://postfiles.pstatic.net/MjAyNDA0MzBfMTEy/MDAxNzE0NDU5OTk5MjIy.Gk1jc5zzVBQxbFeIV8YhZyYH7e2XpsyAMMXbOWeQ8lcg.n-dHQE8-YvKiPFA_DMrmnv7C3zKnr8zSqEzxSOqyzL0g.JPEG/%EB%B0%94%EB%94%94%ED%94%84%EB%9D%BC%EC%9E%84_%EB%B9%84%EA%B0%95%ED%99%95%EC%9E%A5%EA%B8%B0_POP.jpg?type=w966",
        "https://postfiles.pstatic.net/MjAyNDA0MzBfMTQ2/MDAxNzE0NDU5OTk5MTY3.07dyY29cEruIP2hoqty3T6pWysFSXzzfaaY47BJr_S0g.v47gpA7Y30exWuofy3PFsQs79P9xFydSzQFQchwh95Ug.JPEG/%EB%B0%94%EB%94%94%ED%94%84%EB%9D%BC%EC%9E%84_%EB%B9%84%EA%B0%95%ED%99%95%EC%9E%A5%EA%B8%B0_%EB%B8%94%EB%9E%99POP.jpg?type=w966",
        "https://postfiles.pstatic.net/MjAyNDA0MzBfNDIg/MDAxNzE0NDU5OTk4Nzcw.51cjDuELygkMf5JRh7x-J1qcodL6lGdAYoKxxouM4vkg.Vvhe2sPynUtaoDogIDQd5jDHDMqwcs8qD0F_FmNoAHIg.JPEG/%EC%8A%AC%EB%A6%AC%ED%94%BC%EC%86%94_POP.jpg?type=w966",
        "https://postfiles.pstatic.net/MjAyNDA0MzBfNTQg/MDAxNzE0NDYwMDEzNTkz.jsqKzADdLM--rDq-vMCyJSe19Dnbi8F2HPQbcE0QsNsg.HTITQnRh9Sq3ZXqxhGk5niQB--ZT4ramXoZzskiVLtIg.JPEG/ECO-22_%ED%94%8C%EB%9F%AC%EC%8A%A4_%EC%B5%9C%EC%A2%85.jpg?type=w966",
        "https://postfiles.pstatic.net/MjAyNDA0MzBfMTEx/MDAxNzE0NDYwMDEzNjQw.WCvlE6rwtiGoe6xXoFEAox_SYi6QQZzyaOh6mjWKloEg.rC-cGsGuOCiSdD8VqPoZxf0u9cj_IDId6gtqKanyzcsg.JPEG/ECO-33_%ED%94%8C%EB%9F%AC%EC%8A%A4_%EC%B5%9C%EC%A2%85.jpg?type=w966",
        "https://postfiles.pstatic.net/MjAyNDA0MzBfMTY4/MDAxNzE0NDYwMDEzMjQx.fNn4vZvryg5Ug8gyWQux7ElENH0IIVtrxE_mvkrC9asg.2zWe7iEtLjJ6NLE9pjon0g_H-I8Lp5SzCk0eQpUbnlUg.JPEG/ECO-202_%EC%95%84%EB%A6%AC_%EC%B5%9C%EC%A2%85.jpg?type=w966",
        "https://postfiles.pstatic.net/MjAyNDA0MzBfMjI2/MDAxNzE0NDYwMDEzODMz.8UbKP8TPv-YzaFpA2z3NZNavFasWh4KI4yCQ5J7BA6Mg.NY3OkT79C__DYfj-tz-hSyXZLFcxE8K4VhBbMy0x8Psg.JPEG/ECO-203_%EC%B5%9C%EC%A2%85.jpg?type=w966",
    ],
    "backpanel": [
        "https://postfiles.pstatic.net/MjAyNDA0MzBfMjc0/MDAxNzE0NDU5ODMzMzQ1.AI2TQlittCfalfkq0RH_RJ9Q5CK74eAD9x7akCC8JHcg.HUGwTjmXUt3Fg8sYBgfLNzq9s2xBmSZ9cTbJyRaozrgg.PNG/%EB%B3%B4%EB%8B%A4%EB%82%98_%EB%B0%B1%EC%9B%94_%EC%B7%A8%ED%95%A9%EB%82%B4%EC%9A%A9_0613.png?type=w966",
        "https://postfiles.pstatic.net/MjAyNDA0MzBfMTg0/MDAxNzE0NDU5ODMzMzIz.-n_XtxvsPtU7Fgwzekrv082DasLWlZ4F23VQ-q3wklAg.TnO_bMmC3M4smy5dheofajlo3l5VxXzfPRVcjredXoQg.PNG/%EC%9A%94%EC%9D%B4%EC%B9%98_%EB%B0%B1%EC%9B%94_%EC%82%AC%ED%95%98%EC%A0%90.png?type=w966",
        "https://postfiles.pstatic.net/MjAyNDA0MzBfNDkg/MDAxNzE0NDU5ODMzMzQ2.GXwdq40ndMCf6drmdi9SZO2pbZZraP8IRrTbHkV6lLog.6GfkBHeHXg-Qf1SXP-hw129wdw6Dfbqd20W0eXt42QEg.PNG/%EC%9D%98%EB%A3%8C%EA%B8%B0%EA%B8%B0_%EB%B0%B1%EC%9B%94_%EC%B7%A8%ED%95%A9%EB%82%B4%EC%9A%A9_2.png?type=w966",
        "https://postfiles.pstatic.net/MjAyNDA0MzBfNzUg/MDAxNzE0NDU5ODMzMzU0.3VrDUluWvxz18GMd_RadKYVZooMktIKkmR_Sj31pqKYg.kMylG36HAAwzXaI9LAAemv0ezaDxHUo2H_dXDD6n060g.PNG/%EC%9D%98%EB%A3%8C%EA%B8%B0%EA%B8%B0_%EB%B0%B1%EC%9B%94_%EC%B7%A8%ED%95%A9%EB%82%B4%EC%9A%A9_0526.png?type=w966",
        "https://postfiles.pstatic.net/MjAyNDA0MzBfMjk3/MDAxNzE0NDU5ODc5MjM2.IPnkpf-2-drpMUib_f90tlYAHu1L1wgBY5ztseGQ81cg.6ZXxY9v8OwT1iUjlSfKAseMbNZux_e9PID4VFliTjOYg.JPEG/%EC%88%98%EB%A9%B4%EA%B0%80%EC%A0%84_%EB%B0%B1%EC%9B%94_%EC%8B%9C%EC%95%882_%EC%8B%9C%EC%95%881%EC%88%98%EC%A0%95.jpg?type=w966",
        "https://postfiles.pstatic.net/MjAyNDA0MzBfMiAg/MDAxNzE0NDU5ODc5MjQy.8lbBVAcW60sw48i1r5zOjA_js9ojH-ssyv3OstAA3J0g.UfKwq8oSLNIQtu3Duf7VLpeiiDR45gFhCyn3Z9gxISEg.JPEG/%EC%88%98%EB%A9%B4%EA%B0%80%EC%A0%84_%EB%B0%B1%EC%9B%94_%EC%8B%9C%EC%95%882_%EC%8B%9C%EC%95%882.jpg?type=w966",
        "https://postfiles.pstatic.net/MjAyNDA0MzBfOTQg/MDAxNzE0NDU5ODc5MjU4.WjBnx7G7AEA3Iz9Vr3HC6f3iccKP5bR5PiJR4L8cKn8g.gdxieSKOBARjhStlOX6U7X8RcyqC_03DIHbqSvzdo7wg.JPEG/%EC%88%98%EB%A9%B4%EA%B0%80%EC%A0%84_%EB%B0%B1%EC%9B%94_%EC%8B%9C%EC%95%883_%EC%8B%9C%EC%95%883.jpg?type=w966",
    ],
    "11st": [
        "https://postfiles.pstatic.net/MjAyNDA0MzBfMTIg/MDAxNzE0NDU4NjY5ODMw.VfG5hJmcaLg-m17x3iPyu9y4YSpwfG3zNIVdfFMRBaIg.YrEBsc6dWYGd1H6H-gEs-QyyuFNGe8SlOXCaxDyRrwog.JPEG/%EC%94%BD%EA%B3%A0_%EC%96%B4%EB%A6%B0%EC%9D%B4%EB%82%A0_%EC%9D%B4%EB%B2%A4%ED%8A%B8_11%EB%B2%88%EA%B0%80.jpg?type=w966",
        "https://postfiles.pstatic.net/MjAyNDA0MzBfNjQg/MDAxNzE0NDU4Njg0NjM5.bcy1WvTUIaYJN2sG6x52ozTDvDPGrsqjNrDHs_921c4g.kiB9wXObudvKpISl6xNtFIp4J3dearvn3T2NKX_lvaAg.JPEG/%EC%94%BD%EA%B3%A0_%EC%B9%B4%EB%93%9C%EB%B7%B0.jpg?type=w966",
        "https://postfiles.pstatic.net/MjAyNDA0MzBfMjkz/MDAxNzE0NDU4Njg5MDQz.k0kZ3o-WUFxGvoxWCpSrlxlryEKhR1ONPC6Xs8k2uREg.avEQmZbF2bKQlnCvD4UsRBjUEZgZUK9QYikg2N1T6Hog.PNG/%EC%94%BD%EA%B3%A0_%EC%B9%B4%EB%93%9C%EB%B7%B02.png?type=w966",
        "https://postfiles.pstatic.net/MjAyNDA0MzBfMTg2/MDAxNzE0NDU4NzAwNzIy.F-Q0yWaN3JCgmRMlpyjCgLsw3oPrH-Cz8YfpC0BEo68g.FSGA7Rw60nA_WKMhyLIdwHSpL76BRtkufordJgS9_rQg.PNG/%EC%94%BD%EA%B3%A0_%EC%BA%90%EB%A6%AD%ED%84%B0_%EB%94%94%EC%9E%90%EC%9D%B8.png?type=w966",
    ],
    "circulator": [
        "https://postfiles.pstatic.net/MjAyNDA0MzBfNyAg/MDAxNzE0NDU4NTQ2NTQ3.6UYOmDm7Xe2S4bptKyKDXxvMqphkia9xc9BgIEpWqgwg.r63Fl5xgsf-SNTl-b31AuWsSBTGZxCXQPGqtBpwdPucg.JPEG/%EC%97%90%EC%96%B4_%EC%84%9C%ED%81%98%EB%A0%88%EC%9D%B4%ED%84%B0_%EC%83%81%EC%84%B8%ED%8E%98%EC%9D%B4%EC%A7%80_%EC%B5%9C%EC%A2%85%EB%B3%B8.jpg?type=w966",
    ],
    "induction": [
        "https://postfiles.pstatic.net/MjAyNDA0MzBfMTA4/MDAxNzE0NDU4NDc3NTc1.KysAV3jPrFOZ1W5CH7wk_Czq-yONROQnL0zfdPTYt34g.xgeZNPJ7TJ_0uZg86Xvb7xmZxtIc9aIgADaJDDKYH5Ag.JPEG/%ED%95%98%EC%9D%B4%EB%A9%94%EC%9D%B4%EB%93%9C_1%EA%B5%AC%EC%9D%B8%EB%8D%95%EC%85%98_%EC%83%81%EC%84%B8%ED%8E%98%EC%9D%B4%EC%A7%80_%EC%B5%9C%EC%A2%85.jpg?type=w966",
    ],
    "report": [
        "https://postfiles.pstatic.net/MjAyNDA0MzBfMTQz/MDAxNzE0NDU0Nzg2Njk5.J6nI5KFwQbV8hc6MOI8F4lgqxpSq7AxzPucInHnmuJEg.mZvQ9N6-O_qbzaikcJPdFwB290lRYhxVsHulcxoE4s8g.JPEG/Venus%EA%B2%B0%EA%B3%BC%EB%B3%B4%EA%B3%A0%EC%84%9C-%ED%95%B4%ED%94%BC%ED%95%80%ED%95%80(%EC%B5%9C%EC%A2%85_%EC%88%98%EC%A0%95%EB%B3%B8)-%EC%9D%B4%EB%AF%B8%EC%A7%80-1.jpg?type=w966",
        "https://postfiles.pstatic.net/MjAyNDA0MzBfNzQg/MDAxNzE0NDU0Nzg2NjM1.RhJ0_WKktm3a4RfRApdmtZI0aDZB8TTktwNmTfaVlYEg.5XJeXONqdD5eICLhkiQytEbAAtOMrcrUMc6YtzJemeUg.JPEG/Venus%EA%B2%B0%EA%B3%BC%EB%B3%B4%EA%B3%A0%EC%84%9C-%ED%95%B4%ED%94%BC%ED%95%80%ED%95%80(%EC%B5%9C%EC%A2%85_%EC%88%98%EC%A0%95%EB%B3%B8)-%EC%9D%B4%EB%AF%B8%EC%A7%80-2.jpg?type=w966",
        "https://postfiles.pstatic.net/MjAyNDA0MzBfMjg3/MDAxNzE0NDU0Nzg2NjY5.IaA6rzrhxKR8Ubns5osTmXrVWoCy-uSD101nPT-NZCkg.VE5t8VSBMiBJPIZr6XQ9_7xmIhBEKBsPcsahOwH0ujIg.JPEG/Venus%EA%B2%B0%EA%B3%BC%EB%B3%B4%EA%B3%A0%EC%84%9C-%ED%95%B4%ED%94%BC%ED%95%80%ED%95%80(%EC%B5%9C%EC%A2%85_%EC%88%98%EC%A0%95%EB%B3%B8)-%EC%9D%B4%EB%AF%B8%EC%A7%80-3.jpg?type=w966",
        "https://postfiles.pstatic.net/MjAyNDA0MzBfMTcy/MDAxNzE0NDU0Nzg2Njg4.ZpOifEWcR4bBQmhqN2-uiKrrHK14mFpRFwcGlTMA_fQg.xwThC9V4muyskw6irJLyWLszvtHr7YiifgDEoMFAPEYg.JPEG/Venus%EA%B2%B0%EA%B3%BC%EB%B3%B4%EA%B3%A0%EC%84%9C-%ED%95%B4%ED%94%BC%ED%95%80%ED%95%80(%EC%B5%9C%EC%A2%85_%EC%88%98%EC%A0%95%EB%B3%B8)-%EC%9D%B4%EB%AF%B8%EC%A7%80-4.jpg?type=w966",
        "https://postfiles.pstatic.net/MjAyNDA0MzBfODgg/MDAxNzE0NDU0Nzg2Njg4.YYGip7pDjWfckLCbyBeR8Mz2u2PAYBTf2nKEH9cxY-Ug.sgbRyeD-lAY1kRJKtppEwFHkRL4UfrQF4QXkhKWHcLIg.JPEG/Venus%EA%B2%B0%EA%B3%BC%EB%B3%B4%EA%B3%A0%EC%84%9C-%ED%95%B4%ED%94%BC%ED%95%80%ED%95%80(%EC%B5%9C%EC%A2%85_%EC%88%98%EC%A0%95%EB%B3%B8)-%EC%9D%B4%EB%AF%B8%EC%A7%80-6.jpg?type=w966",
        "https://postfiles.pstatic.net/MjAyNDA0MzBfMjU2/MDAxNzE0NDU0Nzg3MzQ2.CcLyVzVndab4g67rXnKzZdP7xqsSWFAxx0tpFwrxTNUg.5jwqguy_V4_bzD0iJnU9GrNGnjs1UhX4APsnltKf0okg.JPEG/Venus%EA%B2%B0%EA%B3%BC%EB%B3%B4%EA%B3%A0%EC%84%9C-%ED%95%B4%ED%94%BC%ED%95%80%ED%95%80(%EC%B5%9C%EC%A2%85_%EC%88%98%EC%A0%95%EB%B3%B8)-%EC%9D%B4%EB%AF%B8%EC%A7%80-7.jpg?type=w966",
        "https://postfiles.pstatic.net/MjAyNDA0MzBfODQg/MDAxNzE0NDU0Nzg3MzUw.MuRQbtobIP0rfYr1nvSAoi4evlX3wBzLUCniGL4Et98g.mbmPr45uehw4EfcOcglLer1we6g2iHQAio4ovv85xeUg.JPEG/Venus%EA%B2%B0%EA%B3%BC%EB%B3%B4%EA%B3%A0%EC%84%9C-%ED%95%B4%ED%94%BC%ED%95%80%ED%95%80(%EC%B5%9C%EC%A2%85_%EC%88%98%EC%A0%95%EB%B3%B8)-%EC%9D%B4%EB%AF%B8%EC%A7%80-8.jpg?type=w966",
    ],
}

D = [
    dict(slug="holder", num="01", title="제품 거치대 개별집기 디자인", cat="제품 · 일러스트",
         span="7", glyph="거치", grad="linear-gradient(150deg,#2b2f36,#14161a 62%,#0c0e10)",
         scope="제품 이미지 · 판매 구성", blog="223431974474", preview="assets/design/preview-holder.jpg",
         tagline="가전제품 거치대를 개별집기 형태로 구성한 제품 디자인.",
         desc="바디슬립, 포라·오므론, 인바디, 쥬베라 등 제품별 거치대와 구성품을 정리해 판매용 이미지로 만들었습니다. 제품마다 다른 형태를 같은 톤으로 묶는 데 시간을 썼습니다."),
    dict(slug="pop", num="02", title="홍보용 POP 디자인", cat="POP · 인쇄",
         span="5", glyph="POP", grad="linear-gradient(150deg,#c8452a,#7a1f14 65%,#3d0e08)",
         scope="매장 홍보물", blog="223431972432",
         tagline="매장에서 쓰는 홍보용 POP 디자인.",
         desc="고요잠, 바디프레임, 슬리피솔 등 제품의 POP를 여러 규격으로 작업했습니다. 매장에서 멀리서도 읽히도록 제품명과 핵심 문구의 크기를 우선했습니다."),
    dict(slug="backpanel", num="03", title="제품 홍보용 백판 디자인", cat="인쇄 · 패키지",
         span="4", glyph="백판", grad="linear-gradient(150deg,#6f6759,#4a453c 60%,#262420)",
         scope="인쇄물", blog="223431970086", preview="assets/design/preview-backpanel.jpg",
         tagline="제품 홍보용 백판(인쇄물) 디자인.",
         desc="보다나, 요이치, 의료기기, 수면가전 등 제품의 백판을 작업했습니다. 인쇄 결과를 확인하며 색과 여백을 조정했습니다."),
    dict(slug="11st", num="04", title="11번가 프로모션 상세페이지", cat="상세페이지",
         span="4", glyph="11", grad="linear-gradient(150deg,#ff2d55,#b30026 58%,#4a0011)",
         scope="상세페이지 · 캐릭터", blog="223431945888",
         tagline="코딩로봇 ‘씽고’의 11번가 프로모션 상세페이지.",
         desc="어린이날 이벤트 페이지와 카드뷰, 캐릭터 디자인을 함께 작업했습니다. 프로모션 기간에 맞춰 짧은 호흡으로 여러 버전을 만들었습니다."),
    dict(slug="circulator", num="05", title="하이메이드 에어서큘레이터 상세페이지", cat="상세페이지",
         span="4", glyph="에어", grad="linear-gradient(150deg,#7fa8c9,#4a7396 58%,#23384d)",
         scope="상세페이지", blog="223431942100",
         tagline="하이메이드 에어서큘레이터 상세페이지.",
         desc="제품의 기능과 사용 장면을 한 장의 긴 이미지로 구성했습니다. 스크롤에 따라 자연스럽게 읽히도록 섹션 간격을 맞췄습니다."),
    dict(slug="induction", num="06", title="하이메이드 1구 인덕션 상세페이지", cat="상세페이지",
         span="5", glyph="인덕", grad="linear-gradient(150deg,#3a3f45,#22262b 58%,#0f1114)",
         scope="상세페이지", blog="223431941500",
         tagline="하이메이드 1구 인덕션 상세페이지.",
         desc="제품 컷과 기능 설명을 중심으로 구성했습니다. 작은 주방에서도 부담 없는 크기라는 점을 이미지로 먼저 보여주려 했습니다."),
    dict(slug="report", num="07", title="해피핀핀 — 결과보고서", cat="프로젝트 기록",
         span="7", glyph="보고", grad="linear-gradient(150deg,#2a3550,#161d2e 60%,#0b0f18)",
         scope="웹개발 프로젝트", blog="223431866873",
         tagline="이커머스 웹개발 프로젝트 ‘해피핀핀’의 결과보고서.",
         desc="기획 의도와 화면 설계, 구현 결과를 한 문서로 정리한 결과보고서입니다. 프로젝트를 마무리하며 무엇을 만들었고 무엇이 아쉬웠는지 기록으로 남겼습니다."),
]

NAV = """  <header class="nav" id="nav">
    <a class="nav__brand" href="../index.html">이규영<span>Portfolio</span></a>
    <nav class="nav__links" aria-label="주요 메뉴">
      <a href="../index.html#work">Work</a>
      <a href="../index.html#design">Design</a>
      <a href="../index.html#about">About</a>
      <a href="../resume.html">Resume</a>
      <a href="../index.html#contact">Contact</a>
    </nav>
    <a class="nav__cta" href="mailto:wlsduf631@gmail.com">wlsduf631@gmail.com</a>
    <button class="nav__burger" type="button" aria-label="메뉴 열기" aria-expanded="false" aria-controls="navpanel">
      <span></span><span></span><span></span>
    </button>
    <div class="nav__panel" id="navpanel">
      <a href="../index.html#work">Work <span>01</span></a>
      <a href="../index.html#design">Design <span>02</span></a>
      <a href="../index.html#about">About <span>03</span></a>
      <a href="../resume.html">Resume <span>04</span></a>
      <a href="../index.html#contact">Contact <span>05</span></a>
    </div>
  </header>"""


def card(p):
    imgs = IMG[p["slug"]]
    return f"""        <a class="dcard dcard--{p['span']}" href="design/{p['slug']}.html" data-reveal>
          <span class="dcard__media">
            <img class="dcard__img" src="{p.get("preview") or imgs[0]}" alt="{p['title']}" loading="lazy" />
            <span class="dcard__cover" style="background:{p['grad']}">
              <span class="idx">{p['num']} / {p['cat']}</span>
              <span class="glyph">{p['glyph']}</span>
              <span class="kicker">{p['scope']}</span>
            </span>
          </span>
          <span class="dcard__meta">
            <span>
              <span class="dcard__title">{p['title']}</span>
              <span class="dcard__link">작업 보기 →</span>
            </span>
            <span class="dcard__cat">2024</span>
          </span>
        </a>"""


def page(p, nxt):
    imgs = IMG[p["slug"]]
    figures = "\n".join(
        f"""          <figure class="dfig">
            <img src="{u}" alt="{p['title']} 이미지 {i}" loading="lazy" />
            <figcaption><span>{i:02d}</span><span>{len(imgs):02d}</span></figcaption>
          </figure>"""
        for i, u in enumerate(imgs, 1)
    )
    return f"""<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1" />
<title>{p['title']} — 이규영</title>
<meta name="description" content="{p['tagline']}" />
<meta property="og:title" content="{p['title']} — 이규영" />
<meta property="og:description" content="{p['tagline']}" />
<meta name="theme-color" content="#f3eee6" />
<meta property="og:image" content="../assets/og.jpg" />
<meta property="og:image:width" content="1200" />
<meta property="og:image:height" content="630" />
<meta name="twitter:card" content="summary_large_image" />
<link rel="icon" href="../assets/favicon.svg" type="image/svg+xml" />
<link rel="preconnect" href="https://cdn.jsdelivr.net" />
<link rel="preconnect" href="https://postfiles.pstatic.net" />
<link rel="stylesheet" href="../assets/css/style.css" />
<noscript><style>[data-reveal]{{opacity:1!important;transform:none!important}}</style></noscript>
</head>
<body class="paper">
<a class="skip" href="#main">본문으로 건너뛰기</a>
<div class="grain" aria-hidden="true"></div>

{NAV}

<main id="main">
  <article>
    <section class="phero">
      <div class="phero__glow" style="background:{p['grad']}" aria-hidden="true"></div>
      <div class="wrap">
        <div class="phero__top">
          <nav class="crumbs" aria-label="위치">
            <a href="../index.html">Index</a><span>/</span>
            <a href="../index.html#design">Design</a><span>/</span>
            <span>{p['title']}</span>
          </nav>
          <span class="phero__num">Design {p['num']} / {len(D):02d}</span>
        </div>

        <h1 class="phero__title{' phero__title--sm' if len(p['title']) > 12 else ''}">{p['title']}</h1>
        <p class="phero__tagline">{p['tagline']}</p>

        <dl class="pmeta">
          <div><dt>Year</dt><dd>2024</dd></div>
          <div><dt>Category</dt><dd>{p['cat']}</dd></div>
          <div><dt>Scope</dt><dd>{p['scope']}</dd></div>
          <div><dt>Images</dt><dd>{len(imgs)}장</dd></div>
        </dl>
      </div>
    </section>

    <section class="pbody">
      <div class="wrap">
        <div class="pbody__grid">
          <aside class="pbody__aside">
            <p class="mono">About this work</p>
            <h2>{p['title']}</h2>
            <a class="plink" href="{BLOG}{p['blog']}" target="_blank" rel="noopener">원본 글 보기 ↗</a>
          </aside>
          <div class="pbody__main">
            <p>{p['desc']}</p>
            <div class="dgallery">
{figures}
            </div>
          </div>
        </div>
      </div>
    </section>

    <nav class="pnext" aria-label="다음 작업">
      <div class="wrap">
        <a href="{nxt['slug']}.html">
          <div>
            <span class="mono">Next work — {nxt['num']} / {len(D):02d}</span>
            <h3>{nxt['title']}</h3>
          </div>
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.2"><path d="M5 12h14M13 6l6 6-6 6"/></svg>
        </a>
      </div>
    </nav>
  </article>
</main>

<footer class="footer wrap" style="margin-top:0;padding:26px var(--pad) 34px">
  <span>© 2026 이규영</span>
  <a href="mailto:wlsduf631@gmail.com">wlsduf631@gmail.com</a>
  <a href="../index.html#design">Back to design ↑</a>
</footer>

<script src="../assets/js/main.js" defer></script>
</body>
</html>
"""


def main():
    os.makedirs(OUT, exist_ok=True)
    for i, p in enumerate(D):
        nxt = D[(i + 1) % len(D)]
        with open(os.path.join(OUT, p["slug"] + ".html"), "w", encoding="utf-8") as f:
            f.write(page(p, nxt))
        print("wrote design/" + p["slug"] + ".html")

    idx = os.path.join(ROOT, "index.html")
    s = open(idx, encoding="utf-8").read()
    cards = "\n".join(card(p) for p in D)
    new, n = re.subn(
        r"(<!-- DESIGN_CARDS_START -->)(.*?)(<!-- DESIGN_CARDS_END -->)",
        lambda m: m.group(1) + "\n" + cards + "\n        " + m.group(3),
        s,
        flags=re.S,
    )
    if n != 1:
        raise SystemExit("DESIGN_CARDS markers not found in index.html")
    open(idx, "w", encoding="utf-8").write(new)
    print("updated index.html cards:", len(D))


if __name__ == "__main__":
    main()
