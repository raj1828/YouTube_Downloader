from pytube import YouTube
try:
    url = input("Enter The YouTube Link : ")
    yt = YouTube(url)
except Exception as e:
    print("You entered wrong link :( ",e)


vid_name = yt.title

print("Title :",yt.title)
print("\n")
print("Description :",yt.description)
print("\n")
print("Views on Video :",yt.views)
print("\n")
print("Length of Video :",yt.length)
print("\n")
print("Ratings :",yt.rating)
print("\n")

choice = input("Do you want to download this video (yes/no) : ").lower()
try:
    if choice == "yes":
        print("Downloading!!!!!!!!")
        yt.streams.filter(progressive = True, file_extension = "mp4").first().download(output_path = "E:\YouTube\Download")
        print("Download Completed")
    elif choice == "no":
        print("ThankQ!!!")
    else:
        print("Invalid Choice")
    print("ThankQ For Using This App :) ")
except Exception as e:
    print("You have enterd Wrong : ",e)





