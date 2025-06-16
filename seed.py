from random import randint, choice as rc
from faker import Faker 
from app import app
from models import db, Student, Mentor, Reward, Cohort

if __name__ == '__main__':
    with app.app_context():
        db.drop_all()
        db.create_all()

        # Create mentors
        mentor1 = Mentor(name="Aaron")
        mentor2 = Mentor(name="Dennis")
        mentor3 = Mentor(name="Rose")

        db.session.add_all([mentor1, mentor2, mentor3])
        db.session.commit()

        # Create cohorts
        cohort1 = Cohort(name='Remote11', year=2011, mentor_id=mentor1.id)
        cohort2 = Cohort(name='Remote12', year=2012, mentor_id=mentor2.id)
        cohort3 = Cohort(name='Remote13', year=2013, mentor_id=mentor3.id)

        db.session.add_all([cohort1, cohort2, cohort3])
        db.session.commit()

        # Create students
        student1 = Student(name="Ken", cohort_id=cohort1.id)
        student2 = Student(name="Elvis", cohort_id=cohort2.id)
        student3 = Student(name="Yelsin", cohort_id=cohort3.id)
        db.session.add_all([student1, student2, student3])
        db.session.commit()

        # Create rewards
        reward1 = Reward(name='Laptop', mentor_id=mentor1.id)
        reward2 = Reward(name='Biro', mentor_id=mentor2.id)
        reward3 = Reward(name='Tecno', mentor_id=mentor3.id)

        db.session.add_all([reward1, reward2, reward3])
        db.session.commit()

        print("Seeding completed.")