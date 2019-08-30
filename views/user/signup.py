import smtplib
import random

from flask import Blueprint, request
from flask_restplus import Api, Resource
from email.mime.text import MIMEText
from datetime import datetime

from DB import curs

api = Api(Blueprint(__name__, __name__))


@api.route('/signup')
class Signup(Resource):
    def post(self):
        try:
            tell = request.json['tell']
            email = request.json['email']
        except KeyError or TypeError:
            return {'msg': 'value_skipped'}, 400

        query_select_user_info = 'select tell from user where tell = %s'
        curs.execute(query_select_user_info, tell)
        existing_user_tell = curs.fetchone()
        if existing_user_tell:
            return {'msg': 'existing_telephone'}, 406

        query_select_user_info = 'select email from user where email = %s'
        curs.execute(query_select_user_info, email)
        existing_user_email = curs.fetchone()
        if existing_user_email:
            return {'msg': 'existing_email'}, 406

        smtp_connect = smtplib.SMTP('smtp.gmail.com', 587)
        smtp_connect.starttls()
        smtp_connect.login('wjd030811@dsm.hs.kr', 'epzuyfapmvrvxfib')

        cert_num = ''
        for i in range(6):
            cert_num += str(random.randrange(0, 10))

        msg = MIMEText(f'인증번호 : {cert_num}\n인증번호는 10분이 지나면 만료됩니다.')
        msg['Subject'] = 'RE:MARKET에서 발송한 인증번호입니다.'

        smtp_connect.sendmail('wjd030811@dsm.hs.kr', email, msg.as_string())\

        smtp_connect.quit()

        return {'cert_num': cert_num, 'timestamp': datetime.now().timestamp()}, 200
