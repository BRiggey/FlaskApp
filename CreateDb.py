import sqlite3

from flask import Flask, render_template
from flask import request, redirect, url_for

conn = sqlite3.connect("celebrities.db")
cursor = conn.cursor()
# Creating both tables
sql1 = ('''create table celebs(celebID integer PRIMARY KEY, 
firstname text, lastname text, age integer, email text, photo text, bio text)''')
cursor.execute(sql1)
sql2 = ('''create table members(memberID integer PRIMARY KEY, firstname text, 
       lastname text, age integer, email text, bio text)''')
cursor.execute(sql2)
sql5 = '''create table member_login(memberID integer PRIMARY KEY, username text, password text)'''
cursor.execute(sql5)
sql3 = "insert into celebs values(?,?,?,?,?,?,?)"
data = ((1, "Angelina", "Jolie", 40, "angie@hollywood.us", "https://s3.amazonaws.com/isat3402021/aj.jpg",
         "Angelina Jolie is an American actress, filmmaker and humanitarian. The recipient of "
         "numerous accolades, including an Academy Award and three Golden Globe Awards, she has been named Hollywood's "
         "highest-paid actress multiple times."),
        (2, "Brad", "Pitt", 51, "brad@hollywood.us", "https://s3.amazonaws.com/isat3402021/bp.jpg",
         "William Bradley Pitt (born December 18, 1963) is an American actor and film producer. "
         "He is the recipient of various accolades, including two Academy "
         "Awards, two British Academy Film Awards, two Golden Globe Awards, "
         "and a Primetime Emmy Award. As a public figure, Pitt has been "
         "cited as one of the most powerful and influential people in the "
         "American entertainment industry."),
        (3, "Snow", "White", 21, "sw@disney.org", "https://s3.amazonaws.com/isat3402021/sw.jpg",
         "Snow White is a princess of noble birth who is forced into servitude by her jealous stepmother, "
         "the Queen. She is very pure hearted, innocent, and a bit naïve, but she never loses faith that one "
         "day her wish for true love will someday come and take her away."),
        (4, "Darth", "Vader", 29, "dv@darkside.me", "https://s3.amazonaws.com/isat3402021/dv.jpg",
         "Before he became a disciple of the dark side, Darth Vader was Anakin Skywalker, "
         "a goodhearted Jedi and hero of the Clone Wars. While he was considered one of the most powerful "
         "Jedi in the galaxy, Anakin had broken the Order's code by secretly marrying Senator Padmé Amidala"),
        (5, "Taylor", "Swift", 25, "ts@1989.us", "https://s3.amazonaws.com/isat3402021/ts.jpg",
         "Taylor Alison Swift (born December 13, 1989) is an American singer-songwriter. "
         "Recognized for her songwriting, musical versatility, artistic reinventions, "
         "and influence on the music industry, she is a prominent cultural figure of the 21st century."),
        (6, "Beyonce", "Knowles", 34, "beyonce@jayz.me", "https://s3.amazonaws.com/isat3402021/bk.jpg",
         "Beyoncé Giselle Knowles-Carter born September 4, 1981 is an American singer, songwriter and businesswoman. "
         "Known as Queen Bey, she has been recognized for her boundary-pushing artistry, vocals, and performances."
         " Named one of the greatest singers of all time by Rolling Stone, her contributions to music and visual media"
         " and her concert performances have led her to become a prominent cultural icon of the 21st century."),
        (7, "Selena", "Gomez", 23, "selena@hollywood.us", "https://s3.amazonaws.com/isat3402021/sg.jpg",
         "Selena Marie Gomez born July 22, 1992) is an American singer, songwriter, actress, businesswoman and "
         "producer. She has won numerous accolades, including an American Music Award, a Billboard Music "
         "Award, two MTV Video Music Awards, broke 16 Guinness World Records, and received nominations for two "
         "Grammy Awards, a Golden Globe Award, and four Emmy Awards. One of the most influential people on social "
         "media, Gomez is the most-followed woman on Instagram and one of the most-followed people on Twitter. "
         "She was included in the Time 100 in 2020, and was named Billboard's Woman of the Year in 2017."),
        (8, "Stephen", "Curry", 27, "steph@golden.bb", "https://s3.amazonaws.com/isat3402021/sc.jpg",
         "Wardell Stephen Curry IIborn March 14, 1988)[1] is an American professional basketball player for "
         "the Golden State Warriors of the National Basketball Association (NBA). Widely regarded as the greatest "
         "shooter and one of the greatest players of all time, Curry is credited with revolutionizing the sport "
         "by inspiring teams and players to take more three-point shots.[2][3][4][5] He is a four-time NBA champion, "
         "a two-time NBA Most Valuable Player (MVP), an NBA Finals MVP, an NBA All-Star Game MVP, a nine-time NBA "
         "All-Star, and a nine-time All-NBA selection, including four times on the first team.")
        )
cursor.executemany(sql3, data)

sql4 = "insert into members values(?,?,?,?,?,?)"
data = ((2, "Evan", "Cooper", 19, "ercooper510@gmail.com", "I am a sophomore in ISAT from Montpelier, VA"), (1, "Brian",21, "La Rosa", "briggey21@gmail.com", "I am a Junior in ISAT from Richmond, VA"))
cursor.executemany(sql4, data)
sql6 = "insert into member_login values(?,?,?)"
data2 = ((1, "brian", "riggey"), (2, "evan", "cooper"))
cursor.executemany(sql6, data2)
conn.commit()
conn.close()
