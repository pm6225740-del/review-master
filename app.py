import streamlit as st
import yt_dlp
import os
import tempfile
from datetime import datetime

# 1. 페이지 기본 설정 (와이드 모드)
st.set_page_config(page_title="SNS 미디어 다운로더 & 랭킹", page_icon="🎬", layout="wide")

# 2. 디자인 커스텀 (CSS) - 이미지의 어두운 테마와 배너 레이아웃 반영
st.markdown("""
    <style>
    /* 전체 배경 및 폰트 설정 */
    .main { background-color: #0e1117; }
    .stApp { color: #ffffff; }
    
    /* 광고 배너 스타일 */
    .ad-slot {
        background: linear-gradient(135deg, #1e1e2f 0%, #252545 100%);
        border: 1px solid #3d3d5c;
        border-radius: 12px;
        padding: 40px 10px;
        text-align: center;
        color: #a0a0c0;
        font-weight: bold;
        margin-bottom: 15px;
        transition: 0.3s;
    }
    .ad-slot:hover { border-color: #7d7dff; color: #ffffff; }
    
    /* 강조 텍스트 */
    .highlight { color: #8a2be2; font-weight: bold; }
    </style>
""", unsafe_allow_html=True)

# 3. 백엔드 로직: 영상 추출 함수
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

# 4. 앱 레이아웃 구성
# [왼쪽 광고] [중앙 메인 기능] [오른쪽 광고]
left_ad, main_content, right_ad = st.columns([1.5, 7, 1.5])

# --- 왼쪽 사이드 배너 (수익화) ---
with left_ad:
    st.markdown('<div class="ad-slot">💰 SHOP<br><br>추천 상품<br>배너 영역</div>', unsafe_allow_html=True)
    st.markdown('<div class="ad-slot">🔥 HOT<br><br>제휴 마케팅<br>슬롯</div>', unsafe_allow_html=True)

# --- 중앙 메인 영역 ---
with main_content:
    # 상단 공지/광고 바
    st.markdown('<div class="ad-slot" style="padding:15px;">📢 공지: 고화질 인스타그램/X 영상 다운로드 기능을 무료로 이용하세요!</div>', unsafe_allow_html=True)
    
    st.title("🚀 SNS 미디어 허브")
    st.subheader("실시간 검색 다운로드 & 랭킹 시스템")
    
    # 탭 구성: 다운로드와 랭킹 분리
    tab1, tab2 = st.tabs(["📥 다운로드", "📊 실시간 인기 랭킹"])
    
    # [탭 1: 다운로드 기능]
    with tab1:
        st.write("")
        url_input = st.text_input(
            "다운로드할 SNS 링크(URL)를 입력하세요",
            placeholder="https://x.com/... 또는 https://www.instagram.com/reels/..."
        )
        
        col1, col2 = st.columns([1, 4])
        with col1:
            platform = st.selectbox("플랫폼 선택", ["자동 감지", "X (Twitter)", "Instagram"])
        
        if st.button("추출하기", use_container_width=True):
            if url_input:
                with st.spinner('영상을 가져오는 중입니다...'):
                    file_path, title_or_error = download_video(url_input)
                    
                    if file_path and os.path.exists(file_path):
                        st.success(f"✅ 준비 완료: {title_or_error[:30]}...")
                        with open(file_path, "rb") as f:
                            st.download_button(
                                label="💾 내 기기에 저장하기",
                                data=f,
                                file_name=os.path.basename(file_path),
                                mime="video/mp4",
                                use_container_width=True
                            )
                    else:
                        st.error(f"오류가 발생했습니다: {title_or_error}")
            else:
                st.warning("링크를 입력해주세요.")

    # [탭 2: 실시간 랭킹 - 수익화 핵심 (체류시간 증대)]
    with tab2:
        st.markdown("### 🔥 현재 화제의 영상 TOP 5")
        # 실제 데이터베이스와 연결하기 전까지는 트렌드 데이터를 수동/더미로 관리
        trends = [
            {"rank": 1, "platform": "Instagram", "title": "오늘자 압구정 핫플 상황.mp4", "count": "1.2k"},
            {"rank": 2, "platform": "X", "title": "실시간 속보: 신기술 발표 현장", "count": "942"},
            {"rank": 3, "platform": "Instagram", "title": "이거 보면 다이어트 포기함", "count": "850"},
            {"rank": 4, "platform": "X", "title": "강아지들의 귀여운 반란", "count": "720"},
            {"rank": 5, "platform": "Instagram", "title": "올해 꼭 가야할 여행지", "count": "610"}
        ]
        
        for t in trends:
            st.info(f"**{t['rank']}위** [{t['platform']}] {t['title']} | 📈 {t['count']}회 다운로드됨")

# --- 오른쪽 사이드 배너 (수익화) ---
with right_ad:
    st.markdown('<div class="ad-slot">📺 AD<br><br>구글 광고<br>자리</div>', unsafe_allow_html=True)
    st.markdown('<div class="ad-slot">⭐ BRAND<br><br>입점 문의<br>하러가기</div>', unsafe_allow_html=True)

# --- 푸터 영역 ---
st.markdown("---")
f_col1, f_col2, f_col3 = st.columns(3)
with f_col1: st.caption("© 2026 SNS Downloader All rights reserved.")
with f_col2: st.caption("문의: support@example.com")
with f_col3: st.caption("DMCA 정책 | 이용약관")