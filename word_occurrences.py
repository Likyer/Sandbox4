def main():
    emails = {}
    email = input("Please enter your email: ")
    while email != "":
        email_check(email, emails)
        email = input("Please enter your email: ")

    for x in emails:
        print(f"({x}) {emails[x]}")


def email_check(email, emails):
    name = get_name(email)
    name_confirm = input(f"Is your name {name}? (Y/n)")
    if name_confirm == "":
        emails[name] = email
    elif name_confirm.upper() == "Y":
        emails[name] = email
    else:
        new_name = input("You name is?")
        emails[new_name] = email


def get_name(email):
    words = email.split('@')[0]
    name = words.split('.')[0]
    return name


main()