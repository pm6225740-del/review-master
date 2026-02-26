import streamlit as st

# --- 1. 사이드바 디자인 설정 ---
st.sidebar.header("🎨 디자인 설정")
bg_color = st.sidebar.color_picker("배경색 선택", "#000000") # 기본 블랙
text_color = st.sidebar.color_picker("글자색 선택", "#FFFFFF") # 기본 화이트

# --- 2. 완벽한 CSS 적용 (숨은 글자까지 싹 다 잡음) ---
st.markdown(f"""
    <style>
    /* 1. 메인 화면 & 사이드바 배경색 통합 */
    [data-testid="stAppViewContainer"], [data-testid="stSidebar"] {{
        background-color: {bg_color} !important;
    }}
    
    /* 2. 모든 텍스트(제목, 본문, 사이드바 라벨 등) 색상 강제 지정 */
    [data-testid="stAppViewContainer"] p, 
    [data-testid="stAppViewContainer"] h1, 
    [data-testid="stAppViewContainer"] h2, 
    [data-testid="stAppViewContainer"] h3, 
    [data-testid="stSidebar"] p, 
    [data-testid="stSidebar"] h1, 
    [data-testid="stSidebar"] h2, 
    [data-testid="stSidebar"] span,
    [data-testid="stMarkdownContainer"] p {{
        color: {text_color} !important;
    }}

    /* 3. 사이드바 여는 화살표 버튼( > ) 색상 보호 (안 보이던 문제 해결) */
    [data-testid="collapsedControl"] svg {{
        fill: {text_color} !important;
    }}

    /* 4. 리뷰 입력창(Textarea) 절대 보호 (배경 흰색, 글자 검은색 고정) */
    .stTextArea textarea {{
        background-color: #FFFFFF !important;
        color: #000000 !important;
        font-size: 1.1rem !important;
        border: 2px solid #FF4B4B !important;
    }}
    .stTextArea textarea::placeholder {{
        color: #888888 !important;
    }}

    /* 5. 프라이버시 보호 (헤더/푸터 숨기기) */
    #MainMenu {{visibility: hidden;}}
    footer {{visibility: hidden;}}
    header {{visibility: hidden;}}
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
        # 결과 창 디자인도 업그레이드 (회색 박스에 담아 가독성 높임)
        st.markdown(f"""
            <div style="padding:20px; background-color:#1E1E1E; border-radius:10px; border:1px solid {text_color};">
                <strong style="color:{text_color};">[생성된 리뷰 결과]</strong><br><br>
                <span style="color:{text_color};">여기에 AI가 생성한 멋진 리뷰 내용이 표시됩니다.</span>
            </div>
        """, unsafe_allow_html=True)
    else:
        st.warning("먼저 내용을 입력해 주세요!")