import pandas as pd
import re
import re
import spacy
import os
import numpy

nov_file = 'C:/dev/outlook/output-nov.CSV'
dec_file = 'C:/dev/outlook/output-nov.CSV'

df = pd.read_csv(nov_file)
df2 = pd.read_csv(dec_file)

df = df.merge(df2)
emails = df['value'].str.lower().unique()
print(emails)

output_file = 'C:/dev/outlook/emails.CSV'
numpy.savetxt(output_file, emails, fmt='%s')
