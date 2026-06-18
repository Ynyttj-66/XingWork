"""XingWork — LangGraph ReAct AI Agent Web 入口。"""

import uvicorn

from api.server import create_app
from memory.user_init import ensure_all
from version import __version__


def main():
    print(f"XingWork {__version__}")
    print()

    ensure_all()

    app = create_app()
    uvicorn.run(app, host="0.0.0.0", port=8000)


if __name__ == "__main__":
    main()
