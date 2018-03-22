# -*- coding: utf-8 -*-
"""
Created on Sun Sep 24 12:59:35 2017

@author: Rafael
"""

   
import smtplib
 
server = smtplib.SMTP('smtp.sendgrid.net', 587)
server.starttls()
server.login("apikey", "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")
 
msg = """From: Eu mesmo <nildelmo@gmail.com>
To: Eu tambem <lucas.k.kawamura@gmail.com>
Subject: Teste de e-mail SMTP

Bom dia!

Venho por meio desta dizer que seu e-mail foi enviado com sucesso.

Beijos.
"""
server.sendmail('nildelmo@gmail.com', 'lucas.k.kawamura@gmail.com', msg)
server.quit()