def isMatch(p,s):
    if len(p) == 0 and len(s) == 0:
        return True

    if len(p) > 1 and p[0] == '*' and len(s) == 0:
        return False

    if (len(p) > 1 and p[0] == '?') or (len(p) != 0
        and len(s) !=0 and p[0] == s[0]):
        return isMatch(p[1:],s[1:])

    if len(p) !=0 and p[0] == '*':
        return isMatch(p[1:],s) or isMatch(p,s[1:])

    return False

def test(p, s):
    import time
    import psutil
    import os
    start = time.time()
    if isMatch(p, s):
        end = time.time()
        process = psutil.Process(os.getpid())
        print 'Memory requirements in bytes is:- ' + str(process.memory_info().rss)
        print 'runtime in seconds is:- ' + str(end - start)
        return True
    else:
        end = time.time()
        process = psutil.Process(os.getpid())
        print 'Memory requirements in bytes is:- ' + str(process.memory_info().rss)
        print 'runtime in seconds is:- ' + str(end - start)
        return False

print test("*","aa")
print ('###########')
print test("?a","cb")
print ('###########')
print test("*a*b","adceb")
print ('###########')
