def read(file):
    file = (open(file))
    content = file.read()
    file.close()
    return content