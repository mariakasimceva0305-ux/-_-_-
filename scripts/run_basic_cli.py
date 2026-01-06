"""
CLI скрипт для запуска базового геокодера.
"""

import sys
import json
from pathlib import Path

# Добавляем корневую директорию в путь
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from src.geocode_basic import geocode_basic


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Использование: python scripts/run_basic_cli.py <адрес>")
        print('Пример: python scripts/run_basic_cli.py "Москва, Тверская улица, 12к1"')
        sys.exit(1)
    
    query = " ".join(sys.argv[1:])
    res = geocode_basic(query)
    print(json.dumps(res, ensure_ascii=False, indent=2))

