# 이규영 — 포트폴리오

웹디자이너 이규영의 개인 포트폴리오. **빌드 도구 없이** HTML/CSS/JS만으로 동작하는 정적 사이트입니다.
외주 홍보용이 아니라, 작업을 보여주는 **명함**에 가깝게 구성했습니다.

- 메인: `index.html` (원페이지)
- 앱 프로젝트: `work/*.html` (8개)
- 디자인 작업: `design/*.html` (7개, 원본 이미지 갤러리)
- 스타일: `assets/css/style.css`
- 스크립트: `assets/js/main.js`

---

## 1. 미리 보기

`preview.bat` 을 더블클릭하면 로컬 서버(8080)가 열리고 브라우저에서 사이트가 뜹니다.
직접 실행하려면:

```bat
python -m http.server 8080 --directory .
```

> `index.html` 을 파일 탐색기에서 바로 열어도 되지만, 상대경로 문제를 피하려면
> 위처럼 서버로 여는 것을 권장합니다.

## 2. 구성

| 경로 | 설명 |
|---|---|
| `index.html` | 히어로 · 작업 8 · 디자인 아카이브 7 · 소개 · 명함 |
| `resume.html` | 이력서 (인쇄 / PDF 저장 버튼 포함) |
| `assets/docs/resume-2024.pdf` | 2024년 원본 이력서 PDF |
| `work/safe-timer.html` | 세이프 타이머 |
| `work/my-memo.html` | 나만의 메모 |
| `work/mini-cloud.html` | MiniCloud |
| `work/compact-vault.html` | Compact Vault |
| `work/audio-switcher.html` | Audio Switcher |
| `work/lecture-timer.html` | 강의 배속 타이머 |
| `work/dream-tarot.html` | 드림타로 |
| `work/calorie-dict.html` | 칼로리 사전 |
| `design/holder.html` | 제품 거치대 개별집기 디자인 |
| `design/pop.html` | 홍보용 POP 디자인 |
| `design/backpanel.html` | 제품 홍보용 백판 디자인 |
| `design/11st.html` | 11번가 프로모션 상세페이지 |
| `design/circulator.html` | 하이메이드 에어서큘레이터 상세페이지 |
| `design/induction.html` | 하이메이드 1구 인덕션 상세페이지 |
| `design/report.html` | 해피핀핀 — 결과보고서 |
| `assets/img/profile.jpg` | 프로필 사진 (900px) · `profile-avatar.jpg` (160px) |
| `assets/design/` | 디자인 작업 원본 이미지 37장 (로컬 저장) |
| `assets/shots/` | 실제 앱 실행 화면 3종 |
| `assets/icons/` | 앱 아이콘 (256px PNG) |
| `_build/build.py` | 앱 상세 페이지 생성기 |
| `_build/design.py` | 디자인 갤러리 + 메인 카드 생성기 |
| `_build/localize_images.py` | 블로그 이미지 내려받기 + 경로 로컬화 |

## 3. 디자인 작업 이미지에 대해

블로그 원본 37장을 내려받아 `assets/design/` 에 저장했고, 모든 페이지가 로컬 이미지를
참조합니다. 네이버 상태와 무관하게 이미지가 표시됩니다.

- 다시 원격 주소로 되돌리려면: `python _build\design.py`
- 원격 상태에서 다시 내려받으려면: `python _build\localize_images.py` (인터넷 필요)

> 7번째 작업 '해피핀핀 결과보고서'는 블로그 원본에서 5번째 이미지가 삭제되어 7장만 수록했습니다.

## 4. 내용 수정하기

### 문구·링크
`index.html` 과 각 페이지를 직접 고치면 됩니다. 생성된 페이지도 손으로 수정할 수 있습니다.
(다시 생성하면 덮어씁니다.)

### 앱 프로젝트 추가/수정
`_build/build.py` 상단 `P` 리스트를 고친 뒤:

```bat
python _build\build.py
```

### 디자인 작업 추가/수정
`_build/design.py` 상단 `D`(내용)와 `IMG`(이미지 주소)를 고친 뒤:

```bat
python _build\design.py
```

메인 페이지의 디자인 카드 목록은 `index.html` 의
`<!-- DESIGN_CARDS_START -->` 와 `<!-- DESIGN_CARDS_END -->` 사이가 자동으로 갱신됩니다.

## 5. 배포 (GitHub Pages)

이 사이트는 **https://gyuyeonglee.github.io** 기준으로 OG 이미지 주소까지 맞춰져 있습니다.

1. GitHub에서 `gyuyeonglee.github.io` 저장소 생성 (Public, README 추가 없이)
2. `portfolio/` 폴더에서 아래 실행
   ```bash
   git init
   git add .
   git commit -m "Portfolio site"
   git branch -M main
   git remote add origin https://github.com/gyuyeonglee/gyuyeonglee.github.io.git
   git push -u origin main
   ```
3. 저장소 Settings → Pages → Source: `Deploy from a branch`, Branch `main` / `(root)` → Save
4. 1분 뒤 https://gyuyeonglee.github.io 접속

> 다른 이름의 저장소에 올리면 주소가 `https://아이디.github.io/저장소/`가 됩니다.
> 그때는 각 페이지의 `og:image`와 이 문서의 URL을 그 주소로 바꿔주세요.
>
> Netlify는 계정 크레딧이 소진되면 배포가 차단됩니다(실제로 이 계정에서 확인됨).
> Vercel·Firebase Hosting도 같은 폴더를 그대로 올릴 수 있습니다.

## 6. 참고

- 폰트: Pretendard(CDN), Instrument Serif · IBM Plex Mono(Google Fonts) — 인터넷 필요.
- **종이 테마**: 전체가 따뜻한 종이색(`:root`의 `--bg: #f3eee6`)이고, 검정은 명함 카드에만 씁니다.
  - 종이 색·글자색을 바꾸려면 `style.css` 상단 `:root` 값만 수정
  - 디자인 아카이브는 `.paper` 래퍼 + `Chapter 02` 오프너로 구획을 나눕니다
  - 상세 페이지도 `<body class="paper">` 로 같은 재질을 씁니다
- **공유 미리보기**: `assets/og.jpg` (1200×630). `og:image`가 상대경로라, 배포 후에는
  도메인을 붙여 절대 URL로 바꾸는 게 좋습니다 (카카오톡·페이스북은 절대 URL만 인식).
  예: `content="https://내도메인/assets/og.jpg"`
- 접근성: 키보드 포커스, 스킵 링크, `prefers-reduced-motion` 대응 포함.
