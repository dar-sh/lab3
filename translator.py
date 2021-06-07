user_input = input("Input text to translate to pig latin: ")
print("User Text: ", user_input)

updated_user_input = user_input.split(' ')

for j in updated_user_input:
 if len(j) >= 3: 
  j = j + "%say" % (j[0]) 
  j = j[1:]
  print(j)
 else:
  pass
