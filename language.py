from programming_language import ProgrammingLanguage


def main():

main
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)

    print(ruby)
    print(python)
    print(visual_basic)

    print("************************")

    language_list = [ruby, python, visual_basic]
    for x in language_list:
        if x.is_dynamic():
            print(x)

    print("************************")

    print("The dynamically typed languages are:")
    for dynamic in language_list:
        if dynamic.is_dynamic():
            print(dynamic.field)

main()