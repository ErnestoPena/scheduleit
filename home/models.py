from django.db import models
from django.contrib.auth.models import User

# locations table will store information for companies with multiple offices
class locations(models.Model):
    description = models.CharField(max_length=30, blank = False)
    address = models.CharField(max_length=50, blank = True)
    city = models.CharField(max_length=20, blank = False)
    state = models.CharField(max_length=20, blank = False)
    zipcode = models.CharField(max_length=9, blank= False)
    manager = models.ForeignKey(User, on_delete = models.RESTRICT)
    notes = models.TextField(blank = True)

# Tasks status will list different options to categorize Tasks based on completion status
# I have to define this table before projects and taskcycle table because of the foreign keys
class taskstatus(models.Model):
    name = models.CharField(max_length=15, blank = False)
    description = models.TextField(blank = True)
    color = models.CharField(max_length=15, blank = True)


# projects table will store all the information about projects
# which will be identified by the office location
class projects(models.Model):
    project_id = models.TextField(max_length=15, blank = False)
    name = models.CharField(max_length=30, blank = False)
    description = models.TextField(max_length=200, blank = True)
    address = models.CharField(max_length=50, blank = True)
    city = models.CharField(max_length=20, blank = False)
    state = models.CharField(max_length=20, blank = False)
    zipcode = models.CharField(max_length=9, blank= False)
    contact = models.CharField(max_length= 30, blank = True)
    position = models.CharField(max_length=20, blank = True)
    email = models.EmailField(max_length=30, blank = True)
    telephone = models.CharField(max_length=10, blank = True)
    notes = models.TextField(blank = True)
    created_at = models.DateTimeField(blank = False, auto_now_add= True)
    updated_at = models.DateTimeField(blank = False, auto_now= True)
    location = models.ForeignKey(locations, on_delete = models.RESTRICT)
    sales_rep = models.ForeignKey(User, on_delete = models.RESTRICT)
    project_status = models.ForeignKey(taskstatus, on_delete = models.RESTRICT)


# tasks table will keep track of the different activities a project contain
# A single project might have multiple tasks.
class projectTasks(models.Model):
    project = models.ForeignKey(projects, on_delete = models.CASCADE)
    work_order = models.CharField(max_length= 10, blank = False)
    title = models.CharField(max_length=50, blank = False)
    description = models.TextField(blank = False)
    scope_work = models.TextField(blank = False)
    purchase_order = models.CharField(max_length=15, blank = True)
    final_report = models.TextField(blank = True)
    created_at = models.DateTimeField(blank = False, auto_now_add = True)
    updated_at = models.DateTimeField(blank = False, auto_now= True)


# taskhistory table will keep track of changes for the task's life cycle
# and for when a tast require multiple visits. For example, on big projects 
class taskCycle(models.Model):
    task = models.ForeignKey(projectTasks, on_delete = models.CASCADE)
    status = models.ForeignKey(taskstatus, on_delete = models.RESTRICT)
    user = models.ForeignKey(User, on_delete = models.RESTRICT)
    created_at = models.DateTimeField(blank = False, auto_now_add = True)
    updated_at = models.DateTimeField(blank = False, auto_now= True)
    description = models.TextField(blank = True)

# scheduler table is the heart of the system. It will contain the date with the task and 
# the employees assigned to that task.
class scheduler(models.Model):
    task = models.ForeignKey(projectTasks, on_delete = models.CASCADE)
    created_at = models.DateTimeField(blank = False, auto_now_add = True)
    date_togo = models.DateField(blank = False)
    time_togo = models.TimeField(blank = False)
    notes = models.TextField(blank = False)


# userTasks is the table that will hold the employees assigned to each task on an 
# specific date

class userTasks(models.Model):
    schedulerid = models.ForeignKey(scheduler, on_delete = models.CASCADE)
    users = models.ForeignKey(User, on_delete = models.CASCADE) 