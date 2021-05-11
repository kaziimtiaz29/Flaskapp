from app import db, Countries, Cities

db.create_all() 

ITALY = Countries(name = 'Italy')
db.session.add(ITALY)
db.session.commit()

Rome = Cities(name='Rome', country = ITALY)
#mcr = Cities(name='Manchester', country = Countries.query.filter_by(name='United Kingdom').first())

db.session.add(Rome)
#db.session.add(mcr)
db.session.commit()