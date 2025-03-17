#counting word frequency in a sentence
# sentence="this is a simple sentence and this sentence is just a simple"
# word_count={}
# for word in sentence.split():
#     word_count[word]=word_count.get(word,0)+1
# print(word_count)


#Student marks management   
# Students={
#     "Alice":{"math":85,"science":92,"english":88},
#     "Bob":{"math":78,"science":80,"english":75},
#     "Charlie":{"math":90,"science":85,"english":95}
# }
# for student, subject in Students.items():
#     print(f"{student}:{subject}")


# #Phonebook program
# while True:
#     phonebook={
#         "John":"123-456-7890",
#         "Alice":"987-654-3210",
#         "Bob":"555-555-5555"
#     }
#     phonebook["Charlie"]="444-444-4444"
#     name=input("Enter name of search: ")
#     print(f"Phone number:{phonebook.get(name,'Not found')} ")


#reverse key value:
# original_dict={"a":1,"b":2,"c":3}
# reversed_dict={v:k for k, v in original_dict.items()}
# print(reversed_dict)


# #merging tow dictionary
# dict1={"a":1,"b":2}
# dict2={"c":3,"d":4}
# mer_dict={**dict1,**dict2}
# print(mer_dict)
# dict1.update(dict2)
# print(dict1)


#most frequent number
# number=[1,2,3,4,5,2,3,5,2,2]
# frequency={}
# for num in number:
#     frequency[num]=frequency.get(num,0)+1
# most_frequent=max(frequency,key=frequency.get)
# print(f"Most frequent number: {most_frequent} (appears {frequency[most_frequent]} times)")    


# documents={
#     "doc1":"Python is great",
#     "doc2":"Python and Java are popular",
#     "doc3":"I love coding in python"
# }
# inverted_index={}
# for doc, text in documents.items():
#     for word in text.split():
#         word=word.lower()
#         if word not in inverted_index:
#             inverted_index[word]=[]
#         inverted_index[word].append(doc)
# print(inverted_index)      


# dict1={"a": 1,"b": 2, "c": 3}
# dict2={"a": 1,"b": 2, "c": 3}
# dict3={"a": 1,"b": 2, "c": 4}
# print(dict1==dict2)
# print(dict1==dict3)


# data={"apple":3,"banana":1,"cherry":2}
# sorted_data=dict(sorted(data.items(),key=lambda item:item[1]))
# print(sorted_data)


# keys=["name","age","city"]
# values=["Alice",25,"New York"]
# person=dict(zip(keys,values))
# print(person)


# #finding the key with the maximum value
# scores={"Alice":89,"Bob":92,"Charlie":85}
# top_scorer=max(scores,key=scores.get)
# print(f"Top Scorer: {top_scorer} with {scores[top_scorer]} points")



# data={"name":"Alice","age":25,"city":"New York"}
# data.pop("age")
# print(data)


# # #counting character frequency in a string
# text="hello world"
# char_count={}
# for char in text:
#     char_count[char]=char_count.get(char,0)+1
# print(char_count)


#creating a dictionary form user input 
# n = int(input("Enter number of elements: "))
# user_dict={}
# for _ in range(n):
#     key=input("Enter key: ")
#     value=input("Enter value: ")
#     user_dict[key]=value
# print("Your dictionary: ",user_dict)


