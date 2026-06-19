"""Exercise 9 — Movie Night Negotiator
Topics: Sets · Lists · Conditions
You and two friends each have a list of 8 movies you actually want to watch.
Convert each to a set. Find: movies all three agree on, movies only you want,
movies only two people want (and which two), and the best "compromise pick"
ranked by most agreed-upon."""



My_movies = [
    "Inception", "Interstellar", "The Matrix", "Parasite",
    "Dune", "Everything Everywhere", "Oppenheimer", "Arrival"
]

First_friend_movies = [
    "Inception", "Interstellar", "The Dark Knight", "Parasite",
    "Dune", "Get Out", "Tenet", "Arrival"
]

Second_friend_movies = [
    "Inception", "The Godfather", "The Matrix", "Parasite",
    "Blade Runner 2049", "Everything Everywhere", "Tenet", "Arrival"
]

My_movies = set(My_movies)
First_friend_movies = set(First_friend_movies)
Second_friend_movies = set(Second_friend_movies)

Movies_all_three_agree_on = My_movies & First_friend_movies & Second_friend_movies
print(f"Movies all agree on are {Movies_all_three_agree_on}")
print(f"Movies only you want are {My_movies-First_friend_movies-Second_friend_movies}")
Movies_for_me_and_first_friend = My_movies & First_friend_movies
Movies_for_me_and_Second_friend = My_movies & Second_friend_movies
Movies_for_first_and_second_friend = First_friend_movies & Second_friend_movies

print(f"The movies that me and my first friend like are {Movies_for_me_and_first_friend}")
print(f"The movies that me and my second friend like are {Movies_for_me_and_Second_friend}")
print(f"The movies my first friend and my second friend like are {Movies_for_first_and_second_friend}")

Movies_all_three_agree_on = list(Movies_all_three_agree_on)
print(f"The best movies by rank are {Movies_all_three_agree_on[0]} followed by {Movies_all_three_agree_on[1]} then {Movies_all_three_agree_on[2]}")


