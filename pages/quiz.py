import streamlit as st


def question_sheet(data):

    form = st.form(key='form')
    score = 0
    user_answers = []
    correct_answer = []
    for i in data:
        # st.caption(f"Question {i}")
        answer = form.radio(f"Question {i}:\n{data[i]['question']}", data[i]['options'])
        correct_answer.append(data[i]['answer'])
        user_answers.append(answer)

    submit=form.form_submit_button("Submit Quiz")

    if submit:
        for q in range(len(correct_answer)):
            if user_answers[q] == correct_answer[q]:
                score += 1

        st.write(f"Your Score was {score}/{len(correct_answer)}")
        st.subheader("Correct Answers:")
        for i, ans in enumerate(correct_answer, start=1):
            st.write(f"Question {i}: {ans}")


def main():
    st.set_page_config(page_title="Quiz Generator", page_icon="❔")

    if 'topic' not in st.session_state and 'num_of_questions' not in st.session_state and 'data' not in st.session_state:
        st.session_state['topic'] = None
        st.session_state['num_of_questions'] = None
        st.session_state['data'] = None
    else:
        topic = st.session_state["topic"]
        num_of_questions = st.session_state["num_of_questions"]
        data = st.session_state['data']
        st.title(f"{topic} MCQ Quiz")

        question_sheet(data)


if __name__ == "__main__":
    main()
