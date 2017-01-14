f = open('emails.csv','wb')
writer = csv.writer(f)
for r in faculty_email:
    writer.writerow([r])
f.close()
