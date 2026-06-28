from core.estilos import *
"""
FINANCE CONTROL PRO
Módulo responsável por criar a estrutura inicial do arquivo Excel.
"""

import os
from openpyxl import Workbook
from config import APP_NAME, VERSION, EXCEL_FILE, SHEETS


class BancoExcel:

    def __init__(self):
        self.workbook = Workbook()

    def criar_planilhas(self):
        """
        Cria todas as abas do sistema.
        """

        # Renomeia a primeira aba
        self.workbook.active.title = SHEETS[0]

        # Cria as demais
        for aba in SHEETS[1:]:
            self.workbook.create_sheet(title=aba)

    def salvar(self):

        pasta = os.path.dirname(EXCEL_FILE)

        if pasta:
            os.makedirs(pasta, exist_ok=True)

        self.workbook.save(EXCEL_FILE)

    def criar(self):

        self.criar_planilhas()

        self.salvar()

        print("=" * 60)
        print(APP_NAME)
        print("Versão:", VERSION)
        print("Arquivo criado com sucesso.")
        print(EXCEL_FILE)
        print("=" * 60)