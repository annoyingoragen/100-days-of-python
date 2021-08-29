import datetime
import pandas
import smtplib

date = datetime.datetime.now()
month = date.month
day = date.day

date_of_births = pandas.read_csv("birthdays.csv")
date_of_births_dict = date_of_births.to_dict(orient="records")

for index in date_of_births_dict:
    for value, data in index.items():
        if index["month"] == month and index["day"] == day:
            receiver_email = index["email"]
            name = index["name"]

            with open("letter_templates/letter_1.txt", mode="r") as birthday_template:
                data = birthday_template.readlines()

            greeting_line = data[0].replace("[NAME]", name)
            data[0] = greeting_line
            birthday_wish = list()
            for line in data:
                birthday_wish.append(line.strip("\n"))
            final_message = str()
            for line in birthday_wish:
                final_message += line
                final_message += "\n"
            # print(finalmessage)

            my_email, password = "bibliophilemuffie@gmail.com", "0306872174182325"
            connect = smtplib.SMTP("smtp.gmail.com", port=587)

            connect.starttls()

            connect.login(user=my_email, password=password)
            connect.sendmail(from_addr=my_email,
                             to_addrs=receiver_email,
                             msg=f"Subject:Hello\n\n{final_message}")
            connect.close()
            break
