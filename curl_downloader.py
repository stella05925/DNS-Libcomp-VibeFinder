import os

def check_file_exist(input):
    return os.path.isfile(input)

def curl_download(input, url):
    combined_express = f'curl -o "{input}" "{url}"'
    reporter = os.system(combined_express)
    if not reporter:
        return check_file_exist(input)
    else:
        return False
