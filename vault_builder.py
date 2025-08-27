import pandas as pd
from pathlib import Path
from config import VAULT_PATH
from file_utils import clear_folder
from floor_builder import process_floor
from dashboard_builder import create_dashboard

def create_full_vault(df, use_js=True):
    """Создает полную структуру vault - главный координатор"""
    # Очищаем папку
    clear_folder(VAULT_PATH)
    print(f"✅ Vault очищен: {VAULT_PATH}")
    
    # Проверяем есть ли данные
    if df.empty:
        print("⚠️ Нет данных для обработки")
        return
    
    # Обрабатываем каждый этаж
    for floor_value, floor_group in df.groupby("ЭТАЖ", dropna=False):
        process_floor(floor_value, floor_group, VAULT_PATH, use_js)
    
    # Создаем дашборд
    create_dashboard(use_js)
    
    print(f"🎉 Генерация завершена! Файлы в: {VAULT_PATH}")