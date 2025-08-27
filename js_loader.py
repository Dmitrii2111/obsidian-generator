from pathlib import Path
from config import ENCODING

class JSLoader:
    """Загрузчик JavaScript шаблонов"""
    
    def __init__(self, templates_dir="js_templates"):
        self.templates_dir = Path(templates_dir)

    
    def load_js_template(self, template_name):
        """Загружает JS шаблон из файла"""
        js_file = self.templates_dir / f"{template_name}.js"
        
        if not js_file.exists():
            return self.get_fallback_template(template_name)
        
        with open(js_file, "r", encoding=ENCODING) as f:
            return f.read()
    
    def get_fallback_template(self, template_name):
        """Fallback шаблоны если JS файлы отсутствуют"""
        if template_name == "room":
            return """// Простой шаблон для помещения
dv.span("⚠️ Room template not found");"""
        if template_name == "department":
            return """// Простой шаблон для отделения
const rooms = dv.pages().where(p => p.отдел === dv.current().file.name && p.помещение);
dv.table(["Помещение", "Статус"], rooms.map(p => [p.file.link, p.status]));"""
        
        elif template_name == "dashboard":
            return """// Простой шаблон для дашборда
const depts = dv.pages().where(p => p.отдел && !p.помещение);
dv.table(["Отделение", "Статус"], depts.map(p => [p.file.link, p.status]));"""
        
        return "// Шаблон не найден"
    
    def get_room_js(self, use_js=True):
            """Возвращает JS код для помещения"""
            if use_js:
                js_content = self.load_js_template("room")
                return f"```dataviewjs\n{js_content}\n```"
            else:
                return """```dataview
TABLE WITHOUT ID file.link AS "Файл", status AS "Статус"
WHERE file.name = this.file.name
```"""
    
    def get_department_js(self, dept_name, use_js=True):
        """Возвращает JS код для отделения"""
        if use_js:
            js_content = self.load_js_template("department")
            return f"```dataviewjs\n{js_content}\n```"
        else:
            return f"""```dataview
TABLE WITHOUT ID file.link AS "№", помещение AS "Помещение", status AS "Статус"
WHERE отдел = "{dept_name}" AND помещение
SORT file.name
```"""
    
    def get_dashboard_js(self, use_js=True):
        """Возвращает JS код для дашборда"""
        if use_js:
            js_content = self.load_js_template("dashboard")
            return f"```dataviewjs\n{js_content}\n```"
        else:
            return """```dataview
TABLE WITHOUT ID file.link AS "Отделение", status AS "Статус"
WHERE отдел AND NOT помещение
SORT этаж, отдел
```"""
    