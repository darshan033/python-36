input_line = input("Enter five numbers seperated by space:")
number_string_list = input_line.split()
sum=0
for i in number_string_list:
    sum=sum+int(i)
    print(sum)

