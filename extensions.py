def main():
    file_name = input("File Name: ")
    answer = sorter(file_name)
    print (answer)

def sorter(core):
    clean = core.strip()
    if clean.endswith(".gif"):
        return "image/gif"
    elif clean.endswith(".jpg"):
        return "image/jpeg"
    elif clean.endswith(".png"):
        return "image/png"
    elif clean.endswith(".pdf"):
        return "application/pdf"
    elif clean.endswith(".txt"):
        return "text/plain"
    elif clean.endswith(".zip"):
        return "ZIP archive"
    else: 
        return "application/octet-stream"
    
main()