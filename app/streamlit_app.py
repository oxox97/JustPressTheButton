import streamlit as st

# 페이지 설정
st.set_page_config(page_title="Fancy Travel Utilities", layout="wide")

# 커스텀 CSS 삽입
st.markdown("""
    <style>
    .card {
        background-color: #1f1f1f;
        border-radius: 15px;
        padding: 20px;
        margin: 10px 0;
        transition: all 0.3s ease-in-out;
        box-shadow: 0 4px 6px rgba(0,0,0,0.3);
        color: white;
        cursor: pointer;
    }
    .card:hover {
        transform: scale(1.03);
        box-shadow: 0 6px 12px rgba(255, 255, 255, 0.2);
        background: linear-gradient(145deg, #2e2e2e, #1c1c1c);
    }
    .card-title {
        font-size: 20px;
        font-weight: bold;
    }
    .card-subtitle {
        color: #ccc;
        font-size: 14px;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("<h2 style='text-align: center;'>✨ Essential Utilities for Your Journey ✨</h2>", unsafe_allow_html=True)

# 카드 리스트
cards = [
    ("💱", "Currency Converter", "Quickly check exchange rates.", "https://example.com/currency"),
    ("🌐", "Translator", "Type or speak to bridge languages.", "https://example.com/translator"),
    ("🌤️", "Air Quality Index", "Check air quality for any city.", "https://example.com/air"),
    ("🗺️", "Country Guide", "Essential info for your destination.", "https://example.com/guide"),
    ("🕓", "Time Zone Converter", "Add friends' zones, see overlap.", "https://example.com/timezone"),
    ("📘", "Phrasebook", "Common phrases for travelers.", "https://example.com/phrasebook"),
]

# 두 칼럼에 카드 배치
cols = st.columns(2)

for i, (icon, title, subtitle, url) in enumerate(cards):
    with cols[i % 2]:
        card_html = f"""
        <a href="{url}" target="_blank" style="text-decoration: none;">
            <div class="card">
                <div class="card-icon" style="font-size: 30px;">{icon}</div>
                <div class="card-title">{title}</div>
                <div class="card-subtitle">{subtitle}</div>
            </div>
        </a>
        """
        st.markdown(card_html, unsafe_allow_html=True)
