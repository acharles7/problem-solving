
def stack_problem(locks):
    stack, visited = [], set()
    for i, lock in enumerate(locks, start=1):
        action, number = lock.split(' ')
        if action == 'ACQUIRE':
            if number not in visited:
                stack.append(number)
                visited.add(number)
            else:
                print("Already Acquired", i)
                return i
        else:
            if stack and number == stack[-1]:
                stack.pop()
                visited.remove(number)
            else:
                print('Can not released', i)
                return i
    if stack:
        return len(locks) + 1
    return 0


locks1 = ['ACQUIRE 123', 'ACQUIRE 364', 'ACQUIRE 84', 'RELEASE 84',
          'RELEASE 364', 'ACQUIRE 789','RELEASE 456','RELEASE 123']
locks2 = ['ACQUIRE 364', 'ACQUIRE 84', 'ACQUIRE 364', 'RELEASE 364']
locks3 = ['ACQUIRE 364', 'ACQUIRE 84', 'RELEASE 84',
          'ACQUIRE 1337', 'RELEASE 1337', 'RELEASE 364']
locks4 = ['ACQUIRE 364', 'ACQUIRE 84', 'RELEASE 364']
locks5 = ['ACQUIRE 364', 'ACQUIRE 84', 'RELEASE 84', 'RELEASE 364', 'RELEASE 440']
locks6 = ['ACQUIRE 364', 'ACQUIRE 84', 'RELEASE 84', 'RELEASE 364', 'ACQUIRE 614']
print("Ans: ", stack_problem(locks6))
