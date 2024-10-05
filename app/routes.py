from . import app, login_manager
from .forms import LoginForm, RegistrationForm, SubmissionForm
from .models import User, session, Profession, Program, Job, UserTypeEnum, StatusEnumSubmission, Submission, StatusEnumJob, Edit
from flask import render_template, redirect, url_for, flash
from flask_login import current_user, login_user, login_required, logout_user
from werkzeug.security import check_password_hash, generate_password_hash


@login_manager.user_loader
def load_user(user_id):
    return session.query(User).get(user_id)

@app.route("/")
def home():
    return render_template("home.html", UserTypeEnum=UserTypeEnum)



@app.route("/login", methods=["GET", "POST"])
def log_in():
    if current_user.is_authenticated:
        return redirect(url_for("home"))
    form = LoginForm()
    if form.validate_on_submit():
        email = form.email.data
        user = session.query(User).filter_by(email=email).first()
        if not user:
            flash(f"User with email {email} does not exist.<br> <a href={url_for('registration')}>Register</a>", "error")
            return redirect(url_for("log_in"))
        elif check_password_hash(user.password, form.password.data):
            login_user(user=user)
            return redirect(url_for("home"))
        else:
            flash("Password or email incorrect", "error")
            return redirect(url_for("log_in"))
    else:
        return render_template("login.html", form=form)

@app.route("/register", methods=["GET", "POST"])
def registration():
    if current_user.is_authenticated:
        return redirect(url_for("home"))
    form = RegistrationForm()
    if form.validate_on_submit():
        email = form.email.data
        user = session.query(User).filter_by(email=email).first()
        if user:
            flash(f"User with email {email} does not exist.<br> <a href={url_for('log_in')}>Log in</a>", "error")
            return redirect(url_for("registration"))
        new_user = User(
            name=form.name.data,
            email=email,
            password=generate_password_hash(form.password.data),
            phone=form.phone.data,
            user_type=UserTypeEnum(form.role.data)
        )

        try:
            session.add(new_user)
            session.commit()
            flash("Thanks for registration! You can log in now!", "success")
            return redirect(url_for("log_in"))
        except Exception as exc:
            raise exc
        finally:
            session.close()
    return render_template("register.html", form=form)


@app.route("/logout")
@login_required
def log_out():
    logout_user()
    return redirect(url_for("log_in"))


@app.route("/learning")
@login_required
def learning():
    professions = session.query(Profession).all()
    return render_template("learning.html", professions=professions)


@app.route("/learning/program/<int:profession_id>")
@login_required
def profession_programs(profession_id):
    profession = session.query(Profession).get(profession_id)
    programs = session.query(Program).filter_by(profession_id=profession_id)
    return render_template("programs.html", profession=profession, programs=programs)





@app.route("/jobs", methods=["GET", "POST"])
@login_required
def find_job_profession():
    professions = session.query(Profession).all()
    return render_template("find_job.html", professions=professions)

@app.route("/jobs/profession/<int:profession_id>", methods=["GET", "POST"])
@login_required
def find_job(profession_id):
    jobs = session.query(Job).filter_by(profession_id=profession_id, status=StatusEnumJob.not_done).all()
    descriptions = session.query(Edit).filter_by(freelancer_id=current_user.id)
    return render_template("jobs.html", jobs=jobs, UserTypeEnum=UserTypeEnum, descriptions=descriptions)



@app.route("/jobs/<int:job_id>/take", methods=["GET", "POST"])
@login_required
def take_job(job_id):
    job = session.query(Job).get(job_id)

    if current_user.user_type != UserTypeEnum.freelancer:
        flash("Only freelancers can take jobs")
        return redirect(url_for('find_job_profession'))


    if job.freelancer_id is not None:
        flash("This job has already been taken.")
        return redirect(url_for('find_job_profession'))

    job.freelancer_id = current_user.id
    session.commit()

    flash("The job has been successfully taken and is now assigned to you")
    return redirect(url_for('find_job_profession'))





@app.route("/jobs/<int:job_id>/release", methods=["POST"])
@login_required
def release_job(job_id):
    job = session.query(Job).get(job_id)

    if job.freelancer_id != current_user.id:
        flash("You cannot release a job that is not assigned to you")
        return redirect(url_for("/jobs"))


    job.freelancer_id = None
    session.commit()

    flash("You have successfully released the job")
    return redirect(url_for("find_job_profession"))



@app.route("/my_job", methods=["GET", "POST"])
@login_required
def my_job():
    jobs = session.query(Job).filter_by(freelancer_id=current_user.id)
    if not jobs:
        flash('You have not taken any jobs yet.')

    return render_template('my_job.html', jobs=jobs)




@app.route("/jobs/<int:job_id>/submission", methods=['GET', 'POST'])
@login_required
def submission(job_id):
    form = SubmissionForm()

    form.employer_id.choices = [(user.id, user.name) for user in session.query(User).filter_by(user_type=UserTypeEnum.employer)]

    if form.validate_on_submit():
        submission = Submission(
            description=form.description.data,
            GitHub_Url=form.GitHub_Url.data,
            employer_id=form.employer_id.data,
            freelancer_id=current_user.id,
            status=StatusEnumSubmission.submitted

        )
        job = session.query(Job).get(job_id)
        job.status = StatusEnumJob.submitted
        session.add(submission)
        session.commit()
        flash("You turned in your work!")
    return render_template("submission.html", form=form, job_id=job_id)


