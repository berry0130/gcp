import os
for i in range (10):
    s='export INSTANCE_NAMES="vm"'+str(i)+';./vm.sh'
    os.system(s)