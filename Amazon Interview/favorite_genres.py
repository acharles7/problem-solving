
def getUserGenre(userSongs, songGenres):
    output = {}
    reverse_song = {}

    for genre in songGenres:
        for song in songGenres[genre]:
            reverse_song[song] = genre

    for user in userSongs:
        if len(userSongs[user]) >= 1:
            userGenres = []
            for song in userSongs[user]:
                if song in reverse_song.keys():
                    userGenres.append(reverse_song[song])
            output[user] = userGenres
        else:
            output[user] = []
    return output

def findGenres(userSongs, songGenres):
    favoriteGenre = {user: [] for user in userSongs}

    userGenre = getUserGenre(userSongs, songGenres)
    for user in userGenre:
        if len(userGenre[user]) >= 1:
            temp = {}
            count_genre = []
            for genre in userGenre[user]:
                if genre not in temp:
                    temp[genre] = 1
                else:
                    temp[genre] += 1

            maxGenre = max(temp.values())
            for key in temp:
                if temp[key] == maxGenre:
                    favoriteGenre[user].append(key)
    return favoriteGenre


userSongs = {
   "David": ["song1", "song7"],
   "Emma":  ["song7"]
}
songGenres = {
   "Rock":    ["song1", "song3"],
   "Dubstep": ["song7"],
   "Techno":  ["song2", "song4"],
   "Pop":     ["song5", "song6"],
   "Jazz":    ["song8", "song9"]
}
print(findGenres(userSongs, songGenres))
