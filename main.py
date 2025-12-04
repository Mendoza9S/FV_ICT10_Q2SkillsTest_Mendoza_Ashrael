from pyscript import document, display

# dictionary for all the information of the clubs i chose
clubs = {
    "Social Studies Club": {
        "name": "SocSci Club",
        "description": "A club for history, political science, and other branches of social studies enthusiasts of all skill levels.",
        "meeting_time": "Every Tuesday and Thursday, 3:00–4:00 PM",
        "location": "Room 409",
        "moderator": "Mr. Lim",
        "members": 21,
        "category": "Academic"
    },

    "Basketball Varsity": {
        "name": "Basketball Varsity",
        "description": "Aspiring students put their skill of Basketball to use whilst having fun.",
        "meeting_time": "Every Monday, 3:00–5:00 PM",
        "location": "Quadrangle",
        "moderator": "Coach Ruiz",
        "members": 16,
        "category": "Non-Academic"
    },

    "Marching Band": {
        "name": "Marching Band",
        "description": "Students use their skill in various musical instruments in the setting of a band",
        "meeting_time": "Every Tuesday and Wednesday, 3:00–4:30 PM",
        "location": "Band Room",
        "moderator": "Mr. Emilio Alumno",
        "members": 26,
        "category": "Non-Academic"
    }
}

# function that recognizes which club was chosen in the index.html file club-select thing
def show_selected_club(event=None):
    club_name = document.getElementById("club-select").value
    info = clubs[club_name] 

    # this is what shows up when the code recognizes what was chosen, text being what is inputed in the output part in index.html
    text = (
        f"Name: {info['name']}\n"
        f"Description: {info['description']}\n"
        f"Meeting Time: {info['meeting_time']}\n"
        f"Location: {info['location']}\n"
        f"Club Moderator: {info['moderator']}\n"
        f"Number of Members: {info['members']}\n"
        f"Category: {info['category']}"
    )
    #links py to html, append=false is so that the results wouldnt loop and stack on top of each other, https://hyperskill.org/university/python/append-method-in-python
    display(text, target="output", append=False)
