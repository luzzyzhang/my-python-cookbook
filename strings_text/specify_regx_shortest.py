# regx * greedy, ? nogreedy
import re
str_pat = re.compile(r'\"(.*)\"')
text1 = 'ZOOM on shit "no."'
print str_pat.findall(text1)
text2 = 'ZOOM on shit "yes." luzzyzhang and linpuzhao "no."'
print str_pat.findall(text2)
print 50*'*'
str_pat2 = re.compile(r'\"(.*?)\"')
print str_pat2.findall(text2)
