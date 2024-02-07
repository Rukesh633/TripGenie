import streamlit as st
from usellm import UseLLM, Message, Options
from utils import TOUR_GUIDE_SYSTEM, TRIP_PLANNER_SYSTEM

service = UseLLM(service_url="https://usellm.org/api/llm")

st.set_page_config(layout="wide")


def tour_guide_section():
    st.title("Tour Guide Assistant")
    user_input = st.text_input("Enter the Place You Want to Visit", key="input1")
    if st.button("Send", key="button1"):
        if user_input:
            system_message = TOUR_GUIDE_SYSTEM
            output = get_response(system_message, user_input)
            st.markdown(output.content)
        else:
            st.markdown("Please Enter Some Text")


def trip_planner_section():
    st.title("Personal Trip Planner")
    user_input = st.text_input("Enter the Place You Want to Visit", key="input2")
    days = st.text_input("Enter the Number of Days", key="input3")
    budget = st.text_input("Enter Your Budget per person", key="input4")
    if st.button("Send", key="button2"):
        if user_input:
            system_message = TRIP_PLANNER_SYSTEM.format(days, budget)
            output = get_response(system_message, user_input)
            st.markdown(output.content)
        else:
            st.markdown("Please Enter Some Text")


def get_response(system_message, user_input,*args):
    messages = [
        Message(role="system", content=system_message),
        Message(role="user", content=user_input)
    ]
    options = Options(messages=messages)
    output = service.chat(options)
    return output


def show(output):
    if output:
        st.markdown(output.content)
    elif output == "NULL":
        st.markdown("Please Enter Some Text")


def main():
    tab1, tab2 = st.tabs(["Tour Guide", "Trip Planner"])

    with tab1:
        output = tour_guide_section()
        show(output)

    with tab2:
        output = trip_planner_section()
        show(output)



if __name__ == "__main__":
    main()