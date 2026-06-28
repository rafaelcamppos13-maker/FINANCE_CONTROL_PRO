from pathlib import Path
from openpyxl import Workbook

BASE = Path(__file__).parent
EXCEL = BASE / "excel"

EXCEL.mkdir(exist_ok=True)

arquivo = EXCEL / "FINANCE_CONTROL_PRO.xlsx"

wb = Workbook()

ws = wb.active
ws.title = "Dashboard"

ws["A1"] = "FINANCE CONTROL PRO"
ws["A3"] = "Sistema inicial criado com sucesso"

wb.save(arquivo)

print("Projeto criado:", arquivo)