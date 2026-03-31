#CAE

data = [[">=9","yes","Exel","Good","Fast","yes","pos"],
        [">=9","yes","Good","Good","Fast","yes","pos"],
        [">=8","no","Good","Good","Fast","no","neg"],
        [">=9","yes","Good","Good","Slow","no","pos"]]

print("Traininig data")
for row in data:
  print(row)

print("-"*30)
count = 1
attr_len = len(data[0]) -1
print(attr_len)
S = ['0']*attr_len
G = ['?']*attr_len
temp = []

print("Hypothesis")
print("S=",S)
print("G=",G)

print("-"*30)

for row in data:
  #positive instance
  if row[-1] == "pos":
    j = 0
    for col in row:
      if col!= "pos":
        if col!= S[j] and S[j] == '0':
          S[j] = col
        elif col!= S[j] and S[j] !='0':
          S[j] = '?'
        j += 1


    # remove inconsistent value in G
    for j in range(0,attr_len):
      for k in temp:
        if k[j] != S[j] and k[j]!= '?':
          temp.remove(k)



  #negative instance
  if row[-1] == "neg":
    j = 0
    for col in row:
      if col!= 'neg':
        if col!= S[j] and col!='?':
          G[j] = S[j]
          temp.append(G)
          G = ['?']*attr_len
        j +=1
  print("Iteration=",count)
  count += 1
  print("S=",S)
  if len(temp)==0:
    print("G=",G)
  else:
    print("G=",temp)
