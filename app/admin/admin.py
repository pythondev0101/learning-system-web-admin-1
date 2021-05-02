from flask import current_app
from app.core import CoreModule
from .models import AdminDashboard, AdminApp
from app.auth.models import User,Role
from prime_admin.models import Branch, ContactPerson



class AdminModule(CoreModule):
    module_name = 'admin'
    module_icon = 'fa-home'
    module_link = current_app.config['ADMIN']['HOME_URL']
    module_short_description = 'Administration'
    module_long_description = "Administration Dashboard and pages"
    models = [AdminDashboard, AdminApp, User, Role, Branch]
    version = '1.0'
    sidebar = {
        'DASHBOARDS': [
            AdminDashboard
        ],
        'SYSTEM': [
            User, Role
        ],
        'CONFIGURATION':[
            Branch
        ]
    }