# ========================
# VARIABLE ARGS LIST
# ========================

# The * in the *links parameter says, I’ll accept any number of arguments and put them 
# all in a tuple named links. If we supply only one argument, it will be a list with 
# one element; if we supply no arguments, it will be an empty list.  Thus, all these function calls are valid.

from urllib.parse import urlparse
from pathlib import Path

def get_pages(*links: str) -> None:
    for link in links:
        url = urlparse(link)
        name = "index.html" if url.path in ("", "/") else url.path
        target = Path(url.netloc.replace(".", "_")) / name
        print(f"Create {target} from {link!r}")

get_pages('https://www.archlinux.org','https://dusty.phillips.codes','https://itmaybeahack.com')
