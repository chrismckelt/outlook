import pandas as pd
import re
import re
import spacy
import os


def get_phone_numbers(string):
    r = re.compile(
        r'(\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4})')
    phone_numbers = r.findall(string)
    return [re.sub(r'\D', '', num) for num in phone_numbers]


def get_email_addresses(string):
    r = re.compile(r'[\w\.-]+@[\w\.-]+')
    return r.findall(string)


class Data:
    def __init__(self, label, value):
        self.label = label
        self.value = value


# Load English tokenizer, tagger, parser and NER
nlp = spacy.load("en_core_web_sm")
nlp.max_length = 3531630
file_name = 'C:/dev/outlook/outlook-insight-2022-nov.CSV'
isFile = os.path.isfile(file_name)
if not isFile:
    raise "File not found"
lines = ""
list = []

print(f'File Size is {os.stat(file_name).st_size / (1024 * 1024)} MB')

with open(file_name, encoding="utf8") as file:
    for i in range(100000):
        line = next(file).strip()
        lines = lines + line

doc = nlp(lines)

for token in doc:
    #     #print(token.text, token.lemma_, token.pos_, token.tag_, token.dep_, token.shape_, token.is_alpha, token.is_stop)
    emails = get_email_addresses(token.text)
    for email in emails:
        if len(email) > 0:
            d = Data("EMAIL", email)
            if not email in list:
                list.append(d)

df = pd.DataFrame(["", ""])

for entity in doc.ents:
    # print(entity.text, entity.label_)
    # print(entity.label_, entity.text, entity.text)
    # dict.update( [(entity.label_),(entity.text)] )
    d = Data(entity.label_, entity.text)
    list.append(d)

# df = pd.DataFrame.from_dict(dict,)

print(len(list))
filtered = [e for e in list if e.label == 'EMAIL']
df = pd.DataFrame([t.__dict__ for t in filtered])

output_file = 'C:/dev/outlook/output-nov.CSV'
if (file_name.__contains__("dec")):
    output_file = 'C:/dev/outlook/output-dec.CSV'

df.to_csv(output_file)

emails = pd.read_csv(output_file)
