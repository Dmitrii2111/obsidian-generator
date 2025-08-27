import pandas as pd
import re

def oneline(s: str) -> str:
    """Убираем переносы строк"""
    return re.sub(r'[\r\n]+', ' ', str(s)).strip()

def render_group_by_type(group_df: pd.DataFrame) -> str:
    """Простая генерация контента"""
    out = []
    
    # Заполняем NaN
    group_df = group_df.fillna("—")
    
    # Простая таблица
    out.append("| ПОЗ | Название | Поставщик | Кол-во |\n")
    out.append("|---|---|---|---|\n")
    
    for _, row in group_df.iterrows():
        out.append(
            f"| {row.get('ПОЗ', '—')} | {row.get('НАИМ', '—')} | "
            f"{row.get('ПОСТ', '—')} | {row.get('КОЛ', '—')} |\n"
        )
    
    out.append("\n")
    
    # Чеклист
    for _, row in group_df.iterrows():
        poz = oneline(row.get('ПОЗ', '—'))
        naim = oneline(row.get('НАИМ', '—'))
        out.append(f"- [ ] {poz} — {naim}\n")
    
    return "".join(out)