import os
import smtplib
import requests
import ssl


def descarga(url, enfermedad):
    r = requests.get(url, allow_redirects=True)
    open(enfermedad + '.csv', 'wb').write(r.content)
    file_stat = os.stat(enfermedad + '.csv')

    if file_stat.st_size < 30000:
        context = ssl.create_default_context()
        message = 'Se encontro un problema en la BD de' + ' ' + enfermedad
        subject = 'Error en base de datos de' + ' ' + enfermedad
        message = 'Subject: {}\n\n{}'.format(subject, message)
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls(context=context)
        server.login('observatorioproyecto1@gmail.com', 'uwftzgqywensvpdm')
        server.sendmail('observatorioproyecto1@gmail.com', 'edango09@gmail.com', message)
        server.quit()
        exit()
    return
