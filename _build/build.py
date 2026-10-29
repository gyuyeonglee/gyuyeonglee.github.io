# -*- coding: utf-8 -*-
"""
포트폴리오 상세 페이지 생성기
사용: python _build/build.py
결과: work/<id>.html  (정적 HTML, 생성 후 직접 수정해도 됩니다)
"""
import os
import html

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "work")

P = [
    dict(
        id="safe-timer", num="01", title="세이프 타이머", en="Safe Timer",
        label="Desktop App · Python",
        tagline="60초, 그 한 순간을 위한 오버레이 타이머.",
        platform="Windows 데스크톱", stack="Python · Tkinter",
        status="직접 사용 중", shot="safe-timer.png", window="세이프 타이머",
        grad="radial-gradient(120% 120% at 20% 0%, #5a1818, #121212 70%)",
        icon="safe-timer.png", glyph="60",
        aside="게임 화면 위,\n60초.",
        intro=[
            "게임 ‘데드바이 데이라이트’에는 60초 동안 지속되는 생존자 스킬이 있습니다. 그 시간 안에 생존자를 들어 올리면 역으로 큰 위기를 맞기 때문에, 언제까지 기다려야 하는지가 중요합니다.",
            "세이프 타이머는 이 60초를 재는 오버레이 타이머입니다. 게임 창 위에 항상 떠 있고, Z키 하나로 시작하고 멈춥니다. 창을 숨기면 트레이 아이콘으로만 남아 플레이를 방해하지 않습니다.",
        ],
        features=[
            "60초 카운트다운, 15초 이하부터 위험 색상(#990000)으로 전환",
            "Z키 전역 감지 — 게임 중에도 시작·정지, 키 입력은 가로채지 않음",
            "Z키 기능 ON/OFF 버튼과 트레이 메뉴 연동",
            "창 숨김 → 트레이 아이콘, 필요할 때만 꺼내 쓰는 구조",
            "드래그로 옮긴 위치 저장, 모니터를 바꿔도 화면 밖으로 나가지 않음",
            "종료 시 ‘SAFE!’ 표시와 비프음 3회",
        ],
        notes=[
            "GetAsyncKeyState를 20ms 간격으로 폴링해, 게임 클라이언트의 입력을 빼앗지 않으면서 전역 키를 감지했습니다.",
            "CreateMutexW로 중복 실행을 막고, GetSystemMetrics(76~79)로 가상 화면 영역을 확인해 창 위치를 복원합니다.",
            "PyInstaller로 콘솔 창 없는 실행 파일을 만들고, 설정은 %APPDATA%에 JSON으로 저장했습니다.",
        ],
        tech=["Python", "Tkinter", "pystray", "Pillow", "ctypes", "winsound", "PyInstaller"],
        palette=["#121212", "#1A1A1A", "#5A1818", "#990000", "#19381F"],
        link=None,
    ),
    dict(
        id="my-memo", num="02", title="나만의 메모", en="My Memo",
        label="Desktop App · PySide6",
        tagline="메모 한 줄이 곧 미션, 체크하면 사라지는 포스트잇.",
        platform="Windows 데스크톱", stack="Python · PySide6",
        status="직접 사용 중", shot=None, window="나만의 메모",
        grad="linear-gradient(140deg, #ffe0b8, #ffd6e0 46%, #d4ecff)",
        icon="my-memo.png", glyph="메모", ink="dark",
        aside="한 줄이\n미션이 됩니다.",
        intro=[
            "메모 하나가 창 하나인 데스크톱 포스트잇입니다. 할 일을 적어 두고 끝난 줄을 체크하면, 그 줄은 ‘해결한 미션’ 창으로 옮겨집니다. 지운 것이 아니라 옮긴 것이라 필요하면 원래 자리로 되돌릴 수 있습니다.",
            "메모지 일곱 색과 여덟 가지 글자색, 항상 위 고정, 글자 크기와 정렬을 지원합니다. 내용과 서식, 창 위치와 크기는 입력이 멈추면 자동으로 저장됩니다.",
        ],
        features=[
            "메모마다 독립된 창, 겹치지 않게 자동 배치",
            "줄 단위 미션 토글 — Ctrl+M · 🎯 버튼 · 우클릭",
            "해결한 미션 되돌리기 · 선택 삭제 · 전체 삭제",
            "메모지 7색 · 항상 위 고정 · 굵게 · 크기 · 정렬 · 글자색 8종",
            "내용·서식(HTML)·위치·크기를 400ms 디바운스로 자동 저장",
            "중복 실행 시 기존 메모를 앞으로 불러오고 깜빡임",
        ],
        notes=[
            "체크박스를 별도 위젯 없이 거터에 직접 그려, 줄 높이와 어긋나지 않게 맞췄습니다.",
            "줄 상태를 blockFormat 사용자 속성에 보관해, 복사·붙여넣기 후에도 그대로 유지됩니다.",
            "한글 IME 조합 중 플레이스홀더 잔상이 남는 문제를 inputMethodEvent 처리로 해결했습니다.",
        ],
        tech=["Python", "PySide6", "QTextEdit", "QLocalServer", "ctypes", "PyInstaller"],
        palette=["#FFF4A3", "#FFD6E0", "#D4ECFF", "#D8F5C9", "#E6D9FF"],
        link=None,
    ),
    dict(
        id="mini-cloud", num="03", title="MiniCloud", en="미니 클라우드",
        label="Desktop App · PySide6",
        tagline="파일을 끌어다 놓으면 바로 열리는, 화면 위 미니 프리뷰.",
        platform="Windows 데스크톱", stack="Python · PySide6 · SQLite",
        status="직접 사용 중", shot=None, window="MiniCloud",
        grad="linear-gradient(140deg, #e8f2ff, #c9dcff 50%, #9fc0ff)",
        icon="mini-cloud.png", glyph="MC", ink="dark",
        aside="끌어다 놓으면\n열립니다.",
        intro=[
            "바탕화면 한쪽에 띄워 두는 미리보기 창입니다. 레퍼런스 파일을 끌어다 놓고 폴더로 묶어 두면, 클릭 한 번으로 이미지·PDF·문서·오디오·영상을 확인할 수 있습니다.",
            "원본 파일은 건드리지 않습니다. 목록에서 빼도 파일은 그대로 남고, 창 크기와 위치, 볼륨, 마지막으로 보던 폴더까지 다음 실행에 복원됩니다.",
        ],
        features=[
            "드래그앤드롭 등록, 폴더 생성·순서 변경·즐겨찾기",
            "형식별 뷰어 자동 분기 — 이미지·GIF·PDF·DOCX·텍스트·오디오·영상",
            "PDF 최대 20페이지 렌더링, Ctrl+휠 확대",
            "오디오·영상 재생과 시크바·볼륨",
            "별칭 지정, 목록에서만 제거해 원본 파일은 그대로",
            "창 크기·위치·볼륨·마지막 폴더 복원",
        ],
        notes=[
            "미리보기 로딩을 QThread로 분리하고 취소 플래그를 두어, 큰 PDF를 열어도 UI가 멈추지 않습니다.",
            "SmoothPixmapTransform과 AnchorUnderMouse를 써서 확대해도 픽셀이 뭉개지지 않습니다.",
            "SQLite 스키마를 스스로 마이그레이션해, 업데이트 후에도 기존 목록이 유지됩니다.",
        ],
        tech=["Python", "PySide6", "PyMuPDF", "python-docx", "SQLite", "PyInstaller"],
        palette=["#FFFFFF", "#F0F0F0", "#E0F0FF", "#2B2B2B"],
        link=None,
    ),
    dict(
        id="compact-vault", num="04", title="Compact Vault", en="비밀번호 보관함",
        label="Desktop App · Security",
        tagline="마스터 비밀번호 하나로, 계정은 AES-256으로 로컬에만.",
        platform="Windows 데스크톱", stack="Python · PySide6 · Cryptography",
        status="직접 사용 중", shot="compact-vault.png", window="Compact Vault — 비밀번호 보관함",
        grad="linear-gradient(140deg, #3157d5, #172033)",
        icon=None, glyph="CV",
        aside="서버 없이,\n내 PC에만.",
        intro=[
            "계정을 암호화된 파일 하나에 보관하는 오프라인 비밀번호 관리자입니다. 서버도 클라우드도 없이 내 PC 안에서만 동작하고, 마스터 비밀번호를 모르면 파일을 열 수 없습니다.",
            "5분 동안 쓰지 않으면 자동으로 잠기고 키를 폐기합니다. 아이디나 비밀번호를 복사하면 20초 뒤 클립보드에서 지워, 화면과 클립보드에 남는 시간을 모두 줄였습니다.",
        ],
        features=[
            "Argon2id + AES-256-GCM, 단일 .enc 파일",
            "마스터 비밀번호 12자 이상, 변경 시 새 salt로 재암호화",
            "5분 미사용 자동 잠금과 키 폐기",
            "복사 후 20초 뒤 클립보드 자동 삭제",
            "검색, 순서 변경",
            "암호화 백업(.cvault) 내보내기 · 복원",
        ],
        notes=[
            "파일 헤더에 KDF 파라미터·salt·nonce를 기록하고, AAD로 헤더를 암호문에 묶어 변조를 막았습니다.",
            "임시 파일에 쓴 뒤 fsync와 os.replace로 교체해, 저장 중 전원이 꺼져도 원본이 남습니다.",
            "비밀번호 생성기는 문자 종류별 최소 1자를 보장한 뒤 SystemRandom으로 섞습니다.",
        ],
        tech=["Python", "PySide6", "cryptography", "argon2-cffi", "PyInstaller"],
        palette=["#F4F6FA", "#172033", "#3157D5", "#D0D5DD"],
        link=None,
    ),
    dict(
        id="audio-switcher", num="05", title="Audio Switcher", en="오디오 스위처",
        label="Desktop App · Windows",
        tagline="스피커와 헤드셋, 단축키 한 번으로.",
        platform="Windows 데스크톱", stack="Python · PySide6 · COM",
        status="직접 사용 중", shot=None, window="Audio Switcher",
        grad="linear-gradient(140deg, #1f6b35, #121212 72%)",
        icon="audio-switcher.png", glyph="AU",
        aside="듣는 곳을\n바꿉니다.",
        intro=[
            "출력 장치 두 개를 등록해 두고 버튼·전역 단축키·트레이 클릭으로 즉시 바꿉니다. 기본 장치뿐 아니라 통신 장치까지 함께 전환해서, 화상회의와 게임을 오갈 때 설정 창을 열 필요가 없습니다.",
            "Windows 시작 시 자동 실행되고 평소에는 트레이에 숨어 있습니다. 전환할 때는 자체 토스트로 알려 주며, 이 알림은 방해 금지 모드의 영향을 받지 않습니다.",
        ],
        features=[
            "A↔B 원클릭 전환",
            "Ctrl·Alt·Shift·Win 조합 단축키 — A~Z, 0~9, F1~F12",
            "트레이 아이콘 좌클릭으로 즉시 전환",
            "Windows 시작 시 자동 실행",
            "자체 토스트 알림, 방해 금지 모드와 무관",
            "설정 JSON 저장, 시작 시 트레이로 숨김",
        ],
        notes=[
            "공개되지 않은 IPolicyConfig 인터페이스를 vtable 순서까지 선언해, 콘솔·멀티미디어·통신 세 역할을 동시에 바꿉니다.",
            "전환 후 실제 기본 장치를 다시 조회해 적용 여부를 검증합니다.",
            "WM_HOTKEY를 Qt 네이티브 이벤트 필터로 처리하고 MOD_NOREPEAT로 키 반복을 막았습니다.",
        ],
        tech=["Python", "PySide6", "pycaw", "comtypes", "winreg", "PyInstaller"],
        palette=["#2E7D32", "#1E1E1E", "#FFFFFF"],
        link=None,
    ),
    dict(
        id="lecture-timer", num="06", title="강의 배속 타이머", en="Lecture Timer",
        label="Desktop App · Python",
        tagline="2배속 강의가 끝나는 시각을 미리 알려주는 타이머.",
        platform="Windows 데스크톱", stack="Python · Tkinter",
        status="직접 사용 중", shot="lecture-timer.png", window="강의 배속 타이머",
        grad="linear-gradient(140deg, #1f3a5a, #0f1216 72%)",
        icon="lecture-timer.png", glyph="2.0",
        aside="끝나는 시각을\n미리 압니다.",
        intro=[
            "강의 총 재생시간과 배속을 입력하면 실제로 기다려야 하는 시간을 계산해 카운트다운합니다. 남은 시간과 함께 알람이 울릴 시각을 보여 주기 때문에 다음 일정을 잡기 쉽습니다.",
            "Enter로 시작하고 멈추며, 알람이 울리면 창이 최전면으로 올라옵니다. 알람 10초 뒤에는 자동으로 종료됩니다.",
        ],
        features=[
            "시·분·초 + 1.0~3.0배속 입력",
            "길이÷배속 자동 계산",
            "남은 시간과 알람 예정 시각 동시 표시",
            "Enter로 시작·정지, 알람 10초 후 자동 종료",
            "알람 시 창을 최전면으로 호출",
            "창 위치 저장·복원",
        ],
        notes=[
            "time.monotonic을 기준으로 계산해, 배속 재생 중에도 오차가 누적되지 않습니다.",
            "CreateMutexW와 FindWindowW로 중복 실행을 감지하고, 이미 켜져 있으면 기존 창만 앞으로 불러옵니다.",
            "숫자 입력을 세 자리로 제한하고, 포커스가 오면 전체 선택해 바로 덮어쓸 수 있게 했습니다.",
        ],
        tech=["Python", "Tkinter", "threading", "winsound", "ctypes", "PyInstaller"],
        palette=["#1E1E1E", "#1F3A5A", "#1F4D2B", "#E8E8E8"],
        link=None,
    ),
    dict(
        id="dream-tarot", num="07", title="드림타로", en="Dream Tarot",
        label="Web App · Firebase",
        tagline="78장 라이더-웨이트로 오늘의 흐름을 읽는 타로.",
        platform="웹 · Android (Capacitor)", stack="JavaScript · Firebase",
        status="웹 · Android 빌드", shot=None, window="드림타로",
        grad="linear-gradient(140deg, #c76a9e, #9a7fc9 52%, #f7b8d3)",
        icon=None, glyph="타로",
        aside="열세 가지\n스프레드.",
        intro=[
            "일일·주간·월간·연간부터 연애, 켈틱크로스, 예/아니오까지 열세 가지 스프레드를 제공하는 타로 웹앱입니다. 카드를 섞고 딜링하는 과정을 3D 연출로 구현해, 웹에서도 뽑는 느낌을 살렸습니다.",
            "카드마다 수트와 키워드, 분야별 해석을 데이터로 두고 뽑힌 카드 조합으로 문장을 만듭니다. 78장 도감과 지난 운세, AI 심층 리딩도 같은 앱 안에 들어 있습니다.",
        ],
        features=[
            "13종 스프레드(무료 4 + 프리미엄 9), 78장 카드 DB",
            "카드 섞기·딜링·3D 플립 연출",
            "분야 칩(전체·사랑·일·돈·건강)에 따라 해석 분기",
            "78장 도감 필터·검색과 카드별 상세 해설",
            "생년월일 수비학으로 보는 ‘나의 성향 카드’",
            "AI 심층 리딩, 결과 이미지 공유, 지난 운세 30개",
        ],
        notes=[
            "카드 키워드·수트·분야를 조합해 문장을 만드는 서사 엔진을 직접 구현했습니다.",
            "Firestore 보안 규칙으로 사용량·채팅방·문의를 본인과 상담사로 제한했습니다.",
            "무료 1일 1회·프리미엄 1일 30회 한도를 localStorage와 Firestore에서 이중으로 검증합니다.",
        ],
        tech=["HTML", "CSS", "JavaScript", "Firebase Auth", "Firestore", "DeepSeek API", "Capacitor", "PWA"],
        palette=["#FDF3F9", "#C76A9E", "#9A7FC9", "#F7B8D3", "#5A4A6E"],
        link="https://tarot-fortune-5a6d3.web.app",
    ),
    dict(
        id="calorie-dict", num="08", title="칼로리 사전", en="Calorie Dict",
        label="Web App · Vanilla JS",
        tagline="이름만 치면 칼로리와 탄단지가 바로, 332가지 음식 사전.",
        platform="웹 (모바일 우선)", stack="HTML · CSS · JavaScript",
        status="운영 중", shot=None, window="칼로리 사전",
        grad="linear-gradient(140deg, #0e1116, #14311f 55%, #4ade80)",
        icon=None, glyph="칼",
        aside="332가지 음식,\n초성으로.",
        intro=[
            "식품 이름을 입력하면 100g 기준 칼로리와 탄수화물·단백질·지방을 즉시 보여 주는 식단 사전입니다. 332가지 음식을 17개 분류로 나눠 담았습니다.",
            "초성만 쳐도 찾습니다. ‘ㄷㅂ’으로 ‘된장찌개’를, ‘찌게’처럼 자주 틀리는 표기도 보정합니다. 오늘 먹은 양을 제공량 단위로 환산해 기록할 수 있습니다.",
        ],
        features=[
            "332개 음식 · 17개 분류",
            "초성(ㄷㅂ)·자모·부분 일치·띄어쓰기 무시 검색",
            "동의어·오타 보정 14종 (찌게→찌개, 달걀→계란)",
            "제공량 선택 시 자동 환산, 탄단지 열량 비율 바",
            "알코올·식이섬유 음식의 열량 차이 안내",
            "오늘 기록(날짜가 바뀌면 자동 리셋), 내 음식 추가",
        ],
        notes=[
            "빌드 도구 없이 index.html 한 파일로 구현해, 어디서든 열고 고칠 수 있게 했습니다.",
            "한글 유니코드 분해(0xAC00)로 초성·자모 검색을 라이브러리 없이 직접 구현했습니다.",
            "서버 없이 localStorage에 저장하고 Firebase Hosting으로 배포했습니다.",
        ],
        tech=["HTML", "CSS", "JavaScript", "localStorage", "Firebase Hosting"],
        palette=["#0E1116", "#161B22", "#4ADE80", "#38BDF8", "#A78BFA"],
        link="https://calorie-dict.web.app",
    ),
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


def cover(p):
    if p["shot"]:
        return f"""        <div class="pcover__window">
          <div class="pcover__bar"><i></i><i></i><i></i><span>{p['window']}</span></div>
          <img src="../assets/shots/{p['shot']}" alt="{p['title']} 실행 화면" />
        </div>"""
    icon = (
        f'<img src="../assets/icons/{p["icon"]}" width="56" height="56" alt="" style="margin-bottom:18px" />'
        if p["icon"] else ""
    )
    return f"""        <div class="pcover__poster{' is-dark' if p.get('ink') == 'dark' else ''}">
          <div class="top"><span>{p['label']}</span><span>{p['num']} / 08</span></div>
          <div class="bottom">
            {icon}
            <strong>{p['title']}</strong>
            <p>{p['tagline']}</p>
          </div>
          <span class="glyph" aria-hidden="true">{p['glyph']}</span>
        </div>"""


def build_one(p, nxt):
    feats = "\n".join(
        f'            <li><b>{i:02d}</b><span>{html.escape(f)}</span></li>'
        for i, f in enumerate(p["features"], 1)
    )
    notes = "\n".join(
        f'            <li><span>{i:02d}</span><p>{html.escape(n)}</p></li>'
        for i, n in enumerate(p["notes"], 1)
    )
    techs = "\n".join(f"            <li>{html.escape(t)}</li>" for t in p["tech"])
    swatches = "\n".join(
        f'            <span style="background:{c}" data-hex="{c}"></span>' for c in p["palette"]
    )
    paras = "\n".join(f"          <p>{html.escape(t)}</p>" for t in p["intro"])
    aside = p["aside"].replace("\n", "<br />")

    link_block = ""
    if p["link"]:
        link_block = f"""
          <a class="plink" href="{p['link']}" target="_blank" rel="noopener">사이트 열기 ↗</a>"""

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
<meta property="og:image" content="https://gyuyeonglee.github.io/assets/og.jpg" />
<meta property="og:image:width" content="1200" />
<meta property="og:image:height" content="630" />
<meta name="twitter:card" content="summary_large_image" />
<link rel="icon" href="../assets/favicon.svg" type="image/svg+xml" />
<link rel="preconnect" href="https://cdn.jsdelivr.net" />
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
            <a href="../index.html#work">Work</a><span>/</span>
            <span>{p['title']}</span>
          </nav>
          <span class="phero__num">{p['num']} / 08</span>
        </div>

        <h1 class="phero__title">{p['title']}</h1>
        <p class="phero__tagline">{p['tagline']}</p>

        <dl class="pmeta">
          <div><dt>Role</dt><dd>기획 · 디자인 · 개발<br />(1인 작업)</dd></div>
          <div><dt>Platform</dt><dd>{p['platform']}</dd></div>
          <div><dt>Stack</dt><dd>{p['stack']}</dd></div>
          <div><dt>Status</dt><dd>{p['status']}</dd></div>
        </dl>

        <div class="pcover" style="--cover-grad:{p['grad']}" data-cover>
{cover(p)}
        </div>
      </div>
    </section>

    <section class="pbody">
      <div class="wrap">
        <div class="pbody__grid">
          <aside class="pbody__aside">
            <p class="mono">Overview</p>
            <h2>{aside}</h2>
            <a class="plink" href="../index.html#work">Work index ↗</a>
          </aside>

          <div class="pbody__main">
{paras}
{link_block}

            <div class="pblock">
              <div class="pblock__head">
                <h3>주요 기능</h3>
                <span class="mono">Features</span>
              </div>
              <ul class="feat">
{feats}
              </ul>
            </div>

            <div class="pblock">
              <div class="pblock__head">
                <h3>기술 노트</h3>
                <span class="mono">Engineering</span>
              </div>
              <ul class="notes">
{notes}
              </ul>
            </div>

            <div class="pblock">
              <div class="pblock__head">
                <h3>사용 기술</h3>
                <span class="mono">Stack</span>
              </div>
              <ul class="techlist">
{techs}
              </ul>
            </div>

            <div class="pblock">
              <div class="pblock__head">
                <h3>컬러</h3>
                <span class="mono">Palette</span>
              </div>
              <div class="palette">
{swatches}
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <nav class="pnext" aria-label="다음 프로젝트">
      <div class="wrap">
        <a href="{nxt['id']}.html">
          <div>
            <span class="mono">Next project — {nxt['num']} / 08</span>
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
  <a href="../index.html">Back to index ↑</a>
</footer>

<script src="../assets/js/main.js" defer></script>
</body>
</html>
"""


def main():
    os.makedirs(OUT, exist_ok=True)
    for i, p in enumerate(P):
        nxt = P[(i + 1) % len(P)]
        path = os.path.join(OUT, p["id"] + ".html")
        with open(path, "w", encoding="utf-8") as f:
            f.write(build_one(p, nxt))
        print("wrote", os.path.relpath(path, ROOT))


if __name__ == "__main__":
    main()
