from pytube import YouTube, streams

yt = input("Enter The Link Of Video : ")

url = YouTube(yt)

print("Title :",url.title)
print("Description :",url.description)
print("Views on Video :",url.views)
print("Length of Video :",url.length)
print("Ratings :",url.rating)
stream = url.streams.first()
stream.download()