from excel_processor import load_excel_data
from vault_builder import create_full_vault
from config import config, USE_JS, CREATE_DASHBOARD
from logger import logger

def main():
    """Главный файл с улучшенной обработкой"""
    try:
        logger.info("🚀 Запуск генерации Obsidian vault")
        logger.info("=" * 50)
        
        # Загрузка данных
        logger.info("📊 Загружаем данные из Excel...")
        df = load_excel_data()
        
        # Генерация vault
        logger.info("🏗️ Создаем структуру vault...")
        create_full_vault(df, use_js=USE_JS)
        
        logger.info("=" * 50)
        logger.info("🎉 Генерация завершена успешно!")
        
    except Exception as e:
        logger.error(f"❌ Критическая ошибка: {e}")
        logger.exception("Детали ошибки:")
        return 1
    
    return 0

if __name__ == "__main__":
    exit(main())