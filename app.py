import streamlit as st

# --- 1. 사이드바 디자인 설정 ---
st.sidebar.header("🎨 디자인 설정")
bg_color = st.sidebar.color_picker("배경색 선택", "#000000") # 기본 블랙
text_color = st.sidebar.color_picker("글자색 선택", "#FFFFFF") # 기본 화이트

# --- 2. 문제 해결된 CSS 스타일 ---
st.markdown(f"""
    <style>
    /* 전체 배경색 */
    .stApp {{
        background-color: {bg_color};
    }}
    
    /* 모든 텍스트 색상 강제 지정 */
    .stApp p, .stApp h1, .stApp h2, .stApp h3, .stApp span, .stApp label {{
        color: {text_color} !important;
    }}

    /* 리뷰 입력창 절대 보호 (하얀 바탕, 검은 글씨) */
    .stTextArea textarea {{
        background-color: #FFFFFF !important;
        color: #000000 !important;
        font-size: 1.1rem !important;
        border: 2px solid #FF4B4B !important;
    }}

    /* 🚨 문제의 원인 해결: 헤더를 완전히 숨기지 않고 배경만 투명하게 처리 🚨 */
    header {{
        background-color: transparent !important;
    }}

    /* 프라이버시 보호: 우측 상단 햄버거 메뉴와 하단 푸터만 핀셋으로 숨김 */
    #MainMenu {{visibility: hidden;}}
    footer {{visibility: hidden;}}
    </style>
    """, unsafe_allow_html=True)

# --- 3. 앱 메인 콘텐츠 ---
st.title("🚀 AI 리뷰 마스터")
st.markdown("### 사장님의 비즈니스를 위한 최적의 리뷰를 생성합니다.")

# 입력창
review_input = st.text_area(
    "어떤 리뷰를 만들어드릴까요?", 
    placeholder="예: 맛있는 커피, 친절한 매장, 사진 찍기 좋은 곳",
    height=200
)

# 생성 버튼
if st.button("AI 리뷰 생성하기"):
    if review_input:
        st.success("리뷰 생성이 완료되었습니다!")
        st.markdown(f"""
            <div style="padding:20px; background-color:#1E1E1E; border-radius:10px; border:1px solid {text_color};">
                <strong style="color:{text_color};">[생성된 리뷰 결과]</strong><br><br>
                <span style="color:{text_color};">여기에 AI가 생성한 멋진 리뷰 내용이 표시됩니다.</span>
            </div>
        """, unsafe_allow_html=True)
    else:
        st.warning("먼저 내용을 입력해 주세요!")