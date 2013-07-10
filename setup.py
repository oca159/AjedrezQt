from ez_setup import use_setuptools
from setuptools import setup, find_packages

setup( name="AjedrezQt",
       version="1.0",
       description="Ajedrez sencillo hecho en PyQt4",
       author="Osvaldo Cordova Aburto",
       author_email="oca159@hotmail.es",
       license="GPL",
       scripts=["Gui.py"],
       py_modules=["Button","Servidor","Movimientos","Cliente"],
       packages=find_packages(),
       package_data={'': ['*.gif']},
       keywords="ajedrez"
)
