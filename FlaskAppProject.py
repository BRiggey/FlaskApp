_author__ = 'Brian La Rosa', 'Evan Cooper'
#imports

import sqlite3

from flask import Flask, render_template
from flask import request, redirect, url_for
#instantiate
app = Flask(__name__)

#Creating the database
conn = sqlite3.connect("celebrities.db")
cursor = conn.cursor()
#Creating both tables
sql1 = ('''create table celebs(celebID integer PRIMARY KEY, 
firstname text, lastname text, age integer, email text, photo text, bio text)''')
cursor.execute(sql1)
sql2 = ('''create table members(memberID integer PRIMARY KEY, firstname text, 
       lastname text, age integer, email text, bio text)''')
cursor.execute(sql2)

sql3 = "insert into celebs values(?,?,?,?,?,?,?)"
data = ((1,"Angelina", "Jolie", 40, "angie@hollywood.us", "https://s3.amazonaws.com/isat3402021/aj.jpg",
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
data = (1, "Brian", "La Rosa", 21, "briggey21@gmail.com", "blah blah")
cursor.execute(sql4, data)
conn.commit()
conn.close()


# route for handling the login page logic
@app.route('/', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect(url_for('info'))
    return render_template('login.htm', error=error)
def info():
    memberID = None
    firstname = ''
    lastname = ''
    age = None
    email = ''
    bio = ''
    success = False

    if request.method == 'GET':
        conn = sqlite3.connect('celebrities.db')
        c = conn.cursor()
        c.execute('''SELECT * FROM members''')
        row = c.fetchone()
        print(row)
        if row:
            memberID = row[0]
            firstname = row[1]
            lastname = row[2]
            age = row[3]
            email = row[4]
            bio =  row[5]
        conn.close()
    if request.method == 'POST':
        memberID = request.form('memberID')
        firstname = request.form('firstname')
        lastname = request.form('lastname')
        age = request.form('age')
        email = request.form('email')
        bio = request.form('bio')
        success = True

        conn = sqlite3.connect('celebrities.db')
        c = conn.cursor()
        c.execute('''SELECT * FROM members''')
        row = c.fetchone()
        if row:
            c.execute('''UPDATE members SET firstname = ?, lastname = ?, 
            age = ?, email = ?, bio = ? WHERE memberID = ?''',
            (memberID, firstname, lastname, age, email, bio))
        else:
            c.execute('''INSERT INTO members VALUES (?, ?, ?, ?, ?, ?)''',
                      (memberID, firstname, lastname, age, email, bio))
        conn.commit()
        conn.close()
    return render_template('profile.htm', memberID = memberID, firstname = firstname,
                           lastname = lastname, age = age, email = email, bio =bio, success = success)











def get(request):
    pass

def post(request):
    pass

@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


if __name__ == "__main__":
    app.run(debug=False)


conn = sqlite3.connect("celebrities.db")
cursor = conn.cursor()

sql = "select * from celebs"
cursor.execute(sql)
rows = cursor.fetchall()

for row in rows:
    print(row)
conn.close()