# My big apology
# I will proceed in earnest starting next week.

# 백준 #4949

from sys import stdin

string = stdin.readline().rstrip()
# 입력이 제대로 안 받아짐. 왜 그러지

stack = []

for c in string:
  if c == '(' or c == ')' or c == '[' or c == ']':
    if len(stack) == 0:
      stack.append(c)
    else:
      if (stack[-1] == '(' and  c == ')' ) or (stack[-1] == '[' and  c == ']' ):
        stack.pop()
      else:
        stack.append(c)

if len(stack) == 0:
  print('yes')
else:
  print('no')
