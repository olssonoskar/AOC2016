def read(file):
    file = (open(file))
    content = file.read()
    file.close()
    return content

def read_lines(file):
    content = read(file)
    return content.split("\n")