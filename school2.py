import streamlit as st

# Helper function to parse the class schedule input
def parse_schedule_input(input_text):
    schedule = []
    for line in input_text.strip().split('\n'):
        time, subject = line.split('-', 1)
        schedule.append((time.strip(), subject.strip()))
    return schedule

# Initial data for each child (can be edited)
children_schedules = {
    "Ali Mansour": {
        "Monday": "08:00 - Svenska\n08:40 - Matematik\n09:45 - Slöjd\n12:00 - Naturorienterande ämnen\n12:55 - Idrott och hälsa",
        "Tuesday": "08:00 - Svenska\n08:45 - FTH\n09:45 - Matematik\n12:00 - Idrott och hälsa\n12:55 - Samhällsorienterande ämnen",
        "Wednesday": "08:00 - Svenska\n08:45 - Musik\n09:45 - FTH\n12:00 - Svenska\n12:40 - Naturorienterande ämnen",
        "Thursday": "08:00 - Svenska\n08:35 - Samhällsorienterande ämnen\n09:45 - Matematik\n12:00 - Teknik\n12:40 - Svenska",
        "Friday": "08:00 - Svenska\n08:45 - Samhällsorienterande ämnen\n09:45 - Engelska\n12:30 - Bild\n13:15 - Matematik"
    },
    "Yara Mansour": {
        "Monday": "08:00 - Svenska\n08:35 - Matematik\n09:45 - Engelska\n12:00 - Bild\n12:55 - Samhällsorienterande ämnen",
        "Tuesday": "08:00 - Matematik\n08:50 - Svenska\n09:45 - Samhällsorienterande ämnen\n12:00 - Naturorienterande ämnen\n13:40 - Svenska",
        "Wednesday": "08:00 - Samhällsorienterande ämnen\n08:45 - Matematik\n09:45 - Engelska\n12:10 - Idrott och hälsa\n13:05 - Naturorienterande ämnen",
        "Thursday": "08:00 - Svenska\n08:50 - Samhällsorienterande ämnen\n09:45 - Matematik\n10:25 - Engelska\n13:25 - Svenska",
        "Friday": "08:00 - Samhällsorienterande ämnen\n08:45 - Svenska\n09:45 - Idrott och hälsa"
    },
    "Esra Mansour": {
        "Monday": "08:00 - Mentorstid (MTID)\n13:00 - Samhällsorienterande ämnen",
        "Tuesday": "08:00 - Hem- och konsumentkunskap\n09:10 - Samhällsorienterande ämnen\n10:20 - Hem- och konsumentkunskap\n12:50 - Slöjd",
        "Wednesday": "08:00 - Matematik\n09:05 - Samhällsorienterande ämnen\n09:55 - Engelska\n10:45 - Naturorienterande ämnen\n13:55 - Svenska",
        "Thursday": "08:00 - Matematik\n09:00 - Matematik\n10:00 - Bild\n11:10 - Samhällsorienterande ämnen\n12:50 - Idrott och hälsa",
        "Friday": ""
    },
    "Omar Mansour": {
        "Monday": "09:25 - Svenska som andraspråk\n10:30 - Matematik\n12:10 - Naturorienterande ämnen\n13:25 - Samhällsorienterande ämnen",
        "Tuesday": "08:20 - Svenska som andraspråk\n09:25 - Engelska\n10:25 - Musik\n12:30 - Samhällsorienterande ämnen\n14:05 - Matematik",
        "Wednesday": "09:30 - Samhällsorienterande ämnen\n10:40 - Matematik\n12:55 - Svenska som andraspråk\n15:05 - Idrott och hälsa",
        "Thursday": "08:15 - Slöjd\n09:40 - Engelska\n10:45 - Naturorienterande ämnen\n12:30 - Svenska som andraspråk\n13:15 - Svenska som andraspråk",
        "Friday": "08:40 - Bild\n09:55 - Samhällsorienterande ämnen\n11:00 - Svenska som andraspråk\n12:25 - Matematik\n13:35 - Naturorienterande ämnen\n14:45 - Teknik"
    },
    "Sara Mansour": {
        "Monday": "13:30 - Skolstart",
        "Tuesday": "16:00 - Studietid",
        "Wednesday": "16:00 - Studietid",
        "Thursday": "08:00 - Studietid",
        "Friday": "16:00 - Studietid"
    }
}

# Streamlit app
st.title("Children's Weekly Schedule - Week 34")

# Iterate over each child and allow schedule editing
for child, schedule in children_schedules.items():
    st.header(f"{child}")
    for day, classes in schedule.items():
        st.subheader(day)
        schedule_input = st.text_area(f"Edit {child}'s schedule for {day}", value=classes, height=150)
        children_schedules[child][day] = schedule_input  # Update the schedule
        
        # Parse and display schedule
        parsed_schedule = parse_schedule_input(schedule_input)
        for time, subject in parsed_schedule:
            st.write(f"{time} - {subject}")
        
        # Highlight last class in red
        if parsed_schedule:
            last_class_time, last_class_subject = parsed_schedule[-1]
            st.markdown(f"<span style='color:red'><strong>Last class of the day:</strong> {last_class_time} - {last_class_subject}</span>", unsafe_allow_html=True)
        else:
            st.info("No classes scheduled for this day.")
    
    st.markdown("---")

st.write("Schedule provided for Week 34")

# Optionally, save the schedules to a file or database at the end of the week.
