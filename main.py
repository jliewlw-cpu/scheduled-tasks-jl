# To run and test the code you need to update 4 places:
# 1. Change MY_EMAIL/MY_PASSWORD to your own details.
# 2. Go to your email provider and make it allow less secure apps.
# 3. Update the SMTP ADDRESS to match your email provider.
# 4. Update birthdays.csv to contain today's month and day.
# See the solution video in the 100 Days of Python Course for explainations.


from datetime import datetime
import pandas
import random
import smtplib
import os

# import os and use it to get the Github repository secrets
MY_EMAIL = os.environ.get("MY_EMAIL")
MY_PASSWORD = os.environ.get("MY_PASSWORD")

now = dt.datetime.today()
today_day = now.day
today_month = now.month
today = (today_month,today_day)

df = pandas.read_csv("birthdays.csv")
df = df.dropna()
df["year"] = df["year"].astype(int)
df["month"] = df["month"].astype(int)
df["day"] = df["day"].astype(int)

birthdays_dict = {
    (row["month"], row["day"]): row
    for (_, row) in df.iterrows()
}

if today in birthdays_dict:
    person = birthdays_dict[today]
    person_name = person["name"]
    person_email = person["email"]
    send_email = True

    random_letter_template = random.choice(["letter_1.txt","letter_2.txt","letter_3.txt"])

    with open(f"letter_templates/{random_letter_template}","r") as f:
        letter = f.read()
        customized_letter = letter.replace("[NAME]",person_name)

    with smtplib.SMTP("smtp.gmail.com",port=587) as connection:
        #make connection secure
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=my_email,
            msg=f"Subject:Happy Birthday\n\n{customized_letter}"
        )
