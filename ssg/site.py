from pathlib import Path

class Site:
    """class on site, checking on git status."""

    def __init__(self, source, dest):
        self.source = Path(source)
        self.dest = Path(dest)
