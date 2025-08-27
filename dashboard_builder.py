from pathlib import Path
from config import VAULT_PATH, ENCODING
from js_loader import JSLoader

js_loader = JSLoader()

def create_dashboard(use_js=True):
    """Создает дашборд"""
    dashboard_file = VAULT_PATH / "DASHBOARD.md"
    
    js_content = js_loader.get_dashboard_js(use_js)
    
    content = f"""
type: dashboard
status: ❌ Не приступали
    
    # 📊 Дашборд отделений

{js_content}
"""
    
    with open(dashboard_file, "w", encoding=ENCODING) as f:
        f.write(content)
    
    print("📊 Создан дашборд")
    return dashboard_file