def func(big_list):
    average=[]
    for dict in big_list:
        for key, value in dict.items():
            if key =='grades':
                average.append(f"{sum(value)/len(value):.1f}")
                value.sort()

        dict["average"]=average.pop()
    return big_list

        
students = [
    {'name': 'Alice', 'grades': [90, 85, 92]},
    {'name': 'Bob', 'grades': [70, 88, 80]},
    {'name': 'Charlie', 'grades': [95, 93, 97]}
]

output=func(students)
print(output)
