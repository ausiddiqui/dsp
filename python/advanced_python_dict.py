#### Q6.  Create a dictionary in the below format:
#### ------------------------------

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
f.close()

faculty_dict = {}

def degree_modify(degrees):
    import re

    labels_fd = ['M.S.', 'Ph.D.', 'Sc.D.']
    regex_fd = [r"MS",r"Ph[\.]?D[\.]?",r"Sc[\.]?D[\.]?"]
    degree_mod = []

    for fd in degrees:
        fd_new = re.sub(regex_fd[0],labels_fd[0],fd)
        fd_new = re.sub(regex_fd[1],labels_fd[1],fd_new)
        fd_new = re.sub(regex_fd[2],labels_fd[2],fd_new)
        degree_mod.append(fd_new)

    return degree_mod

faculty_degree_mod = degree_modify(faculty_degree)

for i, name in enumerate(faculty_name):
    lname = name[name.rfind(" ") + 1:]
    if lname in faculty_dict:
        faculty_dict[lname].append([faculty_degree_mod[i], faculty_title[i][:faculty_title[i].rfind("r")+1], faculty_email[i]])
    else:
        faculty_dict[lname] = [[faculty_degree_mod[i], faculty_title[i][:faculty_title[i].rfind("r")+1], faculty_email[i]]]

print {k: faculty_dict[k] for k in faculty_dict.keys()[:3]}


#### Q7.  The previous dictionary does not have the best design for keys.  Create a new dictionary with keys as:
#### ------------------------------

professor_dict = {}

for i, name in enumerate(faculty_name):
    name_t = (name[:name.find(" ")], name[name.rfind(" ") + 1:])

    professor_dict[name_t] = [faculty_degree_mod[i], faculty_title[i][:faculty_title[i].rfind("r")+1], faculty_email[i]]

print {k: professor_dict[k] for k in professor_dict.keys()[:3]}

#### Q8.  It looks like the current dictionary is printing by first name.  Print out the dictionary key value pairs based on alphabetical orders of the last name of the professors
#### ------------------------------

key_sort = sorted(professor_dict, key=lambda x: x[1])

for k in key_sort:
    print k, ":", professor_dict[k]
