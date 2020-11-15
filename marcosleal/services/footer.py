from datetime import datetime
from pathlib import Path

from pytz import timezone


def update_footer() -> str:
    timestamp = datetime.now(timezone('America/Sao_Paulo')).strftime(
        '%d/%m/%Y às %H:%M:%S'
    )

    footer = Path('FOOTER.md').read_text()
    return footer.format(timestamp=timestamp)
