import streamlit as st

st.title("To-Do List App")
st.write("Welcome to my To-Do List App!")

# Initialize session state for tasks
if "tasks" not in st.session_state:
    st.session_state["tasks"] = []

task = st.text_input("Enter a task", "")

# Add task to the list
if st.button("Add Task"):
    if task:
        st.session_state["tasks"].append(task)
        st.success ("Add task Successfully")
    else:
        st.warning("Task cannot be empty")

# Display tasks with checkboxes to remove them
tasks_to_remove = []
for i, task in enumerate(st.session_state["tasks"]):
    if st.checkbox(f"{i + 1}: {task}"):
        tasks_to_remove.append(task)

# Remove checked tasks
for task in tasks_to_remove:
    st.session_state["tasks"].remove(task)

# Display updated task list
st.write("### Task List")
for i, task in enumerate(st.session_state["tasks"]):
    st.write(f"{i + 1}: {task}")

