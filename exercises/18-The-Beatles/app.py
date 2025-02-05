# ✅↓ Write your code here ↓✅

def sing():
    lyrics=""
    for i in range (1,12):
        if i == 5:
            lyrics +="there will be an answer,\n"
            #print(lyrics)
        elif i == 11:
            lyrics +="whisper words of wisdom, let it be"
            #print(lyrics)
        else:
            lyrics +="let it be,\n"
            #print(lyrics)
    return lyrics

sing()

