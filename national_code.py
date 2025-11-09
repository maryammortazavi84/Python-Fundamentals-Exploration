people = []
for i in range(30):
    person = {
        "national_code" : i,
        "name" : f'person {i}',
        "last_name" : f'person {i} last name',
        "information" : {
            "loc" : f'city {i}',
            "bla bla bla" : None
        },
    }
    people.append(person)
 
codes = [1 , 2 , 5 , 15 ]
for code in codes:
    for person in people:
        if person["national_code"] == code:
            person["name"] = "##########"
print(people)