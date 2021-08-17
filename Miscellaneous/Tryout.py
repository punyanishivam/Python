def MultipleBrackets(str):
  
  l = []
  bracket_count = 0
  matched_count = 0

  for i in str:
    if i == "(" or i == "{" or i == "]":
      bracket_count += 1
      s.append(i)
    
    if i == ")":
      if l[-1] == "(":
        l.pop(-1)
    if i == "}":
      if l[-1] == "{":
        l.pop(-1)
    if i == "]":
      if l[-1] == "[":
        l.pop(-1)

    if l == []:
      matched_count = 1


  return matched_count, bracket_count

print(MultipleBrackets("(c([od]er)) b(yt[e])"))