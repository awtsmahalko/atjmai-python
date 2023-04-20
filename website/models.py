from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class Alumni(db.Model):
    __tablename__ = 'tbl_alumni'
    alumni_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, nullable=False, default=0)
    alumni_fname = db.Column(db.String(150), nullable=True)
    alumni_mname = db.Column(db.String(150), nullable=True)
    alumni_lname = db.Column(db.String(150), nullable=True)
    alumni_gender = db.Column(db.String(10), nullable=True)
    alumni_contact = db.Column(db.String(15), nullable=True)
    alumni_address = db.Column(db.String(255), nullable=True)
    course_id = db.Column(db.Integer, nullable=False, default=0)
    alumni_graduation = db.Column(db.Date, nullable=False, default='0000-00-00')
    created_at = db.Column(db.DateTime, nullable=False, default=db.func.current_timestamp())
    updated_at = db.Column(db.DateTime, nullable=False, default='0000-00-00 00:00:00', onupdate=db.func.current_timestamp())
    is_employed = db.Column(db.Integer, nullable=False)

class Employers(db.Model):
    __tablename__ = 'tbl_employers'

    employer_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, nullable=False, default=0)
    industry_id = db.Column(db.Integer, nullable=False, default=0)
    sub_industry_id = db.Column(db.Integer, nullable=False, default=0)
    employer_name = db.Column(db.String(255), nullable=True)
    company_name = db.Column(db.String(255), nullable=True)
    company_contact = db.Column(db.String(255), nullable=True)
    company_address = db.Column(db.String(255), nullable=True)
    company_description = db.Column(db.Text, nullable=True)
    employees_number = db.Column(db.String(10), nullable=True)
    created_at = db.Column(db.DateTime, nullable=False, default=db.func.current_timestamp())
    updated_at = db.Column(db.DateTime, nullable=False, default='0000-00-00 00:00:00', onupdate=db.func.current_timestamp())

class Jobs(db.Model):
    __tablename__ = 'tbl_jobs'

    job_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    employer_id = db.Column(db.Integer, nullable=True, default=0)
    job_title = db.Column(db.String(250), nullable=True)
    job_description = db.Column(db.Text, nullable=True)
    job_type_id = db.Column(db.Integer, nullable=False, default=0)
    job_sched_id = db.Column(db.Integer, nullable=False, default=0)
    hire_needed = db.Column(db.Integer, nullable=False, default=0)
    expected_hire_date = db.Column(db.String(50), nullable=True)
    salary_details = db.Column(db.String(150), nullable=True)
    created_at = db.Column(db.DateTime, nullable=False, default=db.func.current_timestamp())
    updated_at = db.Column(db.DateTime, nullable=False, default='0000-00-00 00:00:00', onupdate=db.func.current_timestamp())

class JobSkills(db.Model):
    __tablename__ = 'tbl_job_skills'

    job_skill_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    skill_id = db.Column(db.Integer, nullable=False, default=0)
    skill_rating = db.Column(db.Integer, nullable=False, default=0)
    job_id = db.Column(db.Integer, nullable=False, default=0)
    created_at = db.Column(db.DateTime, nullable=False, default=db.func.current_timestamp())
    updated_at = db.Column(db.DateTime, nullable=False, default='0000-00-00 00:00:00', onupdate=db.func.current_timestamp())

class Skills(db.Model):
    __tablename__ = 'tbl_skills'

    skill_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    sub_industry_id = db.Column(db.Integer, nullable=True)
    sc_id = db.Column(db.Integer, nullable=False, default=0)
    skill_name = db.Column(db.String(150), nullable=True)
    created_at = db.Column(db.DateTime, nullable=False, default=db.func.current_timestamp())
    updated_at = db.Column(db.DateTime, nullable=False, default='0000-00-00 00:00:00', onupdate=db.func.current_timestamp())

class Users(db.Model):
    __tablename__ = 'tbl_users'

    user_id = db.Column(db.Integer, primary_key=True)
    user_fullname = db.Column(db.String(255), nullable=False)
    user_email = db.Column(db.String(150), nullable=False)
    user_password = db.Column(db.String(32), nullable=False)
    user_category = db.Column(db.String(1), nullable=False, comment='A=Admin,E=Employer,S=Student/Alumni')
    user_status = db.Column(db.Integer, nullable=False, default=0)
    user_img = db.Column(db.String(255), nullable=False, default='default_male.png')
    created_at = db.Column(db.DateTime, nullable=False, default=db.func.current_timestamp())
    updated_at = db.Column(db.DateTime, nullable=False, default='0000-00-00 00:00:00', onupdate=db.func.current_timestamp())