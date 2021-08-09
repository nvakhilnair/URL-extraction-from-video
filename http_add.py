def add_http(output):
    url = []
    for i in output:
        if(i[0:4] != 'http'):
            new_str = 'http://' + i
            url.append(new_str)
        else:
            url.append(i)
    return url