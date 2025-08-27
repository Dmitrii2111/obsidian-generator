#!/usr/bin/env python3
"""
Скрипт проверки установки всех компонентов
"""

def check_installation():
    print("🔍 Проверка установки компонентов...")
    print("=" * 50)
    
    # Проверяем Python
    import sys
    print(f"🐍 Python версия: {sys.version}")
    
    # Проверяем основные модули
    modules_to_check = ['pandas', 'openpyxl', 'xlrd', 'pathlib']
    
    for module in modules_to_check:
        try:
            __import__(module)
            print(f"✅ {module}: Установлен")
        except ImportError:
            print(f"❌ {module}: НЕ установлен")
    
    # Проверяем версию pandas
    try:
        import pandas as pd
        print(f"📊 pandas версия: {pd.__version__}")
    except ImportError:
        print("❌ pandas: Требуется установка")
    
    print("=" * 50)
    
    # Рекомендации по установке
    print("\n💡 Если есть ошибки, выполните:")
    print("pip install pandas openpyxl xlrd")
    print("или")
    print("pip install -r requirements.txt")

if __name__ == "__main__":
    check_installation()