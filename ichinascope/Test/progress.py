import time
import sys


def update_progress(progress):
    barLength = 50 # Modify this to change the length of the progress bar
    status = ''
    if isinstance(progress, int):
        progress = float(progress)
    if not isinstance(progress, float):
        progress = 0
        status = "error: progress var must be float\r\n"
    # if progress < 0:
    #     progress = 0
    #     status = "Halt...\r\n"
    if progress >= 1:
        progress = 1
        status = "Done...\r\n"
    block = int(round(barLength*progress))
    text = "\rPercent: [{0}] {1}% {2}".format( "#"*block + "-"*(barLength-block), progress*100, status)
    sys.stdout.write(text)
    sys.stdout.flush()


# update_progress test script


print ""
print "progress : 0->1"
# for i in range(101):
#     time.sleep(0.1)
#     update_progress(i/100.0)
#
# update_progress(100000)

for i in range(101):
    time.sleep(0.1)
    update_progress(i/100.0)

print ""
print "Test completed"



import tick
# for i in range(2):
#     print '\r',i,
#     sys.stdout.flush()
#     time.sleep(0.5)
# print ''
# time.sleep(2)
# print '---------'

ticklen = len(tick.tick)
for ticki in tick.tick:
    print '\r',tick.tick.index(ticki),'/',ticklen,
    sys.stdout.flush()
    time.sleep(0.5)
