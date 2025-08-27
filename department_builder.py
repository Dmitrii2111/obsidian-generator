from pathlib import Path
from config import ENCODING
from file_utils import sanitize_filename
from room_builder import process_rooms
from js_loader import JSLoader

js_loader = JSLoader()

def create_department_readme(dept_folder, dept_name, floor_name, use_js):
    """Создает README отделения с JS"""
    readme_file = dept_folder / f"{dept_name}.md"
    
    js_content = js_loader.get_department_js(dept_name, use_js)
    
    content = f"""---
type: department
этаж: "{floor_name}"
отдел: "{dept_name}"
status: ❌ Не приступали
---

{js_content}
"""
    
    with open(readme_file, "w", encoding=ENCODING) as f:
        f.write(content)
    
    return readme_file

def process_department(floor_folder, dept_value, dept_group, floor_name, use_js):
    """Обрабатывает одно отделение"""
    from room_builder import get_safe_name
    
    dept_name = get_safe_name(dept_value, "Без_отдела")
    dept_folder = floor_folder / sanitize_filename(dept_name)
    dept_folder.mkdir(parents=True, exist_ok=True)
    
    print(f"  🏥 Обрабатываем отделение: {dept_name}")
    
    # Создаем помещения
    process_rooms(dept_folder, dept_name, dept_group)
    
    # Создаем README отделения
    readme_file = create_department_readme(dept_folder, dept_name, floor_name, use_js)
    
    return dept_name, readme_file