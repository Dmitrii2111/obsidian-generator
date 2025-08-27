import re
import shutil
from pathlib import Path

def sanitize_filename(name: str) -> str:
    """Безопасное имя файла"""
    if name is None or str(name).lower() in ['nan', 'none', '']:
        return "Без_названия"
    
    name = str(name)
    name = re.sub(r'[\\/*?:"<>|]', "", name)
    name = name.replace(" ", "_").strip()
    return name[:50]  # Ограничиваем длину

def clear_folder(path: Path):
    """Очистка папки"""
    if path.exists():
        for item in path.iterdir():
            if item.is_dir():
                shutil.rmtree(item, ignore_errors=True)
            else:
                try:
                    item.unlink()
                except:
                    pass
    else:
        path.mkdir(parents=True, exist_ok=True)