from prime_admin.functions import generate_number
from prime_admin.forms import RegistrationForm, StudentForm, TeacherForm, TrainingCenterEditForm, TrainingCenterForm
from flask_login import login_required, current_user
from app.admin.templating import admin_render_template, admin_table, admin_edit
from prime_admin import bp_lms
from prime_admin.models import Earning, Registration, Member
from flask import redirect, url_for, request, current_app, flash
from app import db
from datetime import datetime


@bp_lms.route('/earnings', methods=['GET'])
@login_required
def earnings():
    _table_columns = [
        'Branch', 'Full Name', 'batch no.', 'schedule', 'remark'
    ]

    return admin_table(
        Earning,
        fields=[],
        table_data=[],
        table_columns=_table_columns,
        heading="",
        subheading='',
        title='Earnings',
        table_template='lms/earnings.html'
    )