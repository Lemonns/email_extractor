import json
import re
import csv


def format_file(file_name: str):
    f = open(file_name, encoding="utf8")
    return json.load(f)

json_file = format_file('file.json')

def clean_json(data_set):
    raw_arr = list()
    for i in range(len(data_set[0]["organicResults"])):
        raw_arr.append(data_set[0]["organicResults"][i]["description"])
    return raw_arr

def extract_emails(texts):
    emails = set()
    email_regex = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    for text in texts:
        matches = re.findall(email_regex, text)
        emails.update(matches)
    return emails

def save_emails_to_csv(emails, file_name):
    with open(file_name, 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for email in emails:
            writer.writerow([email])

block = clean_json(json_file)
email_set = extract_emails(block)
save_emails_to_csv(email_set, 'email_list.txt')
