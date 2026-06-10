import os
import sys
import streamlit as st
from agent.agent_ex import config, pipeline_with_history
from agent.summon_llm import llm
from config.summon_langsmith import get_langsmith


def main():
    # إعداد وتجهيز Langsmith
    get_langsmith()

    # إعداد عنوان الصفحة
    st.set_page_config(page_title="AI Agent Chat", page_icon="🤖")
    st.title("🤖 AI Agent Chatbot")
    st.write("اسأل العميل الذكي أي سؤال تريده!")

    # تهيئة سجل المحادثة (Chat History) في الـ Session State إذا لم يكن موجوداً
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # عرض الرسائل السابقة من السجل عند إعادة تحميل الصفحة
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # استقبال مدخلات المستخدم عبر صندوق الشات الذكي
    if human_input := st.chat_input("ما هو سؤالك؟"):

        # قائمة كلمات الخروج (اختياري: في Streamlit المستخدم يغلق المتصفح ببساطة،
        # لكن سنضيف فحصاً سريعاً لتنبيه المستخدم إذا كتب كلمة خروج)
        exit_commands = ["exit", "ثءهف", "خروج", "ov,[", "ov,[]"]
        if human_input.lower() in exit_commands:
            st.warning("يمكنك ببساطة إغلاق المتصفح لإنهاء الجلسة.")
            return

        # 1. عرض رسالة المستخدم في واجهة الشات وحفظها في السجل
        with st.chat_message("user"):
            st.markdown(human_input)
        st.session_state.messages.append({"role": "user", "content": human_input})

        # 2. تشغيل الـ Agent وعرض النتيجة
        with st.chat_message("assistant"):
            # إضافة Spinner (علامة تحميل) أثناء معالجة الـ Agent للطلب
            with st.spinner("جاري التفكير..."):
                try:
                    # استدعاء الـ pipeline
                    out = pipeline_with_history.invoke(
                        {"input": human_input}, config=config
                    )

                    # استخراج المخرجات من القاموس بناءً على طلبك
                    response = out.get("output", "لم يتم العثور على مخرجات.")

                    # عرض الإجابة وحفظها في السجل
                    st.markdown(response)
                    st.session_state.messages.append(
                        {"role": "assistant", "content": response}
                    )

                except Exception as e:
                    st.error(f"حدث خطأ أثناء معالجة الطلب: {e}")


if __name__ == "__main__":
    main()