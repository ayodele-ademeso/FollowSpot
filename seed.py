"""Script to seed database"""

import os
import json
from datetime import datetime

import crud
import model
import server

os.system('dropdb followspot')
os.system('createdb followspot')

# os.system('source secrets.sh')

model.connect_to_db(server.app)
model.db.create_all()

########################################################################

jb = crud.create_user(first_name="Jen",
                      last_name="Brissman",
                      email="brissman514@gmail.com",
                      password="password1",
                      phone="+16507735818"
                      )

sm = crud.create_user(first_name="Sean",
                      last_name="Montgomery",
                      email="seandmontgomery@gmail.com",
                      password="password2",
                      phone="+15202482392"
                      )

sg = crud.create_user(first_name="Spencer",
                      last_name="Glass",
                      email="sglass724@gmail.com",
                      password="password3",
                      phone="+15164451174"
                      )

########################################################################

wk = crud.create_job(user_id=1,
                     project_title="Wicked",
                     industry="Theatre",
                     company="Broadway",
                     casting_office="Telsey",
                     agency="Stewart Talent")


bb = crud.create_job(user_id=2,
                     project_title="Blue Bloods",
                     industry="TV",
                     company="CBS",
                     casting_office="Bowling Miscia",
                     agency="CGF")

cc = crud.create_job(user_id=1,
                     project_title="Coca Cola Energy",
                     industry="Voiceover",
                     company="London Vision",
                     casting_office="Jenny Brightman",
                     agency="Nicolosi")

########################################################################

wka = crud.create_audition(user_id=jb.user_id,
                           job_id=1,
                           callback=False,
                           date="11-18-19",
                           time="3:00pm",
                           role="Nessa",
                           location="1400 Broadway",
                           notes="I wore my long sleeved black dress with flowers on it from H&M.")

# wkk = crud.create_audition(user_id=1,
#                            job_id=1,
#                            callback=True,
#                            date="11-18-19",
#                            time="3:00pm",
#                            role="Nessa",
#                            location="1400 Broadway",
#                            notes="I wore my long sleeved black dress with flowers on it from H&M.")


bba = crud.create_audition(user_id=sm.user_id,
                           job_id=2,
                           callback=False,
                           date="09-01-20",
                           time="11:15am",
                           role="Officer Jones",
                           location="self tape",
                           notes="I did the scene three times, was given notes to do three completely different takes. I wore button up white shirt")

cca = crud.create_audition(user_id=jb.user_id,
                           job_id=3,
                           callback=False,
                           date="02-11-21",
                           time="N/A",
                           role="Woman",
                           location="self record",
                           notes="No response from submission, but felt like this project was a really good fit for me. The final submitted mp3 is attached.")
########################################################################


bb = crud.create_media(audition_id="3",
                       user_id=jb.user_id,
                       media_title="Officer Jones", link="")
cce = crud.create_media(audition_id="2",
                        user_id=sm.user_id,
                        media_title="CocaCola", link="")
wkm = crud.create_media(audition_id="1",
                        user_id=jb.user_id,
                        media_title="Nessa Audition", link="")
