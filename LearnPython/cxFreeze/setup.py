from cx_Freeze import setup, Executable

includes = ['re','urllib.request','urllib.parse']

setup(name='urlExe',
      version='0.1',
      description='parse stuff',
      executables=[Executable('cxFreezeExecutable.py')])

