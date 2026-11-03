import streamlit as st
from chatbot import ObedAI

# =====================================
# PAGE CONFIGURATION
# =====================================

st.set_page_config(
    page_title="OBED AI | Ghana Edition",
    page_icon="🇬🇭",
    layout="centered"
)

# =====================================
# INITIALIZE CHATBOT
# =====================================

if "chatbot" not in st.session_state:
    st.session_state.chatbot = ObedAI()

if "messages" not in st.session_state:
    st.session_state.messages = []

# =====================================
# CUSTOM STYLING
# =====================================

st.markdown("""
<style>

.stApp {
    background-color: #0b1120;
    color: #f8fafc;
}

.main-title {
    text-align: center;
    font-size: 42px;
    font-weight: 800;
    color: #38bdf8;
    margin-bottom: 5px;
}

.subtitle {
    text-align: center;
    color: #94a3b8;
    font-size: 15px;
    margin-bottom: 25px;
}

.info-box {
    background-color: #151e30;
    border: 1px solid #334155;
    border-radius: 12px;
    padding: 15px;
    text-align: center;
    margin-bottom: 20px;
}

.stChatMessage {
    border-radius: 12px;
}

footer {
    visibility: hidden;
}

</style>
""", unsafe_allow_html=True)

# =====================================
# HEADER
# =====================================

st.markdown(
    '<div class="main-title">OBED AI 🇬🇭</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Your Personal Virtual Assistant</div>',
    unsafe_allow_html=True
)

st.markdown("""
<div class="info-box">
    <strong>AKWAABA!</strong><br>
    Welcome to OBED AI – Ghana Edition.<br>
    Chat with me in English or try some Twi expressions.
</div>
""", unsafe_allow_html=True)

# =====================================
# SIDEBAR
# =====================================

with st.sidebar:

    st.title("OBED AI 🇬🇭")

    st.write("Your smart conversational assistant.")

    st.divider()

    st.subheader("What I can do")

    st.write("👋 Respond to greetings")
    st.write("🗣️ Recognize selected Twi phrases")
    st.write("📅 Provide date and time")
    st.write("🤖 Answer basic AI questions")
    st.write("💻 Discuss programming")
    st.write("💬 Maintain conversations")

    st.divider()

    if st.button("Clear Conversation", use_container_width=True):

        st.session_state.messages = []

        st.session_state.chatbot = ObedAI()

        st.rerun()

    st.caption("Developed with Python.")
    st.caption("Proudly Ghanaian 🇬🇭")

# =====================================
# DISPLAY CHAT HISTORY
# =====================================

for message in st.session_state.messages:

    with st.chat_message(message["role"]):

        st.markdown(message["content"])

# =====================================
# CHAT INPUT
# =====================================

user_input = st.chat_input(
    "Type your message to OBED AI..."
)

if user_input:

    # Display user message
    st.session_state.messages.append({
        "role": "user",
        "content": user_input
    })

    with st.chat_message("user"):
        st.markdown(user_input)

    # Generate chatbot response
    response = st.session_state.chatbot.get_response(
        user_input
    )

    # Display chatbot response
    st.session_state.messages.append({
        "role": "assistant",
        "content": response
    })

    with st.chat_message("assistant"):
        st.markdown(response)

# =====================================
# FOOTER
# =====================================

st.divider()

st.markdown(
    "<center>OBED AI | Ghana Edition 🇬🇭<br>"
    "Simple Conversations. Smart Responses.</center>",
    unsafe_allow_html=True
)
