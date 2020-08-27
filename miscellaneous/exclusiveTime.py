'''
Leetcode 636: Exclusive Time of Functions
'''

def exclusive_time(n, logs):
    out = [0]*n
    stack = []
    for log in logs:
        fid, status, time = log.split(':')
        fid time = int(fid), int(time)

        if status == 'start':
            stack.append([fid,time])

        else:
            v = time - stack.pop()[1] + 1
            out[fid] += v

            if stack:
                out[stack[-1][0]] -= v 
    return out
    
n, logs = 3, ["0:start:0", "1:start:2", "1:end:5", "2:start:6", "2:end:9", "0:end:12"]
exclusive_time(n, logs)
