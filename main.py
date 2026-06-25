import streamlit as st
from agent.agent_ex import config, pipeline_with_history
from agent.summon_llm import llm
from config.summon_langsmith import get_langsmith


def main():
    get_langsmith()

    st.set_page_config(page_title="AI Agent Chat", page_icon="🤖")
    st.title("🤖 AI Agent Chatbot")
    st.write("اسأل العميل الذكي أي سؤال تريده!")

    if "messages" not in st.session_state:
        st.session_state.messages = []

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    if human_input := st.chat_input("ما هو سؤالك؟"):

        exit_commands = ["exit", "ثءهف", "خروج", "ov,[", "ov,[]"]
        if human_input.lower() in exit_commands:
            st.warning("يمكنك ببساطة إغلاق المتصفح لإنهاء الجلسة.")
            return

        with st.chat_message("user"):
            st.markdown(human_input)
        st.session_state.messages.append({"role": "user", "content": human_input})

        with st.chat_message("assistant"):
            with st.spinner("جاري التفكير..."):
                try:
                    out = pipeline_with_history.invoke(
                        {"input": human_input}, config=config
                    )

                    response = out.get("output", "لم يتم العثور على مخرجات.")

                    st.markdown(response)
                    st.session_state.messages.append(
                        {"role": "assistant", "content": response}
                    )

                except Exception as e:
                    st.error(f"حدث خطأ أثناء معالجة الطلب: {e}")


if __name__ == "__main__":
    main()