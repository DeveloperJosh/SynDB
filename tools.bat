0<0# : ^
''' 
@echo off
echo SynDB Tools
python "%~f0" %*
exit /b 0
'''

from main import main

if __name__ == '__main__':
    main()