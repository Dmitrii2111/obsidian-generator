import pandas as pd
from pathlib import Path
from config import EXCEL_PATH, SHEET_NAME, COLUMN_FLOOR, COLUMN_DEPARTMENT, COLUMN_ROOM
from logger import logger

def load_excel_data():
    """Загрузка и валидация Excel файла"""
    try:
        if not Path(EXCEL_PATH).exists():
            raise FileNotFoundError(f"Файл не найден: {EXCEL_PATH}")
        
        logger.info(f"Загружаем Excel: {EXCEL_PATH}, лист: {SHEET_NAME}")
        df = pd.read_excel(EXCEL_PATH, sheet_name=SHEET_NAME)
        
        # Валидация данных
        validate_dataframe(df)
        
        logger.info(f"Данные загружены: {df.shape[0]} строк, {df.shape[1]} колонок")
        return df
        
    except Exception as e:
        logger.error(f"Ошибка загрузки Excel: {e}")
        raise

def validate_dataframe(df):
    """Валидация структуры DataFrame"""
    required_columns = [COLUMN_FLOOR, COLUMN_DEPARTMENT, COLUMN_ROOM, 'ПОМ', 'ПОЗ', 'НАИМ']
    
    missing_columns = [col for col in required_columns if col not in df.columns]
    if missing_columns:
        raise ValueError(f"Отсутствуют обязательные колонки: {missing_columns}")
    
    # Проверяем наличие данных
    if df.empty:
        raise ValueError("Excel файл пустой")
    
    # Логируем информацию о данных
    logger.info(f"Колонки: {list(df.columns)}")
    logger.info(f"Этажи: {df[COLUMN_FLOOR].unique()}")
    logger.info(f"Количество отделений: {df[COLUMN_DEPARTMENT].nunique()}")