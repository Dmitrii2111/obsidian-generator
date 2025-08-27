from pathlib import Path
import yaml

def load_config():
    """Загрузка конфигурации из YAML"""
    config_path = Path("config.yaml")
    
    if config_path.exists():
        try:
            with open(config_path, 'r', encoding='utf-8') as f:
                return yaml.safe_load(f)
        except Exception as e:
            print(f"⚠️ Ошибка загрузки config.yaml: {e}")
            print("🔄 Используем настройки по умолчанию")
    
    # Конфигурация по умолчанию если файла нет или ошибка
    return {
        'excel': {
            'path': 'testData.xlsx',
            'sheet_name': 'testSheet'
        },
        'vault': {
            'path': 'output/test_vault',
            'encoding': 'utf-8'
        },
        'generator': {
            'use_js': True,
            'create_dashboard': True,
            'log_level': 'INFO'
        },
        'columns': {
            'floor': 'ЭТАЖ',
            'department': 'ОТДЕЛ',
            'room': 'НОМ',
            'room_number': 'ПОМ',
            'room_name': 'ПОМ_НАИМ',
            'position': 'ПОЗ',
            'item_name': 'НАИМ',
            'supplier': 'ПОСТ',
            'quantity': 'КОЛ',
            'type': 'ТИП'
        }
    }

# Загружаем конфигурацию
config = load_config()

# Настройки с проверкой на None
EXCEL_PATH = config.get('excel', {}).get('path', 'testData.xlsx')
SHEET_NAME = config.get('excel', {}).get('sheet_name', 'testSheet')
VAULT_PATH = Path(config.get('vault', {}).get('path', 'output/test_vault'))
ENCODING = config.get('vault', {}).get('encoding', 'utf-8')
USE_JS = config.get('generator', {}).get('use_js', True)
CREATE_DASHBOARD = config.get('generator', {}).get('create_dashboard', True)
LOG_LEVEL = config.get('generator', {}).get('log_level', 'INFO')

# Column mappings
COLUMN_FLOOR = config.get('columns', {}).get('floor', 'ЭТАЖ')
COLUMN_DEPARTMENT = config.get('columns', {}).get('department', 'ОТДЕЛ')
COLUMN_ROOM = config.get('columns', {}).get('room', 'НОМ')
COLUMN_ROOM_NUMBER = config.get('columns', {}).get('room_number', 'ПОМ')
COLUMN_ROOM_NAME = config.get('columns', {}).get('room_name', 'ПОМ_НАИМ')
COLUMN_POSITION = config.get('columns', {}).get('position', 'ПОЗ')
COLUMN_ITEM_NAME = config.get('columns', {}).get('item_name', 'НАИМ')
COLUMN_SUPPLIER = config.get('columns', {}).get('supplier', 'ПОСТ')
COLUMN_QUANTITY = config.get('columns', {}).get('quantity', 'КОЛ')
COLUMN_TYPE = config.get('columns', {}).get('type', 'ТИП')