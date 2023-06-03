import subprocess

if __name__ == '__main__':
## command line args along with error capture on failure with check true
      s = subprocess.run('py.test -m mallcz00 -v --html=\"./20230603_Mall_CZ_Test00.html\"',shell=True, check=True)
