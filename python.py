import gofile  as go
  
def store_file(file):
    cur_server = go.getServer()
    print("Server :",cur_server)
    url = go.uploadFile(file)
    print("\n\n\t\t\bFile shared Sucessfully\n\n\t\t")
    print("Here is Download Link : ", url["downloadPage"])

filepath = input("Enter the file path")
print("\n\n\t\tGenerating Downlaod link \n \n\n\t\tPlease wait")

store_file(filepath)
