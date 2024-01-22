# Input a Python list of student heights
student_heights = input().split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆
#   total height = 857
# number of students = 5
# average height = 171
# Write your code below this row 👇
sum_height1=0
count=0
for student_height in student_heights:
  sum_height1+=student_height

for student_count in student_heights:
  count+=1

average_height=round(sum_height1/count)

print(f"total height = {sum_height1}")
print(f"number of students = {count}")
print(f"average height = {average_height}")
  