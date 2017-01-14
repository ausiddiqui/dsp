import csv
f = open('faculty.csv')
rows = csv.reader(f)

faculty_name = []
faculty_degree = []
faculty_title = []
faculty_email = []

for row in rows:
    if row[0] != 'name':
        faculty_name.append(row[0])
        faculty_degree.append(row[1].strip())
        faculty_title.append(row[2])
        faculty_email.append(row[3])

#### Q1. Find how many different degrees there are, and their frequencies: Ex:  PhD, ScD, MD, MPH, BSEd, MS, JD, etc.
#### ------------------------------
faculty_degree_unique = list(set((faculty_degree)))
for l in [d.split() for d in faculty_degree_unique]:
    fd_temp += l

fd_unique = list(set((fd_temp)))
print sorted(fd_unique)

import re

counts = [0] * 9
labels = ['No Data', 'B.S.Ed.', 'JD', 'MS', 'MA', 'MD', 'MPH', 'PhD', 'ScD']
regex = [r"0",r"Ed",r"JD",r"M\.?S",r"MA",r"MD",r"MPH",r"Ph\.?D",r"Sc\.?D"]

for fd in faculty_degree:
    for i, r in enumerate(regex):
        if re.search(r,fd):
            counts[i] += 1

for i, c in enumerate(counts):
    print labels[i] + ": " + str(c)

#### Q2. Find how many different titles there are, and their frequencies:  Ex:  Assistant Professor, Professor
#### ------------------------------

ft_unique = list(set(faculty_title))

counts_ft = [0] * 3
labels_ft = [ft_unique[0], ft_unique[3], ft_unique[1]]
regex_ft = [r"Assistant", r"Associate", r"^Professor"]

for ft in faculty_title:
    for i, r in enumerate(regex_ft):
        if re.search(r,ft):
            counts_ft[i] += 1

for i, c in enumerate(counts_ft):
    print labels_ft[i] + ": " + str(c)

#### Q3. Search for email addresses and put them in a list.  Print the list of email addresses.
#### ------------------------------

#### Please note that the emails were already read into a list when reading the original CSV (see for loop at very top)
print faculty_email

#### Q4. Find how many different email domains there are (Ex:  mail.med.upenn.edu, upenn.edu, email.chop.edu, etc.).  Print the list of unique email domains.
#### ------------------------------

faculty_domains = set()
for fe in faculty_email:
    if fe[fe.find("@")+1:] not in faculty_domains:
        faculty_domains.add(fe[fe.find("@")+1:])
print faculty_domains
