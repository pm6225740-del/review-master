import streamlit as st

# --- 1. 사이드바 디자인 설정 영역 ---
st.sidebar.header("🎨 디자인 설정")
# 사장님이 직접 배경색과 글자색을 고를 수 있는 기능을 넣었습니다.
bg_color = st.sidebar.color_picker("배경색을 선택하세요", "#000000") 
text_color = st.sidebar.selectbox("글자색을 선택하세요", ["#FFFFFF", "#000000", "#F8F9FA"])

# --- 2. CSS 스타일 적용 (프라이버시 및 가독성) ---
# 배경색은 바뀌어도 입력창은 항상 잘 보이도록 설정했습니다.
st.markdown(f"""
    <style>
    /* 전체 배경 및 기본 글자색 설정 */
    .stApp {{
        background-color: {bg_color};
        color: {text_color};
    }}
    
    /* 리뷰 입력창: 하얀 배경에 검은 글씨로 가독성 확보 */
    textarea {{
        background-color: #FFFFFF !important;
        color: #000000 !important;
        font-size: 1.1rem !important;
        border-radius: 10px !important;
    }}
    
    /* 입력창 위 라벨(제목) 글자색 설정 */
    .stTextArea label p {{
        color: {text_color} !important;
        font-weight: bold;
    }}

    /* 프라이버시 보호: 상단 메뉴, 깃허브 아이콘, 하단 푸터 숨기기 */
    #MainMenu {{visibility: hidden;}}
    footer {{visibility: hidden;}}
    header {{visibility: hidden;}}
    </style>
    """, unsafe_allow_html=True)

# --- 3. 앱 콘텐츠 영역 ---
st.title("🚀 AI 리뷰 마스터")
st.write("사장님의 비즈니스를 위한 최적의 리뷰를 생성합니다.")

# 사용자가 입력하는 공간입니다.
review_input = st.text_area(
    "어떤 리뷰를 만들어드릴까요?", 
    placeholder="예: 강남역 맛집, 친절한 서비스, 재방문 의사 200%",
    height=200
)

if st.button("AI 리뷰 생성하기"):
    if review_input:
        st.success("멋진 리뷰가 준비되었습니다!")
        # 여기에 추후 AI API를 연결하면 실제 결과가 나옵니다.
        st.info(f"입력하신 내용: {review_input}")
    else:
        st.warning("내용을 먼저 입력해 주세요!")