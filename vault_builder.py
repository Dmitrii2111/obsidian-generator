import pandas as pd
from pathlib import Path
from config import VAULT_PATH
from file_utils import clear_folder
from floor_builder import process_floor
from dashboard_builder import create_dashboard
from logger import logger

def create_full_vault(df, use_js=True):
    """Создает полную структуру vault - главный координатор"""
    try:
        # Очищаем папку
        clear_folder(VAULT_PATH)
        logger.info(f"Vault очищен: {VAULT_PATH}")
        
        # Проверяем есть ли данные
        if df.empty:
            logger.warning("Нет данных для обработки")
            return
        
        # Обрабатываем каждый этаж
        for floor_value, floor_group in df.groupby("ЭТАЖ", dropna=False):
            try:
                process_floor(floor_value, floor_group, VAULT_PATH, use_js)
            except Exception as e:
                logger.error(f"Ошибка обработки этажа {floor_value}: {e}")
                continue
        
        # Создаем дашборд
        try:
            create_dashboard(use_js)
            logger.info("Дашборд создан")
        except Exception as e:
            logger.error(f"Ошибка создания дашборда: {e}")
        
        logger.info(f"Генерация завершена! Файлы в: {VAULT_PATH}")
        
    except Exception as e:
        logger.error(f"Критическая ошибка: {e}")
        raise