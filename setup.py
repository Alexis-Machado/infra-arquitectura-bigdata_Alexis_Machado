from setuptools import setup, find_packages

setup(
    name="infra-arquitectura-bigdata_Alexis_Machado",
    version="1.0.1",
    author="Jhon Alexis Machado Rodriguez",
    author_email="jmachadoa12@gmail.com",
    description="EA1 Proyecto integrador: Ingesta de datos desde un API a SQLite y Muestra en Excel. 🚀",
    py_modules=["EA1_Ingestión_Datos_API"],
    install_requires=[
        'requests',
        "pandas",
        "openpyxl"
    ]
)