import pandas as pd
from pathlib import Path
from config import EXCEL_PATH, SHEET_NAME

def load_excel_data():
    """Простая загрузка Excel"""
    if not Path(EXCEL_PATH).exists():
        raise FileNotFoundError(f"Файл не найден: {EXCEL_PATH}")
    
    return pd.read_excel(EXCEL_PATH, sheet_name=SHEET_NAME)

def check_data_structure(df):
    """Проверка структуры данных"""
    required_columns = ['ЭТАЖ', 'ОТДЕЛ', 'НОМ', 'ПОМ', 'ПОЗ', 'НАИМ']
    missing = [col for col in required_columns if col not in df.columns]
    
    if missing:
        raise ValueError(f"Отсутствуют колонки: {missing}")
    
    return True