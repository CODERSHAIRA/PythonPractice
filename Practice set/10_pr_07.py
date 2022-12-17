def remove_and_split(string,word):
  newStr=string.replace(word,"")
  return newStr.strip()

this="      Dora where are you going??"

print(remove_and_split(this,"Dora"))
print(this)
print(this.strip())
