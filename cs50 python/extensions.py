f_name = input("File name: ").strip().lower()
words = f_name.split(".")
extension = words[1]

if words[1] == "gif":
    print("image/gif")

elif words[1] == "jpg" or words[1] == "jpeg":
    print("image/jpeg")

elif words[1] == "png":
    print("image/png")

elif words[1] == "pdf":
    print("application/pdf")

elif words[1] == "txt":
    print("text/plain")

elif words[1] == "zip":
    print("application/zip")

else:
    print("application/octet-stream")

