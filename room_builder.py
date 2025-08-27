import pandas as pd
from pathlib import Path
from config import ENCODING
from file_utils import sanitize_filename
from content_generator import render_group_by_type

def get_safe_name(value, default):
    """Безопасное получение имени"""
    if value is None or (hasattr(pd, 'isna') and pd.isna(value)):
        return default
    return str(value)

def get_safe_value(value, default):
    """Безопасное получение значения"""
    if value is None or (hasattr(pd, 'isna') and pd.isna(value)):
        return default
    return str(value)

def get_room_name(row):
    """Получает название помещения"""
    room_num = get_safe_value(row.get("ПОМ"), "")
    room_name = get_safe_value(row.get("ПОМ_НАИМ", ""), "")
    
    if room_num and room_name:
        return f"{room_num} — {room_name}"
    elif room_num:
        return room_num
    else:
        return "—"

def create_room_file(room_file, dept_name, group_data):
    """Создает файл помещения"""
    first_row = group_data.iloc[0]
    
    floor = get_safe_value(first_row.get("ЭТАЖ"), "—")
    department = get_safe_value(first_row.get("ОТДЕЛ"), "—")
    room = get_room_name(first_row)
    
    content = render_group_by_type(group_data)
    
    md_content = f"""---
этаж: "{floor}"
отдел: "{department}"
помещение: "{room}"
status: ❌ Не приступали
---

{content}
[[{dept_name}]]
"""
    
    with open(room_file, "w", encoding=ENCODING) as f:
        f.write(md_content)
    
    return room_file

def process_rooms(dept_folder, dept_name, dept_group):
    """Создает помещения в отделении"""
    created_files = []
    
    for nom_value, group in dept_group.groupby("НОМ", dropna=False):
        room_name = get_safe_name(nom_value, "Без_кода")
        room_file = dept_folder / f"{sanitize_filename(room_name)}.md"
        
        create_room_file(room_file, dept_name, group)
        created_files.append(room_file)
        
        print(f"    🚪 Помещение: {room_name}")
    
    return created_files