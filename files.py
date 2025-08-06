import os


var = os.listdir("C:/Users/ilyass/Downloads/EST")
for i in var:
  name, extension = os.path.splitext(i)

  
  if extension in (".pdf", ".doc", ".docx", ".txt"):
    source = os.path.join("C:/Users/ilyass/Downloads/EST", i)
    destination = os.path.join("C:/Users/ilyass/Downloads/EST/pdf",i)

    os.rename(source, destination)

  elif extension in (".jpg", ".png", ".jpge", ".svg") :
    source = os.path.join("C:/Users/ilyass/Downloads/EST", i)
    destination = os.path.join("C:/Users/ilyass/Downloads/EST/img",i)

    os.rename(source, destination)

  elif extension in (".mp4", ".mkv", ".webm" ):
    source = os.path.join("C:/Users/ilyass/Downloads/EST", i)
    destination = os.path.join("C:/Users/ilyass/Downloads/EST/vid",i)

    os.rename(source, destination)

  elif extension in (".mp3", ".m4a", ".ogg" ):
    source = os.path.join("C:/Users/ilyass/Downloads/EST", i)
    destination = os.path.join("C:/Users/ilyass/Downloads/EST/audio",i)

    os.rename(source, destination)

  elif extension in (".zip", ".rar", ".7z", ".tar" ):
    source = os.path.join("C:/Users/ilyass/Downloads/EST", i)
    destination = os.path.join("C:/Users/ilyass/Downloads/EST/compresed",i)

    os.rename(source, destination)