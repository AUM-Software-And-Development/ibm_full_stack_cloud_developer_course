#Create a set

set1={"pop","punk","soul","hard rock", "rock", "r&b", "rock", "disco"}
print (set1)

#instantiate a set from a list

album_list = [ "Michael Jackson", "Thriller", 1982, "00:42:19", \
              "Pop, Rock, R&B", 46.0, 65, "30-Nov-82", None, 10.0]
album_set = set (album_list)
print ("set",album_set)
print ("list",album_list)

music_genres = set (["pop", "pop", "rock", "folk rock", "hard rock", "soul", \
                    "progressive rock", "soft rock", "R&B", "disco"])
print ("\n genres of music:",music_genres)

A = set (["Thriller", "Back in Black", "AC/DC"])
print (A)
A.add ("NSYNC")
print ("Adding an item to the set:",A)
A.add ("NSYNC")
print ("Adding the same item to the set again:",A)
A.remove("NSYNC")
print ("Removing the same item from the set:",A)
print ("Check if 'AC/DC' in A:\n")
print ("AC/DC" in A)

#Set ops
print ("Sets for set operations:\n")
album_set1 = set (["Thriller", 'AC/DC', 'Back in Black'])
album_set2 = set ([ "AC/DC", "Back in Black", "The Dark Side of the Moon"])

print (album_set1, album_set2)

#intersection
intersection = album_set1 & album_set2
print ("The intersection of sets is:",intersection)
print ("Method2:", album_set1.intersection (album_set2))

#difference
print ("The difference in sets using set1 is:",album_set1.difference(album_set2))
print ("The difference in sets using set2 is:",album_set2.difference(album_set1))

#union
print("Union:",album_set1.union(album_set2))

#superset
print("Is set 1 a superset to set 2?:",(album_set1).issuperset(album_set2))

#subset
print("Is set 1 a subset to set 2?:",(album_set1).issubset(album_set2))