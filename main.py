
from pyscript import document

def candidate_checker(e):

    club_members = [
        "czarina lodronio",
        "simone tinio",
        "ezra lazo",
        "yanna moya"
    ]

    f_name = document.getElementById("first_name").value
    l_name = document.getElementById("last_name").value


    candidate = f"{f_name.strip()} {l_name.strip()}"

    member_checker = candidate.lower() in club_members


    if member_checker:
        message = (
            f"Congratulations, {candidate}! "
            "You are part of the Volleyball Varsity."
        )
    else:
        message = (
            f"Sorry, {candidate}! "
            "Your name is not on the list."
        )

    document.getElementById("result").innerHTML = message
