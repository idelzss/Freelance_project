from flask import Blueprint, render_template, flash, redirect
from ..models import session, Job, Profession, Submission, Edit
from .utils import employer_only
from flask_login import current_user
from .forms_employer import JobForm, NotAcceptForm


employer = Blueprint(
    "employer",
    __name__,
    url_prefix="/employer",
    static_folder="static",
    template_folder="templates"


)

@employer.route("/")
@employer_only
def dashboard():
    jobs = session.query(Job).all()
    return render_template("employer/employer.html", jobs=jobs)


@employer.route("/create_job", methods=['GET', 'POST'])
@employer_only
def create_job():
    form = JobForm()

    form.profession.choices = [(profession.id, profession.name) for profession in session.query(Profession).all()]

    if form.validate_on_submit():
        job = Job(
            title=form.title.data,
            description=form.description.data,
            profession_id=form.profession.data,
            employer_id=current_user.id
        )
        session.add(job)
        session.commit()
        flash("Your job has been created!")
    return render_template("employer/create_job.html", form=form)

@employer.route("/send_works", methods=['GET', 'POST'])
@employer_only
def all_send_works():
    works = session.query(Submission).filter_by(employer_id=current_user.id)
    return render_template("employer/send_works.html", works=works)


@employer.route("/accept_work<int:id>", methods=['GET', 'POST'])
@employer_only
def accept_work(id):
    submission = session.query(Submission).filter_by(id=id).first()
    jobs = session.query(Submission).filter_by(id=id).first()
    if submission and jobs:
        session.delete(submission)
        session.delete(jobs)
        session.commit()
        session.close()
        flash("You accept this work!")
        return redirect("/employer/send_works")

@employer.route("/not_accept_work<int:id>", methods=['GET', 'POST'])
@employer_only
def not_accept_work(id):
    form = NotAcceptForm()

    submission = session.query(Submission).filter_by(id=id).first()

    if form.validate_on_submit():
        not_accept = Edit(
            description=form.description.data,
            employer_id=current_user.id,
            freelancer_id=submission.freelancer_id,


        )
        session.add(not_accept)
        session.commit()
        flash("You turned in your work!")
    return render_template("employer/not_accept.html", form=form, id=id)