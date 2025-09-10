from datetime import datetime, date
from typing import Optional

def convert_to_date(date_str: str) -> Optional[date]:
    """Converte uma string no formato 'DD/MM/AAAA' para um objeto datetime."""
    try:
        return datetime.strptime(date_str, "%d/%m/%Y").date()
    except ValueError:
        return None