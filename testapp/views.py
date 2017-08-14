from django.shortcuts import render
from .models import Test, Tquestion, Applicant, User
from django.conf import settings
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
import datetime

from django.utils.crypto import get_random_string


import requests


"""Валідація Email"""
def validateEmail(email):
    from django.core.validators import validate_email
    from django.core.exceptions import ValidationError
    try:
        validate_email(email)
        return True
    except ValidationError:
        return False


#https://simpleisbetterthancomplex.com/tutorial/2017/02/21/how-to-add-recaptcha-to-django-site.html


def validateCaptcha(recaptcha_response):
    data = {
        'secret': settings.GOOGLE_RECAPTCHA_SECRET_KEY,
        'response': recaptcha_response
    }
    r = requests.post('https://www.google.com/recaptcha/api/siteverify', data=data)
    result = r.json()
    if result['success']:
        return True
    else:
        return False


def logout(request):
    request.session['loged'] = False
    return HttpResponseRedirect('/')


"""Start page
this module is displaying sign in/sign up page, if the user is not
loged in, and redirect to testlist, if the user is loged in
('loged' in request.session or request.session['loged'] = True)
System is checking user Login and Email for prevention of duplicate accounts data"""


def home(request):
    request.session['submited'] = False
    if request.session.get('loged'):
        return HttpResponseRedirect('/testlist/')
    if request.method == 'POST':
        if request.POST.get('g-recaptcha-response'):
            if '_signin' in request.POST:
                if request.POST.get("Login", "") != '' and request.POST.get("Password", "") != '':
                    if User.objects.filter(login=request.POST.get("Login", ""),
                                           password=request.POST.get("Password", "")).count() > 0:
                        if User.objects.filter(login=request.POST.get("Login", ""),
                                           password=request.POST.get("Password", ""), active=True).count() == 0:
                            return render(request, "testapp/aplicant_info.html",
                                          {'message': 'your account is not active'})
                        udata = User.objects.filter(login=request.POST.get("Login", ""),
                                                    password=request.POST.get("Password", ""))[0]
                        request.session['FirstName'] = udata.name
                        request.session['LastName'] = udata.surname
                        request.session['Email'] = udata.email
                        request.session['loged'] = True
                        request.session['testlist'] = True
                        message=''
                        return HttpResponseRedirect('/testlist/', {'message': message})
                    else:
                        return render(request, "testapp/aplicant_info.html",
                                      {'message': 'enter valid User name and Password'})

            if '_signup' in request.POST:
                if User.objects.filter(email=request.POST.get("Email", "")).count() != 0:
                    return render(request, "testapp/aplicant_info.html",
                                  {'message': 'this e-mail is already using in our system'})
                if User.objects.filter(login=request.POST.get("Login_up", "")).count() != 0:
                    return render(request, "testapp/aplicant_info.html",
                                  {'message': 'this login is already using in our system'})
                if validateEmail(request.POST.get("Email", "")).__bool__() and \
                                request.POST.get("FirstName", "") != '' and \
                                request.POST.get("LastName", "") != '' and \
                                request.POST.get("Login_up", "") != ''and \
                                request.POST.get("Password1", "") != ''and \
                                request.POST.get("Password2", "") != '':

                    activatecode = get_random_string(length=50)
                    newuser = User(email=request.POST.get("Email", ""),
                                   name=request.POST.get("FirstName", ""),
                                   surname=request.POST.get("LastName", ""),
                                   login=request.POST.get("Login_up", ""),
                                   password=request.POST.get("Password1", ""),
                                   active=False,
                                   veryfied=False,
                                   activatecode=activatecode
                                   )
                    newuser.save()
                    send_mail('Info about your account',
                              'Today you registered in our test portal.\nYour login is: ' +
                              request.POST.get("Login_up", "") +
                              '\nYour password is: ' +
                              request.POST.get("Password1", "") + '\nClick for activation your account'
                              '\nhttp://77.120.94.81:61616/?activate=' + activatecode,
                              settings.EMAIL_HOST_USER,
                              [request.POST.get("Email", ""), settings.EMAIL_HOST_USER])
                    """return HttpResponseRedirect('/#signin',
                                                {'message': 'Information about your registration was sent to: '
                                              +request.POST.get("Email", "")})
                    return render(request, "testapp/aplicant_info.html",
                                  {'message': 'Information about your registration was sent to: '
                                              +request.POST.get("Email", "")})"""
                    return render(request, "testapp/info_page.html",
                                  {'Message': 'Information about your registration was sent to: '
                                              +request.POST.get("Email", "")+
                                              ' Please, check your email for activating account'})

            if '_forgot' in request.POST:
                if User.objects.filter(email=request.POST.get("Emailfrg", ""),
                                       name=request.POST.get("FirstNamefrg", ""),
                                       surname=request.POST.get("LastNamefrg", "")).count() == 0:
                    return render(request, "testapp/aplicant_info.html",
                                  {'message': 'there is no such user in system'})
                else:
                    loginfrg = User.objects.filter(email=request.POST.get("Emailfrg", ""),
                                       name=request.POST.get("FirstNamefrg", ""),
                                       surname=request.POST.get("LastNamefrg", ""))[0].login
                    passwordfrg = User.objects.filter(email=request.POST.get("Emailfrg", ""),
                                                name=request.POST.get("FirstNamefrg", ""),
                                                surname=request.POST.get("LastNamefrg", ""))[0].password
                    send_mail('Info about your account',
                              'You forgot your accout info?.\nYour login is: ' +
                              loginfrg + '\nYour password is: ' + passwordfrg +
                              '\nhttp://77.120.94.81:61616/ ',
                              settings.EMAIL_HOST_USER,
                              [request.POST.get("Emailfrg", ""), settings.EMAIL_HOST_USER])
                    return render(request, "testapp/aplicant_info.html",
                                  {'message': 'Information about your registration was sent to: '
                                              +request.POST.get("Emailfrg", "")})
        else:
            message = 'captcha is not valid ('
            return render(request, "testapp/aplicant_info.html", {'message': message})

    if request.method == 'GET':
        if request.session.get('message'):
            message = request.session.get('message')
        else:
            message = ''
        if request.GET.get('activate'):
            if User.objects.filter(activatecode=request.GET['activate']).count() > 0:
                a = User.objects.get(activatecode=request.GET['activate'])
                a.activatecode = 'activated'
                a.active = True
                a.veryfied = True
                a.save()
                message = 'Welcome into our test system'
                request.session['FirstName'] = a.name
                request.session['LastName'] = a.surname
                request.session['Email'] = a.email
                request.session['loged'] = False
                request.session['testlist'] = False
                message = 'Dear '+a.name+' ' + a.surname +\
                          ' .Welcome in to our test system. Now your account is activated.'
                return render(request, "testapp/info_page.html", {'Message': message})
                #return HttpResponseRedirect('/testlist/', {'message': message})
            else:
                message = 'This activation link is unavailable'
        return render(request, "testapp/aplicant_info.html", {'message': message})


"""Display of tests
this module is displaying test_list page and user history if request.session['loged'] == True and
test  not started by such user. If the user have started test and (submit_if_leave==False),
it redirect him on question_list page to continue passing saved test.
if (submit_if_leave==True) system will automatic submit this test
If method==Post it request.session['loged']=False system will redirect to login page
The user can't pass the same test more than once
"""

def test_list(request):
    if 'loged' in request.session and 'Email' in request.session:
        if not request.session.get('loged'):
            return HttpResponseRedirect('/')

    if Applicant.objects.filter(email=request.session['Email'], test_status='started').count() != 0:
        tname = Applicant.objects.filter(email=request.session['Email'], test_status='started')[0].test_name
        testid = Test.objects.filter(test_name=tname)[0].id
        return question_list(request, testid)
    if request.method == 'POST':
        if 'logout' in request.POST:
            request.session['loged'] = False
            #return render(request, "testapp/aplicant_info.html", {'message': ''})
            return HttpResponseRedirect('/')
        if 'gotoadmin' in request.POST:
            return HttpResponseRedirect('/admin/')

    else:
        tests = Test.objects.all()
        apphist = Applicant.objects.all().filter(email=request.session['Email'])
        message = ''
        if 'message' in request.session:
            message = request.session['message']
        request.session['message'] = ''
        return render(request, 'testapp/test_list.html', {'tests': tests,
                                                          'FirstName': request.session['FirstName'],
                                                          'LastName': request.session['LastName'],
                                                          'Email': request.session['Email'],
                                                          'apphist': apphist,
                                                          'message': message})


"""List of question
this module is displaying the list of questions if request.session['loged'] == True, and started 
test by such user. If the user have started test and (Test.submit_if_leave == False), it will get saved data from 
dbase about started test and display questions, which displayed at start of that test in the past.
If (Test.submit_if_leave == True) it will write info to dbase, that the user failed test.
If request.session['loged'] == False it redirect to home.
If method==POST, all the results in form saving in SUBMITTEST and redirect to submit
"""


def question_list(request, pk):
    request.session['message'] = ''
    qquestion = ''
    if 'loged' in request.session:
        if not request.session.get('loged'):
            return HttpResponseRedirect('/')
    if request.method == 'GET':
        tname = Test.objects.get(pk=pk)
        if Applicant.objects.filter(email=request.session['Email'],
                                    test_name=tname.test_name,
                                    test_status='passed').count() != 0 or \
                        Applicant.objects.filter(email=request.session['Email'],
                                                 test_name=tname.test_name,
                                                 test_status='failed').count() != 0:
            request.session['message'] = 'you have already tried to pass' + tname.test_name
            return HttpResponseRedirect('/testlist/')

        if Tquestion.objects.filter(test_name_id=pk).count() < Test.objects.filter(pk=pk)[0].q_count.__int__():
            request.session['message'] = 'not enough questions in dbase for test: ' + tname.test_name
            return HttpResponseRedirect('/testlist/')


        # зберігаємо початок тесту
        if Applicant.objects.filter(email=request.session['Email'], test_name=tname.test_name,
                                    test_status='started').count() == 0:
            quests = Tquestion.objects.order_by('?').filter(test_name_id=pk)[:tname.q_count]
            for e in quests:
                qquestion = qquestion + e.pk.__str__() + ','
            request.session['QUESTCOUNT'] = quests.count()
            request.session['TESTNAME'] = tname.test_name
            status_description = 'Test was started normaly'
            newresult = Applicant(test_name=tname, email=request.session['Email'],
                                  name=request.session['FirstName'],
                                  surname=request.session['LastName'],
                                  test_status='started', qquery=qquestion,
                                  startpassing_date=datetime.datetime.now(),
                                  passing_date=datetime.datetime.now(),
                                  status_description=status_description,
                                  test_id=pk)
            newresult.save()
            dad_line_time = Applicant.objects.get(email=request.session['Email'],
                                                  test_name=tname.test_name,
                                                  test_status='started').startpassing_date + \
                            datetime.timedelta(minutes=Test.objects.get(test_name=tname.test_name).timetest)

            minutes = (dad_line_time-datetime.datetime.now()).seconds//60+1
            seconds = 00
            dad_line_time = dad_line_time.strftime('%Y/%m/%d %H:%M:%S')
            now_date_time = datetime.datetime.now().strftime('%Y/%m/%d %H:%M:%S')
            strquests = Applicant.objects.filter(email=request.session['Email'], test_status='started')[0].qquery[:-1]
            quests = Tquestion.objects.filter(pk__in=strquests.split(','))
            return render(request, 'testapp/questions.html', {'quests': quests,
                                                              'tname': tname.test_name,
                                                              'cquests': tname.q_count,
                                                              'idtest': tname.id,
                                                              'FirstName': request.session['FirstName'],
                                                              'LastName': request.session['LastName'],
                                                              'Email': request.session['Email'],
                                                              'dad_line_time': dad_line_time,
                                                              'now_date_time': now_date_time,
                                                              'minutes': minutes,
                                                              'seconds': seconds})
        # вибірка питань збереженого тесту
        if Applicant.objects.filter(email=request.session['Email'],
                                    test_name=tname.test_name,
                                    test_status='started').count() != 0 and \
                        Test.objects.get(test_name=tname.test_name).submit_if_leave == False:
            strquests = Applicant.objects.filter(email=request.session['Email'], test_status='started')[0].qquery[:-1]
            #arrayquests = eval('[' + strquests + ']')
            #quests = Tquestion.objects.filter(id=arrayquests[0])
            k = 1
            #while k < len(arrayquests):
             #   quests = quests | Tquestion.objects.all().filter(id=arrayquests[k])
                #quests = quests | arrayquests[k]
              #  k = k + 1
            quests = Tquestion.objects.filter(pk__in=strquests.split(','))
            dad_line_time = Applicant.objects.get(email=request.session['Email'],
                                                  test_name=tname.test_name,
                                                  test_status='started').startpassing_date + \
                            datetime.timedelta(minutes=Test.objects.get(test_name=tname.test_name).timetest)

            minutes = (dad_line_time - datetime.datetime.now()).seconds // 60
            seconds = (dad_line_time - datetime.datetime.now()).seconds % 60

            dad_line_time = dad_line_time.strftime('%Y/%m/%d %H:%M:%S')
            timeforpass = Test.objects.get(test_name=tname.test_name).timetest
            starttesttime = Applicant.objects.get(email=request.session['Email'],
                                                  test_name=tname.test_name,
                                                  test_status='started').startpassing_date
            if (datetime.datetime.now() - starttesttime).total_seconds() > (timeforpass * 60):
                request.session['submited'] = True
                request.session['SUBMITTEST'] = request.POST
                request.session['TESTID'] = pk
                return HttpResponseRedirect('/submit/')
            return render(request, 'testapp/questions.html', {'quests': quests,
                                                              'tname': tname.test_name,
                                                              'cquests': tname.q_count,
                                                              'idtest': tname.id,
                                                              'FirstName': request.session['FirstName'],
                                                              'LastName': request.session['LastName'],
                                                              'Email': request.session['Email'],
                                                              'dad_line_time': dad_line_time,
                                                              'minutes': minutes,
                                                              'seconds': seconds})

        # Якщо відновлення тесту не передбачено - сабмітимо 0 результат
        if Applicant.objects.filter(email=request.session['Email'],
                                    test_name=tname.test_name,
                                    test_status='started').count() != 0 and \
                        Test.objects.get(test_name=tname.test_name).submit_if_leave == True:
            status_description = 'Leaved from test, auto-failed'
            Applicant.objects.filter(email=request.session['Email'],
                                     test_name=tname.test_name,
                                     test_status='started').update(test_status='failed',
                                                                   passing_date=datetime.datetime.now(),
                                                                   status_description=status_description)
            return HttpResponseRedirect('/testlist/')
            # Якщо форма поститься переходимо на сабміт
    else:
        request.session['submited'] = True
        request.session['SUBMITTEST'] = request.POST
        request.session['TESTID'] = pk
        return HttpResponseRedirect('/submit/')


"""Calculate the mark and show the last page
This module make calculation with data from request.session['SUBMITTEST'],
record results into dbase and send it to user's email
"""


def submit(request):
    if not request.session.get('loged'):
        return HttpResponseRedirect('/')

    if 'submited' in request.session:
        if not request.session['submited']:
            return HttpResponseRedirect('/')
    TestRslt = request.session['SUBMITTEST']
    testid = request.session.get('TESTID')
    testname = request.session.get('TESTNAME')
    questcount = request.session.get('QUESTCOUNT')
    FirstName = request.session['FirstName']
    LastName = request.session['LastName']
    Email = request.session['Email']
    if Applicant.objects.filter(email=request.session['Email'],
                                test_name=request.session.get('TESTNAME'),
                                test_status='started').count() != 0:
        result = 0
        for e in Tquestion.objects.all().filter(test_name_id=testid):
            if ('ch' + e.id.__str__() + '.1') in request.session['SUBMITTEST']:
                choicer1 = True
            else:
                choicer1 = False
            if ('ch' + e.id.__str__() + '.2') in request.session['SUBMITTEST']:
                choicer2 = True
            else:
                choicer2 = False
            if ('ch' + e.id.__str__() + '.3') in request.session['SUBMITTEST']:
                choicer3 = True
            else:
                choicer3 = False
            if ('ch' + e.id.__str__() + '.4') in request.session['SUBMITTEST']:
                choicer4 = True
            else:
                choicer4 = False
            if ('ch' + e.id.__str__() + '.5') in request.session['SUBMITTEST']:
                choicer5 = True
            else:
                choicer5 = False
            resquery = {'id': e.id,
                        'choicer1': choicer1,
                        'choicer2': choicer2,
                        'choicer3': choicer3,
                        'choicer4': choicer4,
                        'choicer5': choicer5}
            if choicer1 == choicer2 == choicer3 == choicer4 == choicer5 == False:
                result = result
            else:
                result = result + Tquestion.objects.all().filter(**resquery).count()

        if result != 0:
            mark = round(result / questcount * 100, 1)
        else:
            mark = 0
        status_description = ''
        test_status = ''
        if mark > 80:
            status_description = 'In time and more than 80% right answers'
            test_status = 'passed'
        else:
            status_description = 'Les than 80% right answers'
            test_status = 'failed'
        timeforpass = Test.objects.get(test_name=testname).timetest
        starttesttime = Applicant.objects.get(email=request.session['Email'],
                                              test_name=testname,
                                              test_status='started').startpassing_date
        resultstring = 'You tried to pass the test with ' + \
                       questcount.__str__() + \
                       ' question(s). You gave ' + \
                       result.__str__() + \
                       ' right answers and scored: ' + \
                       mark.__str__() + ' %'
        if (datetime.datetime.now() - starttesttime).total_seconds() > (timeforpass * 60)+2:
            test_status = 'failed'
            status_description = 'Submitted test not in time'
            resultstring = 'You tried to pass the test with ' + \
                           questcount.__str__() + ' question(s). You gave ' + \
                           result.__str__() + ' right answers and scored: ' + \
                           mark.__str__() + ' %. But you tried to pass too long.((( You failed this test.'
        Applicant.objects.filter(email=request.session['Email'],
                                 test_name=testname,
                                 test_status='started').update(test_status=test_status,
                                                               mark_pass=mark,
                                                               passing_date=datetime.datetime.now(),
                                                               status_description=status_description)
        subject = 'Result of your testing on testproject'
        message = resultstring
        from_email = settings.EMAIL_HOST_USER
        to_list = [Email, settings.EMAIL_HOST_USER]
        send_mail(subject, message, from_email, to_list)
        return render(request, "testapp/thankyou.html", {'TestRslt': TestRslt,
                                                         'FirstName': FirstName,
                                                         'LastName': LastName,
                                                         'Email': Email,
                                                         'Mark': mark,
                                                         'Message': message})
    else:
        return HttpResponseRedirect('/testlist/')
