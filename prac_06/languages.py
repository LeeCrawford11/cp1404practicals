from programming_language import ProgrammingLanguage

ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
language_list = [ruby, python, visual_basic]
print(ruby)
print(python)
print(visual_basic)
for line in language_list:
    if line.is_dynamic():
        print(line.name)
