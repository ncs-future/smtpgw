import asyncio
import smtplib
import email.utils
import ssl
from aiosmtpd.controller import Controller

class SMTPGWHandler:
    async def handle_DATA(self, server, session, envelope):
        peer = session.peer
        server = smtplib.SMTP("smtp.email.ap-tokyo-1.oci.oraclecloud.com", 587)
        server.ehlo()
        server.starttls(context=ssl.create_default_context(purpose=ssl.Purpose.SERVER_AUTH, cafile=None, capath=None))
        server.ehlo()
        server.login("ながいoci smtp credential login user", "oci smtp credential password")
        server.sendmail(envelope.mail_from, envelope.rcpt_tos, envelope.content)
        server.close()
        return '250 OK'

if __name__ == '__main__':
    controller = Controller(SMTPGWHandler(), hostname='127.0.0.1', port=10025)
    controller.start()
    input('Press Return to exit.')
    controllerd.stop()
