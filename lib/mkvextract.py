"""Wrappers around the mkvextract command-line tool."""


import subprocess


def MkvExtract():
    with subprocess.Popen(['mkvextract', '-h'], stdout=subprocess.PIPE) as mkvextract_process:
        out = mkvextract_process.communicate()[0]
        print(out)
        assert mkvextract_process.returncode == 0


if __name__ == '__main__':
    MkvExtract()
