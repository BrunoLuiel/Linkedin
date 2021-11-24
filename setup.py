###Usar esta aplicação para criar o executavel - APENAS

import sys
from cx_Freeze import setup, Executable

base = None
if sys.platform == 'win32':
    base = 'Win32GUI'

executables = [
    Executable('app.py', base=base)
]

includefiles = ['Linkedin.py', 'geckodriver.exe']
#packages = [insira aqui a lib] #Caso queira importar alguma lib externa basta usar este código

setup(
    name='Linkedin bot',
    version='1.0',
    description='Aplicativo que cria conexões automaticamente no Linkedin',
    options = {'build_exe':{'include_files':includefiles}}, #Este 'include_files' é regra do cx-freeze para  incluir arquivos
    executables=executables
)