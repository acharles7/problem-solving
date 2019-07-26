# Given a list of emails, we send one email to each address in the list.
# How many different addresses actually receive mails?
import numpy as np
import matplotlib.pyplot as plt
import math

sin_wave = np.array([math.sin(x) for x in np.arange(200)])
plt.plot(sin_wave[:50])


X = []
Y = []

seq_len = 50
num_records = len(sin_wave) - seq_len

for i in range(num_records - 50):
    X.append(sin_wave[i:i+seq_len])
    Y.append(sin_wave[i+seq_len])


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
# print(numUniqueEmails(emails))
