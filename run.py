import os,sys,platform
bit = platform.architecture()[0]
if bit == '64bit':
    os.system('chmod +x ffg')
    os.system('./ffg')
elif bit == '32bit':
    os.system('chmod +x ffg32')
    os.system('./ffg32')
else:
    print('device not supported')
