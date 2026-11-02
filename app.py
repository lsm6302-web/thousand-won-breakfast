
import json
from pathlib import Path

import streamlit as st

st.set_page_config(
    page_title="천원의 아침밥",
    page_icon="🍚",
    layout="centered"
)

DATA_FILE = Path(__file__).with_name("breakfast.json")


def load_data():
    if not DATA_FILE.exists():
        return {
            "quantity": 100,
            "updated_at": "아직 업데이트되지 않음"
        }

    try:
        with DATA_FILE.open("r", encoding="utf-8") as f:
            data = json.load(f)

        return data

    except (json.JSONDecodeError, OSError, KeyError):
        return {
            "quantity": 0,
            "updated_at": "데이터를 읽을 수 없음"
        }


@st.fragment(run_every="2s")
def student_page():
    data = load_data()
    quantity = int(data["quantity"])

    st.metric("현재 잔여 수량", f"{quantity}식")

    if quantity == 0:
        st.error("현재 잔여 수량이 없습니다.")
    elif quantity <= 10:
        st.warning("잔여 수량이 얼마 남지 않았어요!")
    else:
        st.success("아직 이용할 수 있어요!")

    st.caption(f"마지막 업데이트: {data['updated_at']}")
    st.caption("※ 실제 잔여 수량과 차이가 있을 수 있습니다.")


st.title("🍚 천원의 아침밥")
st.write("방문하기 전에 잔여 수량을 확인해 보세요.")

student_page()
