from excel_processor import load_excel_data
from vault_builder import create_full_vault
from config import VAULT_PATH

def main():
    """Главный файл с выбором режима"""
    print("🚀 Запуск генерации Obsidian vault")
    print("=" * 50)
    
    try:
        # Загрузка данных
        print("📊 Загружаем данные из Excel...")
        df = load_excel_data()
        print(f"✅ Данные загружены: {df.shape[0]} строк")
        
        # Выбор режима
        use_js_input = input("Использовать JavaScript? (y/n, по умолчанию y): ").lower().strip()
        use_js = not use_js_input.startswith('n') if use_js_input else True
        
        mode = "JavaScript" if use_js else "Simple Dataview"
        print(f"🔧 Режим: {mode}")
        
        # Генерация vault
        print("🏗️ Создаем структуру vault...")
        create_full_vault(df, use_js=use_js)
        
        print("=" * 50)
        print(f"🎉 Готово! Режим: {mode}")
        print(f"📁 Результат в: {VAULT_PATH}")
        
    except Exception as e:
        print(f"❌ Ошибка: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()