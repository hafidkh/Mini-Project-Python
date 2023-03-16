email = input("Enter Your Email: ")
username = email[:email.index("@")]
domainname = email[email.index("@")+1:]
slice = "Your user name is '{}' and your domain name is '{}'".format(username,domainname)
print(slice)
