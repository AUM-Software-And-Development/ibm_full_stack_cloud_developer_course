#Create the dictionary

print("\nDictionaries:\n")
Dict = {"key1":1,"key2":"2","key3":[3,3,3],"key4":(4,4,4),('key5'):5,(0,1):6}
print(Dict)
print("key1:", Dict["key1"])
print("(0,1)", Dict[(0,1)]) #key6

release_year_dict = {"Thriller": "1982", "Back in Black": "1980", \
                    "The Dark Side of the Moon": "1973", "The Bodyguard": "1992", \
                    "Bat Out of Hell": "1977", "Their Greatest Hits (1971-1975)": "1976", \
                    "Saturday Night Fever": "1977", "Rumours": "1977"}
print('release year dict', release_year_dict)
print('Thriller value:', release_year_dict["Thriller"])
print('The Bodyguard value:', release_year_dict["The Bodyguard"])

print('release year keys:', release_year_dict.keys())
print('release year values:', release_year_dict.values())

print('Adding to the dictionary')
release_year_dict['Graduation'] = '2007'
print(release_year_dict)

print("key validation (does 'The Bodyguard' exist in this dictionary?')\n")
print('The Bodyguard' in release_year_dict)