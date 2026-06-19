#My favorite songs in real life

playlist = [
    ("Take Over",         "Theophilus Sunday", 389, "Gospel Worship"),
    ("Intensify",         "Theophilus Sunday", 816, "Gospel Worship"),
    ("Satan Has Lost It", "Theophilus Sunday", 209, "Gospel Worship"),
    ("To See You",        "Lawrence Oyor",     312, "Prophetic Worship"),
    ("We Will Be Many",   "Lawrence Oyor",     347, "Prophetic Worship"),
    ("Ga Shi Nan",        "Kaestrings",        423, "Contemporary Gospel"),
    ("Broken",            "Kaestrings",        285, "Contemporary Gospel"),
    ("I Offer My Life",   "Don Moen",          224, "Classic Worship"),
    ("Give Thanks",       "Don Moen",          207, "Classic Worship"),
    ("Thank You Lord",    "Don Moen",          359, "Classic Worship"),
]
#Initialization of total song seconds
Total = 0
for song in playlist:
    Total += song[2]   

#Hours minutes and seconds!
number_of_hours = Total // 3600
other_seconds = Total - (number_of_hours * 3600) 
number_of_minutes = other_seconds // 60
remaining_seconds = other_seconds -(60 * number_of_minutes)
print(f"Total duration of songs in the playlist is {number_of_hours}:{number_of_minutes}:{remaining_seconds} seconds")
unique_genres = [] #Storage of Unique Genres

for song in playlist:
    unique_genres.append(song[3])

unique_genres = set(unique_genres)


print(f"The unique genres are {unique_genres}")

#Machine for gospel time
gospel_time = []

for song in playlist:
    gospel_time.append(song[2])

# longest and shortest track
longest_track_time = max(gospel_time)
shortest_track_time = min(gospel_time)

for song in playlist:
    if song[2] == longest_track_time:
        print(f"The Longest track is {song[0]}")
    if song[2] == shortest_track_time:
        print(f"The Shortest track is {song[0]}")

#track beyond three minutes
for song in playlist:
    if song[2] > 180:
        print(f"{song[0]} is beyond 3 minutes")

artists = []
for song in playlist:
    artists.append(song[1])

print(artists)

#function to count the number of times a word appears in artist

def count_in_list(My_list, word_to_count):
    count = 0
    for word in My_list:
        if word == word_to_count:
            count += 1
    return count

#Calculate total songs for each artist
for artist in set(artists):
    print(f"{artist} appears {count_in_list(artists, artist)} songs")