str1="https://database.com/user/augustom,AugUSto Martin, 23, Approved,,"
str2="https://database.com/user/juliasch,JuLIA SchmidT, 67, rejected,,"
str3="https://database.com/user/kmarx,Karl Marx, 42, rejected,,"

print(f'message:  {str1[26:].rstrip(',,').replace(" ","").lower()}')
print(50*"#")

print(f'message:  {str2[26:].rstrip(',,').replace(" ","").lower()}')
print(50*"#")

print(f'message:  {str3[26:].rstrip(',,').replace(" ","").lower()}')
print(50*"#")
