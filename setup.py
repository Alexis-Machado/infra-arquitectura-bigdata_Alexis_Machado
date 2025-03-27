from setuptools import setup, find_packages

setup(
    name="infra-arquitectura-bigdata_Alexis_Machado",
    version="3.0.0",
    author="Jhon Alexis Machado Rodriguez",
    author_email="jmachadoa12@gmail.com",
    description="EA3 Proyecto Integrador: Enriquecimiento de Datos simulando una Plataforma de Big Data en la Nube. 🔍🚀",
    py_modules=["EA3_Enriquecimiento_de_Datos_simulando_una_Plataforma_de_Big_Data_en_la_Nube"],
    install_requires=[
        'requests',
        "pandas",
        "openpyxl"
    ]
)
