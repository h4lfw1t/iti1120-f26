def is_eligible(age, citizenship, conviction_status) -> bool:
    if age >= 18 and is_citizen(citizenship) and not is_convicted(conviction_status):
        return True
    else:
        return False

def is_citizen(country: str) -> bool:
    if country.lower().strip() in ("canada", "canadian"):
        return True
    else:
        return False

def is_convicted(status: str) -> bool:
    if status.lower().strip() in ("yes"):
        return True
    else:
        return False

name = input("What is your name? ")
age = int(input("How old are you? "))
citizenship = input("What is your citizenship? ")
conviction_status = input("Have you been convicted of a crime? (yes/no) ")

if is_eligible(age, citizenship, conviction_status):
    print(name, ", you are eligible to vote")
else:
    print(name, ", you are ineligible to vote")