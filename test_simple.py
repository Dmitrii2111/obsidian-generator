from pathlib import Path
import pandas as pd
from config import EXCEL_PATH, SHEET_NAME, VAULT_PATH, ENCODING
from file_utils import sanitize_filename, clear_folder
from excel_processor import load_excel_data, check_data_structure
from content_generator import render_group_by_type

def test_excel_loading():
    """Тест 1: Загрузка Excel"""
    print("🧪 Тест 1: Загрузка Excel файла...")
    
    try:
        df = load_excel_data()
        print(f"✅ Успешно! Размер: {df.shape[0]} строк, {df.shape[1]} колонок")
        return df
    except Exception as e:
        print(f"❌ Ошибка: {e}")
        return None

def test_data_structure(df):
    """Тест 2: Проверка структуры данных"""
    print("\n🧪 Тест 2: Проверка структуры данных...")
    
    try:
        check_data_structure(df)
        print("✅ Все обязательные колонки присутствуют")
        
        # Покажем немного данных
        print(f"📋 Колонки: {list(df.columns)}")
        print(f"🏢 Этажи: {df['ЭТАЖ'].unique()}")
        print(f"🏥 Отделения: {df['ОТДЕЛ'].unique()[:3]}")  # Первые 3
        
        return True
    except Exception as e:
        print(f"❌ Ошибка: {e}")
        return False

def test_content_generation(df):
    """Тест 3: Генерация контента"""
    print("\n🧪 Тест 3: Генерация контента...")
    
    try:
        # Возьмем первую группу для теста
        first_floor = df['ЭТАЖ'].iloc[0] if not df.empty else None
        test_group = df[df['ЭТАЖ'] == first_floor].head(3)
        
        content = render_group_by_type(test_group)
        print(f"✅ Контент сгенерирован ({len(content)} символов)")
        print(f"📝 Превью: {content[:200]}...")
        
        return content
    except Exception as e:
        print(f"❌ Ошибка: {e}")
        return None

def test_file_creation(df, content):
    """Тест 4: Создание файлов"""
    print("\n🧪 Тест 4: Создание тестовых файлов...")
    
    try:
        # Очищаем папку
        clear_folder(VAULT_PATH)
        print(f"✅ Папка очищена: {VAULT_PATH}")
        
        # Создаем тестовый файл
        test_file = VAULT_PATH / "test_file.md"
        
        with open(test_file, "w", encoding=ENCODING) as f:
            f.write("# Тестовый файл\n\n")
            f.write("## Данные из Excel\n\n")
            f.write(content)
        
        print(f"✅ Файл создан: {test_file}")
        
        # Создаем структуру папок
        test_folder = VAULT_PATH / "test_folder"
        test_folder.mkdir(exist_ok=True)
        
        sub_file = test_folder / "sub_test.md"
        with open(sub_file, "w", encoding=ENCODING) as f:
            f.write("# Вложенный файл\n\nТест структуры папок")
        
        print(f"✅ Структура папок создана")
        
        return True
    except Exception as e:
        print(f"❌ Ошибка: {e}")
        return False

def main():
    """Главная функция тестирования"""
    print("🚀 Запуск комплексного тестирования...")
    print("=" * 50)
    
    # Тест 1: Загрузка Excel
    df = test_excel_loading()
    if df is None:
        return
    
    # Тест 2: Структура данных
    if not test_data_structure(df):
        return
    
    # Тест 3: Генерация контента
    content = test_content_generation(df)
    if content is None:
        return
    
    # Тест 4: Создание файлов
    if not test_file_creation(df, content):
        return
    
    print("\n" + "=" * 50)
    print("🎉 ВСЕ ТЕСТЫ ПРОЙДЕНЫ УСПЕШНО!")
    print("📁 Результаты в папке: output/test_vault")
    print("👉 Теперь можно запускать полную генерацию")

if __name__ == "__main__":
    main()