"""
CLI скрипт для запуска оценки качества геокодеров.
"""

import sys
from pathlib import Path

# Добавляем корневую директорию в путь
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from src.evaluate import main


if __name__ == "__main__":
    main()

