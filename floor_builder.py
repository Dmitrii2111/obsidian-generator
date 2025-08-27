from pathlib import Path
from config import ENCODING
from file_utils import sanitize_filename
from department_builder import process_department
from room_builder import get_safe_name

def create_floor_readme(floor_folder, floor_name, dept_links):
    """Создает README этажа"""
    if not dept_links:
        return None
    
    readme_file = floor_folder / f"Содержание_{floor_name}.md"
    
    with open(readme_file, "w", encoding=ENCODING) as f:
        f.write(f"# Этаж {floor_name}\n\n")
        f.write("## Отделения:\n\n")
        f.write("\n".join(dept_links))
    
    return readme_file

def process_floor(floor_value, floor_group, floor_path, use_js):
    """Обрабатывает один этаж"""
    floor_name = get_safe_name(floor_value, "Без_этажа")
    floor_folder = floor_path / sanitize_filename(floor_name)
    floor_folder.mkdir(parents=True, exist_ok=True)
    
    print(f"🏢 Обрабатываем этаж: {floor_name}")
    
    dept_links = []
    
    # Обрабатываем каждое отделение на этаже
    for dept_value, dept_group in floor_group.groupby("ОТДЕЛ", dropna=False):
        dept_name, _ = process_department(floor_folder, dept_value, dept_group, floor_name, use_js)
        dept_links.append(f"- [[{dept_name}/{dept_name}]]")
    
    # Создаем README этажа
    readme_file = create_floor_readme(floor_folder, floor_name, dept_links)
    
    return floor_folder, readme_file