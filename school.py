import streamlit as st

# Data for each child
children_schedules = {
    "Ali Mansour": {
        "Monday": [("08:00", "Svenska"), ("08:40", "Matematik"), ("09:45", "Slöjd"), ("12:00", "Naturorienterande ämnen"), ("12:55", "Idrott och hälsa")],
        "Tuesday": [("08:00", "Svenska"), ("08:45", "FTH"), ("09:45", "Matematik"), ("12:00", "Idrott och hälsa"), ("12:55", "Samhällsorienterande ämnen")],
        "Wednesday": [("08:00", "Svenska"), ("08:45", "Musik"), ("09:45", "FTH"), ("12:00", "Svenska"), ("12:40", "Naturorienterande ämnen")],
        "Thursday": [("08:00", "Svenska"), ("08:35", "Samhällsorienterande ämnen"), ("09:45", "Matematik"), ("12:00", "Teknik"), ("12:40", "Svenska")],
        "Friday": [("08:00", "Svenska"), ("08:45", "Samhällsorienterande ämnen"), ("09:45", "Engelska"), ("12:30", "Bild"), ("13:15", "Matematik")]
    },
    "Yara Mansour": {
        "Monday": [("08:00", "Svenska"), ("08:35", "Matematik"), ("09:45", "Engelska"), ("12:00", "Bild"), ("12:55", "Samhällsorienterande ämnen")],
        "Tuesday": [("08:00", "Matematik"), ("08:50", "Svenska"), ("09:45", "Samhällsorienterande ämnen"), ("12:00", "Naturorienterande ämnen"), ("13:40", "Svenska")],
        "Wednesday": [("08:00", "Samhällsorienterande ämnen"), ("08:45", "Matematik"), ("09:45", "Engelska"), ("12:10", "Idrott och hälsa"), ("13:05", "Naturorienterande ämnen")],
        "Thursday": [("08:00", "Svenska"), ("08:50", "Samhällsorienterande ämnen"), ("09:45", "Matematik"), ("10:25", "Engelska"), ("13:25", "Svenska")],
        "Friday": [("08:00", "Samhällsorienterande ämnen"), ("08:45", "Svenska"), ("09:45", "Idrott och hälsa")]
    },
    "Esra Mansour": {
        "Monday": [("08:00", "Mentorstid (MTID)"), ("13:00", "Samhällsorienterande ämnen")],
        "Tuesday": [("08:00", "Hem- och konsumentkunskap"), ("09:10", "Samhällsorienterande ämnen"), ("10:20", "Hem- och konsumentkunskap"), ("12:50", "Slöjd")],
        "Wednesday": [("08:00", "Matematik"), ("09:05", "Samhällsorienterande ämnen"), ("09:55", "Engelska"), ("10:45", "Naturorienterande ämnen"), ("13:55", "Svenska")],
        "Thursday": [("08:00", "Matematik"), ("09:00", "Matematik"), ("10:00", "Bild"), ("11:10", "Samhällsorienterande ämnen"), ("12:50", "Idrott och hälsa")],
        "Friday": []
    },
    "Omar Mansour": {
        "Monday": [("09:25", "Svenska som andraspråk"), ("10:30", "Matematik"), ("12:10", "Naturorienterande ämnen"), ("13:25", "Samhällsorienterande ämnen")],
        "Tuesday": [("08:20", "Svenska som andraspråk"), ("09:25", "Engelska"), ("10:25", "Musik"), ("12:30", "Samhällsorienterande ämnen"), ("14:05", "Matematik")],
        "Wednesday": [("09:30", "Samhällsorienterande ämnen"), ("10:40", "Matematik"), ("12:55", "Svenska som andraspråk"), ("15:05", "Idrott och hälsa")],
        "Thursday": [("08:15", "Slöjd"), ("09:40", "Engelska"), ("10:45", "Naturorienterande ämnen"), ("12:30", "Svenska som andraspråk"), ("13:15", "Svenska som andraspråk")],
        "Friday": [("08:40", "Bild"), ("09:55", "Samhällsorienterande ämnen"), ("11:00", "Svenska som andraspråk"), ("12:25", "Matematik"), ("13:35", "Naturorienterande ämnen"), ("14:45", "Teknik")]
    },
    "Sara Mansour": {
        "Monday": [("13:30", "Skolstart")],
        "Tuesday": [("16:00", "Studietid")],
        "Wednesday": [("16:00", "Studietid")],
        "Thursday": [("08:00", "Studietid")],
        "Friday": [("16:00", "Studietid")]
    }
}

# Streamlit app
st.title("Children's Weekly Schedule - Week 34")

# Iterate over each child and display their schedule
for child, schedule in children_schedules.items():
    st.header(f"{child}")
    for day, classes in schedule.items():
        st.subheader(day)
        for time, subject in classes:
            st.write(f"{time} - {subject}")
        if classes:
            last_class_time, last_class_subject = classes[-1]
            st.success(f"**Last class of the day:** {last_class_time} - {last_class_subject}")
        else:
            st.info("No classes scheduled for this day.")
    st.markdown("---")

st.write("Schedule provided for Week 34")
