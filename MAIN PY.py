import streamlit as st
import random

st.set_page_config(page_title="لعبة تخمين الأرقام", page_icon="🎮")

st.title("🎮  لعبة تفكير الأرقام السرية ياسين")
st.write("لقد اخترت رقماً سرياً بين 50 0، هل يمكنك معرفته؟")

if 'secret_number' not in st.session_state:
    st.session_state.secret_number = random.randint(1, 50)
    st.session_state.attempts = 0

guess = st.number_input("اكتب تخمينك هنا (من 1 إلى 50):", min_value=1, max_value=50, step=1)

if st.button("تأكيد التخمين"):
    st.session_state.attempts += 1
    if guess < st.session_state.secret_number:
        st.warning("📉 رقمك أصغر من الرقم السري! حاول برقم أكبر.")
    elif guess > st.session_state.secret_number:
        st.warning("📈 رقمك أكبر من الرقم السري! حاول برقم أصغر.")
    else:
        st.success(f"🎉 مبروك الفوز! الرقم الصحيح هو [{st.session_state.secret_number}]")
        st.info(f"📊 عدد المحاولات: {st.session_state.attempts}")
