import os
pwdPath=os.path.abspath('..')+'\\emailConfig.txt'
print pwdPath
f=open(pwdPath)
gmail_pwd = f.read()
print gmail_pwd
