student_id = int(input("Student ID - "))
house_no = student_id % 4
print (house_no)
if house_no == 0:
    house = "Gamunu"
elif house_no == 1:
    house = "Thissa"
elif house_no == 2:
    house = "Vijaya"
elif house_no == 3:
    house = "Parakum"
print (house)
