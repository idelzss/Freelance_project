from flask import Blueprint, render_template, flash
from ..models import session, Profession, Program
from .utils import admin_only
from .forms_admin.profession import ProfessionForm
from .forms_admin.program import ProgramForm

admin = Blueprint(
    "admin",
    __name__,
    url_prefix="/admin",
    static_folder="static",
    template_folder="templates"
)


@admin.route('/dashboard', endpoint='dashboard')
@admin_only
def dashboard():
    professions = session.query(Profession).all()
    return render_template("admin/admin.html", professions=professions)


@admin.route("/create_profession", methods=["GET", "POST"])
@admin_only
def create_profession():
        form = ProfessionForm()
        if form.validate_on_submit():
            profession = Profession(
                name=form.name.data,
                description=form.description.data
            )
            session.add(profession)
            session.commit()
            flash("Your profession has been created!")
        return render_template("admin/create_profession.html", form=form)


@admin.route("/create_program", methods=["GET", "POST"])
@admin_only
def create_program():
    form = ProgramForm()

    form.profession.choices = [(profession.id, profession.name) for profession in session.query(Profession).all()]

    if form.validate_on_submit():
        program = Program(
            title=form.title.data,
            description=form.description.data,
            video_url=form.video_url.data,
            profession_id=form.profession.data
        )
        session.add(program)
        session.commit()
        flash("Your program has been created!")

    return render_template("admin/create_programs.html", form=form)


