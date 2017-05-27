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
ali_text4 = format(text, '=>20s')  # fill character other than space
ali_text5 = format(text, '*^20s')
print ali_text1
print ali_text2
print ali_text3
print ali_text4
print ali_text5
# format multiple values
words = '{:>10s} {:<10s} {:^10s}'.format('Happy', 'Hack', 'Day')
print words
x = 1.2345
print format(x, '>10')
print format(x, '^10.2f')
