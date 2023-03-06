from .sms_sender import SendSMS


def send_sms_user(phone_number):
    sms = SendSMS()
    generate = sms.generate_one_time_sms()
    sms.send_sms(phone_number, generate)
    return generate

