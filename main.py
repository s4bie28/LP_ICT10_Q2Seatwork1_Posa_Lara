from pyscript import document, when

club_members = [
    'lara posa',
    'cloie abenojar',
    'mia padillo',
    'ezra lazo',
    'aica pizzaro',
    'simone tinio',
    'jarissa dizon',
    'ruffalyn cuartero',
    'christian torres',
    'ruzia cruz'
]

@when("click", "#enter_button")
def candidate_checker(event):
    f_name = document.getElementById('first_name').value.strip()
    l_name = document.getElementById('last_name').value.strip()

    candidate = f"{f_name} {l_name}".strip()

    if not f_name or not l_name:
        message = "Please enter your first and last name!"
    elif candidate.lower() in club_members:
        message = f"Congratulations, {candidate}! You are now part of the Volleyball Varsity!"
    else:
        message = f"Sorry, {candidate}. Your name is not on the list."

    document.getElementById('result').innerText = message
