######### Recieving Emails
import smtplib

smtp_object = smtplib.SMTP('smtp.gmail.com', 587)

smtp_object.ehlo()
# (250, b'smtp.gmail.com at your service, [31.205.216.221]\nSIZE 35882577\n8BITMIME\nSTARTTLS\nENHANCEDSTATUSCODES\nPIPELINING\nCHUNKING\nSMTPUTF8')

smtp_object.starttls()
# (220, b'2.0.0 Ready to start TLS')

# password = input('Enter your password')

import getpass

email = getpass.getpass('Email: ')
password = getpass.getpass('Password: ')

smtp_object.login(email,password)
# (235, b'2.7.0 Accepted')

from_address = email
to_address = 'kjwesley2002@gmail.com'

subject = input('enter subject line:')
message = input('ente the message: ')
msg_str = "Subject:"+subject+'\n'+message

smtp_object.sendmail(from_address,to_address,msg_str)

smtp_object.quit()
# (221, b'2.0.0 closing connection k8sm1144709wma.16 - gsmtp')

###### Recieving Emails

import imaplib
M = imaplib.IMAP4_SSL('imap.gmail.com')

email = input("Email: ")
password = getpass.getpass("Password: ")

M.login(email,password)
# ('OK', [b'johnwesleygithub@gmail.com authenticated (Success)'])

M.list()
# ('OK', [b'(\\HasNoChildren) "/" "INBOX"', b'(\\HasChildren \\Noselect) "/" "[Gmail]"', b'(\\All \\HasNoChildren) "/" "[Gmail]/All Mail"', b'(\\Drafts \\HasNoChildren) "/" "[Gmail]/Drafts"', b'(\\HasNoChildren \\Important) "/" "[Gmail]/Important"', b'(\\HasNoChildren \\Sent) "/" "[Gmail]/Sent Mail"', b'(\\HasNoChildren \\Junk) "/" "[Gmail]/Spam"', b'(\\Flagged \\HasNoChildren) "/" "[Gmail]/Starred"', b'(\\HasNoChildren \\Trash) "/" "[Gmail]/Trash"'])

M.select('inbox')
# ('OK', [b'77'])

typ, data = M.search(None,'SUBJECT "Nice Receive"')
# typ OK
# data [b'78']

email_id = data[0]
result , email_data = M.fetch(email_id,'(RFC822)')
email_data
# [(b'78 (RFC822 {4830}', b'Delivered-To: johnwesleygithub@gmail.com\r\nReceived: by 2002:a17:90a:bf90:0:0:0:0 with SMTP id d16csp2470655pjs;\r\n        Tue, 15 Sep 2020 14:19:52 -0700 (PDT)\r\nX-Received: by 2002:a05:651c:484:: with SMTP id s4mr7870937ljc.391.1600204792439;\r\n        Tue, 15 Sep 2020 14:19:52 -0700 (PDT)\r\nARC-Seal: i=1; a=rsa-sha256; t=1600204792; cv=none;\r\n        d=google.com; s=arc-20160816;\r\n        b=nQlEKAsUyUGvG1gRXNCDXOb8PWWbNKvBjTkUaHarxUtMZ3xLOUCJYfOn5UYFSOSt02\r\n         PFSbPCI3T5zZ3AHGrmNZ17AJ7uvf+mJZT3AuO05ywVurmpIsb6y0uqSphJH+lxnIW5TD\r\n         InzXeMfDVCtTBU36YnBsL41QRctWt4G8e1WrxXi4xHG70gWLMeFZq1nVfibhoECpj5sT\r\n         6F3glVEbB/OHqvVYfsMn+DG+Vm700LLhI5Ce4CqdywA41vlLIscNrBSnyMmbNYoQGg3e\r\n         txexH529XikyXbcpv5YqXzYF5kH8P6p0OBtJ5GznsEItTEWeqedfUZJMpSTI1MB7d1yQ\r\n         DjXA==\r\nARC-Message-Signature: i=1; a=rsa-sha256; c=relaxed/relaxed; d=google.com; s=arc-20160816;\r\n        h=to:subject:message-id:date:from:mime-version:dkim-signature;\r\n        bh=WfLaZrEV1dG73yT0aKdo2uxWEJG3e/ait7vM/gtpaa8=;\r\n        b=0R3r+Vnd4trJrckP9ia/1J315Mz9Lx16nthuOpguinoemiSe/OZ5YaSdJ1n0Cdy2DW\r\n         vIP+d5CaVCOLY++dzTWPYHxqomTYn3CMQsz8mS4KIMsTAPWxzj4y/ao0ShjdI4IJSYgC\r\n         wZILigT+mo1DfN9FHS4uRPBMX58rszvEYuUL/0MkXlTMu0KEpjzynQlLlmkTZGrQj5yq\r\n         eMOGrR0FS0rSRw2WE7M9VukjO6mYy9mErIuQXr5Ca8HdEF3FDhGEfd8M3n61M3rdxkAo\r\n         I5KO8ZDN7LryoKFuukE4HyFztNDr5Hwif7R7F9Tp50KdoNQ+e02oYA10uAgahdGO5gEK\r\n         Z6tw==\r\nARC-Authentication-Results: i=1; mx.google.com;\r\n       dkim=pass header.i=@gmail.com header.s=20161025 header.b=R6TrultB;\r\n       spf=pass (google.com: domain of kjwesley2002@gmail.com designates 209.85.220.41 as permitted sender) smtp.mailfrom=kjwesley2002@gmail.com;\r\n       dmarc=pass (p=NONE sp=QUARANTINE dis=NONE) header.from=gmail.com\r\nReturn-Path: <kjwesley2002@gmail.com>\r\nReceived: from mail-sor-f41.google.com (mail-sor-f41.google.com. [209.85.220.41])\r\n        by mx.google.com with SMTPS id e20sor2743460lfj.24.2020.09.15.14.19.52\r\n        for <johnwesleygithub@gmail.com>\r\n        (Google Transport Security);\r\n        Tue, 15 Sep 2020 14:19:52 -0700 (PDT)\r\nReceived-SPF: pass (google.com: domain of kjwesley2002@gmail.com designates 209.85.220.41 as permitted sender) client-ip=209.85.220.41;\r\nAuthentication-Results: mx.google.com;\r\n       dkim=pass header.i=@gmail.com header.s=20161025 header.b=R6TrultB;\r\n       spf=pass (google.com: domain of kjwesley2002@gmail.com designates 209.85.220.41 as permitted sender) smtp.mailfrom=kjwesley2002@gmail.com;\r\n       dmarc=pass (p=NONE sp=QUARANTINE dis=NONE) header.from=gmail.com\r\nDKIM-Signature: v=1; a=rsa-sha256; c=relaxed/relaxed;\r\n        d=gmail.com; s=20161025;\r\n        h=mime-version:from:date:message-id:subject:to;\r\n        bh=WfLaZrEV1dG73yT0aKdo2uxWEJG3e/ait7vM/gtpaa8=;\r\n        b=R6TrultBr4m121ZsTUFuU7R6tAR0e6/PIntgXUfelt80rdsnnixQl4W8XqyxvFrAf+\r\n         beT6j2mW93FkiUVxi15NbJ+xmfqJlYbPFR0osxuEJdWpnyeVZxBp4MNmz6RJgUsnmfKe\r\n         C2BKuCqQjYDYt4AR04pRCvjnWowj2JVEkhDPFjaT/qeYUWg9LNgSmszEBxeqhDTHEfuJ\r\n         1UEqtqLZuJVJzbmQBNcntSaSO6mAJDGnUd9g7PaLixbfVyMtgmN0vuMjdWkC5PPJD5rh\r\n         yu+AVT6o1UAAjRioQOCnsBlux9do6kiKv/QxNXWXpFWpW1LLI5xsB3GM0tZwcRkHXcm9\r\n         KX9g==\r\nX-Google-DKIM-Signature: v=1; a=rsa-sha256; c=relaxed/relaxed;\r\n        d=1e100.net; s=20161025;\r\n        h=x-gm-message-state:mime-version:from:date:message-id:subject:to;\r\n        bh=WfLaZrEV1dG73yT0aKdo2uxWEJG3e/ait7vM/gtpaa8=;\r\n        b=dZCjuEA607d4xtK5l6XQIu6kD1i7H05nW2VCeKXRVHeM5srvmAIfcQEKlnIx0bduUi\r\n         95S8BPG/5mSWsxmT6jzvtCS1wNuE7Ojm3OgqiqeRKrNtv0ju3d9dDtgObiKVYow2V4Ay\r\n         Izfy9XVd4oRr01Dtjj5WkBmOoQB1sLX2Lthcv696NneOMpEM27/3kCSAPMF8TvUkkdvA\r\n         Ys+XK5WzMxDO/eq3Zxs/vJn2U9HPzs+aIpT2zvmrwB8drlnzYNHXtiKw20MV/NizMFi+\r\n         nhOltBY7w2YnHfUBmJ88qPLOWtyoHK6ZXOafSP27OnF+sRY41X2mYBXT4/hXWeBbangc\r\n         xcpQ==\r\nX-Gm-Message-State: AOAM532UKIQp0SGHpMrApyc0FirTUAhbA/cG/GBLtCAF0HyNo8jy0A+7\r\n\tZTeCusRarUdm3gaKOWzqoz8YuWwMB7YTOPRD4vVN3tUUpCPxNg==\r\nX-Google-Smtp-Source: ABdhPJwlZ1fWzu+Fr4R9JqijDvWIXnaJTex2CpLt+5Wh74TwnYZu82XrfbQDkZnYKGG5sl48q9GhjI3W422OmyeV+UM=\r\nX-Received: by 2002:a19:8ad4:: with SMTP id m203mr7955318lfd.183.1600204791860;\r\n Tue, 15 Sep 2020 14:19:51 -0700 (PDT)\r\nMIME-Version: 1.0\r\nFrom: John Wesley <kjwesley2002@gmail.com>\r\nDate: Tue, 15 Sep 2020 22:19:41 +0100\r\nMessage-ID: <CAF2O3ozFq7zVz7JQjoK5R_e7-yvF7rsmUejCqzDPiV+3N3k9GA@mail.gmail.com>\r\nSubject: Nice Receive\r\nTo: "johnwesleygithub@gmail.com" <johnwesleygithub@gmail.com>\r\nContent-Type: multipart/alternative; boundary="0000000000002fcf5705af60b6de"\r\n\r\n--0000000000002fcf5705af60b6de\r\nContent-Type: text/plain; charset="UTF-8"\r\n\r\nTest email for receiving emails with python\r\n\r\n--0000000000002fcf5705af60b6de\r\nContent-Type: text/html; charset="UTF-8"\r\n\r\nTest email for receiving emails with python\r\n\r\n--0000000000002fcf5705af60b6de--\r\n'), b' FLAGS (\\Seen))']

raw_email = email_data[0][1]
raw_email_string = raw_email.decode('utf-8')
import email
email_message = email.message_from_string(raw_email_string)

for part in email_message.walk():
    if part.get_content_type() == 'text/plain':
        body = part.get_payload(decode=True)
        print(body)
# b'Test email for receiving emails with python\r\n'



