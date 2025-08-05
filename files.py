import os


var = os.listdir("C:/Users/ilyass/Downloads/EST")
for i in var:
  name, extension = os.path.splitext(i)
  if extension == ".pdf":
    source = os.path.join("C:/Users/ilyass/Downloads/EST", i)
    destination = os.path.join("C:/Users/ilyass/Downloads/EST/pdf",i)

    os.rename(source, destination)