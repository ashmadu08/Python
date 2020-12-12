ict = 1000
maths = 1100
science = 1110
english = 1111
sinhala = 1010
buddhism = 1101
commerce = 1001
literature = 1111
history = 1011

subject = int(input("Subject code - "))

if ict == subject:
    sub = ("ICT")
elif maths == subject:
    sub = ("Mathematics")
elif science == subject:
    sub = ("Science")
elif english == subject:
    sub = ("English")
elif sinhala == subject:
    sub = ("Sinhala")
elif buddhism == subject:
    sub = ("Buddhism")
elif commerce == subject:
    sub = ("Commerce")
elif literature == subject:
    sub = ("Literature")
elif history == subject:
    sub = ("History")
print (sub)


marks = int(input(str("Marks - ")))
if marks >= 75:
 result = "A"
 print (result)
elif marks >= 65:
 result = "B"
elif marks >= 55:
 result = "C"
elif marks >= 35:
 result = "S"
else:
 result = "W"
print (result)
