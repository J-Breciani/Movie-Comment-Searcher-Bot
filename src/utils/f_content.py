from files.read_txt import get_content

def organize_content():
    content_list = []
    for line in get_content():
        content_list.append(line.strp())
    return content_list