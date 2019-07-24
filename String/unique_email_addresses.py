# Given a list of emails, we send one email to each address in the list.
# How many different addresses actually receive mails? 

def numUniqueEmails(emails):
    output =  set()
    for email in emails:
        final_email = ""
        local, domain = email.split('@')
        for dot in local.split('+')[0].split('.'):
            final_email += dot
        output.add(final_email+'@'+domain)
    print(output)
    return len(output)

emails = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
print(numUniqueEmails(emails))
