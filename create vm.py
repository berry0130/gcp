import os
for i in range (10):
    s='export INSTANCE_NAMES="vvmm"'+str(i)+';./vm.sh'
    os.system(s)
