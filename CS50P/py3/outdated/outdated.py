months = {
    "January" : 1,
    "February" : 2,
    "March" : 3,
    "April" : 4,
    "May" : 5,
    "June" : 6,
    "July" : 7,
    "August" : 8,
    "September" : 9,
    "October" : 10,
    "November" : 11,
    "December" : 12
}

while True:

    date = input("Date: ").strip()
    try:
        month, day, year = date.split("/")
    try ValueError:
        x, year = date.split(", ")
        m, day = x.split(" ")
        m = m.title()
        month = months[m]
    except:
        return 1
    break

if int(month) < 10:
    month = "0" + str(month)
if int(day) < 10:
    day = "0" + str(day)

print(f"{year}-{month}-{day}")
