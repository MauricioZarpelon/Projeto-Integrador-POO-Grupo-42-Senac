import sys
path = '/home/Darkmave/Projeto-Integrador-POO-Grupo-42-Senac'
if path not in sys.path:
    sys.path.append(path)

from app import app as application
