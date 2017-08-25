# Match span multiple lines
# Example match C-style comments
import re
comment = re.compile(r'/\*(.*?)\*/')
text1 = '/* This is a comment */'
text2 = '''/* This is a
           multiline comment */
        '''
print(comment.findall(text1))
print(50*'~')
print(comment.findall(text2))
print(50*'-')
# Fix use pattern (?:.|\n) specifies a noncaptrure group
comment2 = re.compile(r'/\*((?:.|\n)*?)\*/')
print comment2.findall(text2)
print 50*'~'
# re.compile() function accepts a flag re.DOTALL use here
# make . in a regex match all characters including newlines
# simple pattern work well complex regx not well
comment3 = re.compile(r'/\*(.*?)\*/', re.DOTALL)
print comment3.findall(text2)
