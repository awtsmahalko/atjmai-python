from flask import Blueprint, render_template, request, flash, jsonify, redirect, url_for
from flask_login import login_required, current_user
from .models import Alumni, Employers, Jobs, JobSkills, Skills
from . import db
import json
from datetime import datetime, timedelta
from collections import defaultdict
from sqlalchemy import extract,func

views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
def home():
    return "Access forbidden.<br>Alumni Tracker with Job Matching using AI Integration @2023"

@views.route('/job-match', methods=['GET', 'POST'])
def job_match():
    alumni_id = 1
    job_list = get_best_jobs(alumni_id)
    response = {
        'jobs': job_list
    }
    return jsonify(response)
    if request.method == 'POST':
        alumni_id = request.form.get('alumni_id')
    else:
        return "Access forbidden.<br>Alumni Tracker with Job Matching using AI Integration @2023"

def get_best_jobs(alumni_id):
    job_list = []
    jobs = Jobs.query.all()
    for job in jobs:
        job_data = {
            'job_id': job.job_id,
            'employer_id': job.employer_id,
            'job_title': job.job_title,
            'job_type_id': job.job_type_id,
            'job_sched_id': job.job_sched_id,
            'job_description': job.job_description,
            'hire_needed': job.hire_needed,
            'expected_hire_date': job.expected_hire_date,
            'created_at': str(job.created_at),
            'updated_at': str(job.updated_at),
            'salary_details':job.salary_details,
            'skills':get_job_skills(job.job_id),
            'employers':get_employer_data(job.employer_id),
        }
        job_list.append(job_data)
    return job_list

def get_employer_data(employer_id):
    employer_data = Employers.query.filter_by(employer_id=employer_id).first()
    return {
        'company_address':employer_data.company_address,
        'company_contact':employer_data.company_contact,
        'company_description':employer_data.company_description,
        'company_name':employer_data.company_name,
        'created_at': str(employer_data.created_at),
        'employees_number':employer_data.employees_number,
        'employer_id':employer_data.employer_id,
        'employer_name':employer_data.employer_name,
        'industry_id':employer_data.industry_id,
        'sub_industry_id':employer_data.sub_industry_id,
        'user_id':employer_data.user_id,
        'updated_at': str(employer_data.updated_at),
    }

def get_job_skills(job_id):
    skill_list = []
    job_skills = JobSkills.query.filter_by(job_id=job_id).all()
    for skill in job_skills:
        skill_data_ = get_skills_data(skill.skill_id)
        skill_list.append({
            'created_at': str(skill.created_at),
            'job_id':skill.job_id,
            'job_skill_id':skill.job_skill_id,
            'skill_id':skill.skill_id,
            'skill_name':skill_data_['skill_name'],
            'skill_rating':skill.skill_rating,
            'updated_at': str(skill.updated_at),
        })
    return skill_list

def get_skills_data(skill_id):
    skill_data = Skills.query.filter_by(skill_id=skill_id).first()
    if skill_data:
        return {
            'created_at': str(skill_data.created_at),
            'sc_id':skill_data.sc_id,
            'skill_id':skill_data.skill_id,
            'skill_name':skill_data.skill_name,
            'updated_at': str(skill_data.updated_at),
        }

    return {
        'created_at': "",
        'sc_id':0,
        'skill_id':0,
        'skill_name':"",
        'updated_at': "",
    }