# sentence="this is a sample and this setence is just a simple"
# word_count={}
# for word in sentence.split():
#     word_count[word]=word_count.get(word,0)+1
# print(word_count)
   

# students={
#     "Alice":{"math":85, "Science": 92, "English":88},
#     "Bob":{"math":85, "Science": 92, "English":88},
#     "Charlie":{"math":85, "Science": 92, "English":88}
# }

# for student,subjects in students.items():
#     print(f"{student}:{subjects}")


# phonebook={
#     "Jhon":"123-456-7890",
#     "Alice":"987-654-3210",
#     "Bob":"555-555-5555"
# }
# phonebook["Charlie"]="444-444-4444"

# name=input("Enter the name:").title()
# print(f"Phone number:{phonebook.get(name,'Not found')}")


# sentence="This is a sample sentence and this sentence is just a sample"
# word_count={}
# for word in sentence.split():
#     word_count[word]=word_count.get(word,0)+1
# print(word_count)


# students={
#     "Alice":{"math":85,"science":92,"elglish":88},
#     "Bob":{"math":78,"science":80,"elglish":75},
#     "Charlie":{"math":90,"science":85,"elglish":95}
# }

# for student,subjects in students.items():
#     print(f"{student}:{subjects}")
#     for key,value in subjects.items():
#         print(f"{key}:{value}")


# phonebook={
#     "John":"123-456-7890",
#     "Alice":"987-654-3210",
#     "Bob":"555-555-5555"
# }
# phonebook["Charlie"]="444-444-4444"

# name=input("Enter name to search: ")
# print(f"Phone number: {phonebook.get(name,"Not found")}")


# original_dict={"a":1,"b":2,"c":3}
# reversed_dict={v:k for k,v in original_dict.items()}
# print(reversed_dict)


# numbers=[1,3,2,3,4,2,3.5,2,2]
# frequency={}
# for num in numbers:
#     frequency[num]=frequency.get(num,0)+1
#     most_frequent=max(frequency,key=frequency.get)
# print(f"Most frequent number: {most_frequent} (appears {frequency[most_frequent]} times)")


# data={"apple":3,"banana":1,"cherry":2}
# sorted_data=dict(sorted(data.items(),key=lambda item: item[1]))
# print(sorted_data)

# keys=["name","age","city"]
# values=["Alice",25,"New York"]
# person=dict(zip(keys,values))
# print(person)


scores={"Alice":89,"Bob":92, "Charlie":85}
top_score=max(scores,key=scores.get)
print(top_score)