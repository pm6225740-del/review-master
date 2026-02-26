import streamlit as st
import streamlit.components.v1 as components
import yt_dlp
import os
import tempfile
import random

# === 1. 페이지 기본 설정 ===
st.set_page_config(page_title="SNS 미디어 허브", page_icon="🚀", layout="wide", initial_sidebar_state="collapsed")

# === 2. 고급 CSS 디자인 커스텀 ===
st.markdown("""
    <style>
    #MainMenu {visibility: hidden;}
    header {visibility: hidden;}
    footer {visibility: hidden;}
    .stDeployButton {display:none;}

    @import url('https://cdn.jsdelivr.net/gh/orioncactus/pretendard/dist/web/static/pretendard.css');
    html, body, [class*="css"] { font-family: 'Pretendard', sans-serif; }
    .main { background-color: #0b0e14; }
    
    .premium-banner {
        background: linear-gradient(135deg, #4A00E0 0%, #8E2DE2 100%);
        border-radius: 12px;
        padding: 25px 20px;
        text-align: center;
        color: white;
        font-weight: 800;
        font-size: 1.1rem;
        margin-bottom: 25px;
        box-shadow: 0 4px 15px rgba(142, 45, 226, 0.3);
    }
    
    .side-banner {
        background: #1a1d24;
        border: 1px solid #2d3139;
        border-radius: 10px;
        padding: 30px 10px;
        text-align: center;
        color: #a0aabf;
        margin-bottom: 15px;
        transition: all 0.3s ease;
    }
    .side-banner:hover {
        border-color: #8E2DE2;
        color: white;
        transform: translateY(-2px);
    }
    
    /* 랭킹 카드 디자인 */
    .ranking-card {
        background-color: #161922;
        border-left: 4px solid #8E2DE2;
        padding: 15px 20px;
        border-radius: 8px;
        margin-bottom: 10px;
    }
    </style>
""", unsafe_allow_html=True)

# === 3. 영상 임베드 함수 (실제 SNS 게시물 노출용) ===
# 트위터(X) 게시물을 웹사이트에 진짜로 띄워주는 기능입니다.
def embed_x_tweet(tweet_url):
    html_code = f"""
    <blockquote class="twitter-tweet" data-theme="dark">
    <a href="{tweet_url}"></a>
    </blockquote>
    <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>
    """
    components.html(html_code, height=450, scrolling=True)

# 인스타그램 게시물을 웹사이트에 띄워주는 기능입니다.
def embed_instagram(post_url):
    html_code = f"""
    <blockquote class="instagram-media" data-instgrm-permalink="{post_url}?utm_source=ig_embed" data-instgrm-version="14"></blockquote>
    <script async src="//www.instagram.com/embed.js"></script>
    """
    components.html(html_code, height=500, scrolling=True)

# === 4. 백엔드 로직 ===
def download_video(url):
    ydl_opts = {
        'format': 'best',
        'quiet': True,
        'no_warnings': True,
        'outtmpl': tempfile.gettempdir() + '/%(title)s.%(ext)s',
    }
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            file_path = ydl.prepare_filename(info)
            return file_path, info.get('title', 'video')
    except Exception as e:
        return None, str(e)

# 50개 랭킹 데이터 생성 함수
@st.cache_data
def generate_50_trends():
    trends = []
    # 데모를 위해 실제 존재하는 안전한 트윗/인스타 URL 구조를 사용합니다.
    # 추후 API를 연결하면 이 URL들이 실시간으로 교체됩니다.
    sample_x_url = "https://twitter.com/X/status/1801041697268801758"
    sample_ig_url = "https://www.instagram.com/p/C-vT-0_h"
    
    for i in range(1, 51):
        platform = "X (Twitter)" if i % 2 == 0 else "Instagram"
        trends.append({
            "rank": i,
            "platform": platform,
            "title": f"실시간 화제의 급상승 영상 {i}탄",
            "count": f"{random.randint(50, 999) / 10.0:.1f}k",
            "url": sample_x_url if platform == "X (Twitter)" else sample_ig_url
        })
    return trends

# === 5. 레이아웃 및 UI 구성 ===
left_ad, main_content, right_ad = st.columns([1.5, 7, 1.5])

# [좌측 광고] - 요청하신 대로 '광고문의'로 변경
with left_ad:
    st.markdown('<div class="side-banner">📢<br><br><b>광고문의</b><br>배너 등록<br>문의하기</div>', unsafe_allow_html=True)
    st.markdown('<div class="side-banner">🎯<br><br>스폰서 배너<br>영역</div>', unsafe_allow_html=True)

# [우측 광고]
with right_ad:
    st.markdown('<div class="side-banner">📺<br><br>구글 애드센스<br>광고 자리</div>', unsafe_allow_html=True)
    st.markdown('<div class="side-banner">🤝<br><br>제휴/입점 문의</div>', unsafe_allow_html=True)

# [중앙 메인 영역]
with main_content:
    st.markdown('<div class="premium-banner">🚀 고화질 SNS 영상 다운로더 & 실시간 트렌드 분석 허브</div>', unsafe_allow_html=True)
    
    tab_dl, tab_rank = st.tabs(["📥 초고속 다운로드", "🔥 실시간 인기 영상 리스트"])
    
    # --- 탭 1: 다운로드 ---
    with tab_dl:
        st.write("")
        url_input = st.text_input(
            "👇 다운로드할 링크(URL)를 아래에 붙여넣으세요.",
            placeholder="예: https://x.com/username/status/123456..."
        )
        
        if st.button("지금 추출하기", type="primary", use_container_width=True):
            if url_input:
                with st.spinner('서버에서 고화질 영상을 가져오고 있습니다...'):
                    file_path, title_or_error = download_video(url_input)
                    if file_path and os.path.exists(file_path):
                        st.success("🎉 성공적으로 추출했습니다!")
                        with open(file_path, "rb") as f:
                            st.download_button("💾 내 기기에 저장하기", data=f, file_name=os.path.basename(file_path), mime="video/mp4", use_container_width=True)
                    else:
                        st.error(f"❌ 다운로드에 실패했습니다. (상세 오류: {title_or_error})")
            else:
                st.warning("먼저 링크를 입력해주세요.")

    # --- 탭 2: 실시간 랭킹 (필터 및 리스트형 뷰) ---
    with tab_rank:
        st.write("")
        # 상단 플랫폼 선택 필터 추가
        selected_platform = st.radio("보기 옵션 선택:", ["🔥 전체보기", "🐦 X (Twitter)", "📸 Instagram"], horizontal=True)
        st.markdown("---")
        
        all_trends = generate_50_trends()
        
        # 필터링 로직
        if selected_platform == "🐦 X (Twitter)":
            filtered_trends = [t for t in all_trends if t["platform"] == "X (Twitter)"]
        elif selected_platform == "📸 Instagram":
            filtered_trends = [t for t in all_trends if t["platform"] == "Instagram"]
        else:
            filtered_trends = all_trends

        # 50개의 영상이 브라우저를 느리게 하는 것을 방지하기 위해 스크롤 컨테이너 사용
        with st.container(height=800):
            for t in filtered_trends:
                # 텍스트 정보
                st.markdown(f"""
                <div class="ranking-card">
                    <h4 style="margin:0; color:#fff;">🏅 {t['rank']}위 | {t['title']}</h4>
                    <p style="margin:5px 0 0 0; color:#aaa; font-size:0.9em;">
                        플랫폼: {t['platform']} | 📈 조회수: {t['count']}
                    </p>
                </div>
                """, unsafe_allow_html=True)
                
                # 실제 영상 임베드 노출
                if t['platform'] == "X (Twitter)":
                    embed_x_tweet(t['url'])
                else:
                    embed_instagram(t['url'])
                
                st.markdown("<br>", unsafe_allow_html=True)

# --- 푸터 ---
st.markdown("<br><hr style='border-color: #2d3139;'>", unsafe_allow_html=True)
st.caption("<div style='text-align:center; color:#666;'>© 2026 SNS Media Hub. All rights reserved. | 이용약관 | DMCA | 개인정보처리방침</div>", unsafe_allow_html=True)