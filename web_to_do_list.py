import streamlit as st


import functions

def add_to_do_item():
    item = st.session_state["add_to_do"]+"\n"
    to_do_list.append(item)
    functions.write_to_do_list_files(to_do_list)
    st.session_state['add_to_do'] = ""



to_do_list=functions.get_to_do_list()
st.title("My To-Do App")

st.subheader("This is my first to do app")

st.write("This app is to increase your productivity")

for index,to_do in enumerate(to_do_list):
    checkbox = st.checkbox(to_do,key=to_do)
    if checkbox:
        to_do_list.pop(index)
        functions.write_to_do_list_files(to_do_list)
        del st.session_state[to_do]
        st.rerun()

st.text_input(label="",placeholder="Add a new to do",on_change=add_to_do_item,key="add_to_do")

print("Hi")

st.session_state
