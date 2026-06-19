contact_list =[
    "Tunde   ",
    "Tolu    ",
    "Tobi  ",
    "CHISOM",
    "chisom",
    "tunde  ",
    "ADEBAYO",
    "adebayo",
    "ChRistian  ",
    "CHRISTIAN",
    "KING         ",
    "king ",
    "kinG   ",
    "QUEEN  ",
]
print(f"Former contact list is {contact_list}")
def count_words_in_list(word_list, particular_word):
    count = 0
    for word in word_list:
        if word == particular_word:
            count += 1
    return count

new_contact_list = []
#This for loop goes to each of the elements in the contact list, removes the extra spaces and capitalizes the first letter of each name, then adds it to a new list
for contact in contact_list:
    new_contact_list.append(contact.strip().capitalize())
print("===UNIQUE CONTACTS DETECTED===")
unique_contacts = set(new_contact_list)
print(unique_contacts)
#print(new_contact_list)
for i in range(len(unique_contacts)):
    contact = list(unique_contacts)[i]
    count = count_words_in_list(new_contact_list, contact)
    if count > 1:
        print(f"The contact {contact} duplicates itself : {count} times")
    else:
        print(f"The contact {contact} is unique and appears only once")
   