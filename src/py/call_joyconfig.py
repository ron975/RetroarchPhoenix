import subprocess as subp
import os
import shlex
import win32_check

def call():
    if win32_check.check() == False:
        subp.Popen(shlex.split('gnome-terminal -x bash -c "/usr/bin/retroarch-joyconfig"'))
        return '*nix terminal opened'
    else:
        root_dir = os.path.dirname(os.path.realpath(__file__))
        joy_path = root_dir + '\\retroarch_v1.0\\retroarch-joyconfig.exe'
        subprocess.call(joy_path)
        return 'Windows terminal opened'
