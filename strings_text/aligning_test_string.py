# Format text with some of alignment applied
text = "WelcomeToTop"
print text.ljust(20)
print text.rjust(20)
print text.center(20)
print text.rjust(20, '=')
print text.center(20, '*')
# Use format() function to easily align things >^<
ali_text1 = format(text, '>20')  # left
ali_text2 = format(text, '<20')  # right
ali_text3 = format(text, '^20')  # center
print ali_text1
print ali_text2
print ali_text3
