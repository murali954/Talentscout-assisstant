import streamlit as st
import cohere
from datetime import datetime
import json, re

# --
COHERE_API_KEY = ""#replace with your api key
co = cohere.Client(COHERE_API_KEY)


st.set_page_config(page_title="TalentScout - Hiring Assistant", page_icon="🧑‍💻", layout="centered")

st.title("🧑‍💼 TalentScout — Hiring Assistant")
st.caption("Your AI-powered hiring assistant. Please enter your details to begin the screening.")


if "candidate" not in st.session_state:
    st.session_state.candidate = {}
if "questions" not in st.session_state:
    st.session_state.questions = []
if "current_q" not in st.session_state:
    st.session_state.current_q = 0
if "answers" not in st.session_state:
    st.session_state.answers = []
if "finished" not in st.session_state:
    st.session_state.finished = False


if not st.session_state.candidate:
    with st.form("candidate_form"):
        full_name = st.text_input("Full Name")
        email = st.text_input("Email Address")
        phone = st.text_input("Phone Number")
        exp = st.text_input("Years of Experience")
        position = st.text_input("Desired Position(s)")
        location = st.text_input("Current Location")
        tech_stack = st.text_input("Tech Stack (e.g., Python, Django, React)")

        submitted = st.form_submit_button("Save & Start Interview")
        if submitted:
            st.session_state.candidate = {
                "full_name": full_name,
                "email": email,
                "phone": phone,
                "experience": exp,
                "position": position,
                "location": location,
                "tech_stack": tech_stack,
                "timestamp": datetime.utcnow().isoformat()
            }

            user_prompt = f"""
            Candidate Tech Stack: {tech_stack}.
            Generate up to 5 interview questions in total (not per tech).
            Cover the most important technologies from the stack.
            Format strictly as JSON:
            {{"Tech": ["Q1", "Q2", ...]}}
            """

            try:
                resp = co.chat(model="command-r-plus", message=user_prompt, temperature=0.3)
                match = re.search(r"\{.*\}", resp.text, re.S)
                block = match.group(0) if match else resp.text
                data = json.loads(block)

                all_qs = []
                for tech, qs in data.items():
                    for q in qs:
                        all_qs.append(f"({tech}) {q}")
                st.session_state.questions = all_qs[:5]

            except Exception:
                st.session_state.questions = []
            
            st.session_state.current_q = 0
            st.rerun()



if st.session_state.candidate and not st.session_state.finished:
    if st.session_state.questions:
        if st.session_state.current_q < len(st.session_state.questions):
            question = st.session_state.questions[st.session_state.current_q]
            st.subheader(f"Question {st.session_state.current_q+1}")
            st.write(question)

            answer = st.text_area("Your Answer:", key=f"ans_{st.session_state.current_q}")
            if st.button("Submit Answer"):
                st.session_state.answers.append({"q": question, "a": answer})
                st.session_state.current_q += 1
                st.rerun()
        else:
            st.success("🎉 Thank you! You have completed the interview questions.")
            st.session_state.finished = True
            st.write("✅ We’ve recorded your responses. Our team will review your profile and contact you with next steps.")
    else:
        st.error("⚠️ Unable to generate questions right now. Please try again later.")

