import os, subprocess, getpass, sys, pathlib

try:
    import keyring  # pip install keyring
except ImportError:
    keyring = None

SERVICE = "elementary-mcp"
ACCOUNT = "token"
DEFAULT_URL = "http://localhost:8081/mcp/"


def get_token():
    # 1️⃣ try env var first
    token = os.getenv("ELEMENTARY_TOKEN")
    if token:
        return token.strip()

    # 2️⃣ try keychain
    if keyring:
        saved = keyring.get_password(SERVICE, ACCOUNT)
        if saved:
            return saved

    # 3️⃣ ask user
    token = getpass.getpass("Paste your Elementary MCP token: ").strip()
    if keyring:
        try:
            keyring.set_password(SERVICE, ACCOUNT, token)
        except Exception:
            pass
    else:
        cfg_dir = pathlib.Path.home() / ".config" / SERVICE
        cfg_dir.mkdir(parents=True, exist_ok=True)
        (cfg_dir / "token").write_text(token)
    return token


def main():
    token = get_token()
    url = os.getenv("ELEMENTARY_MCP_URL", DEFAULT_URL)

    args = [
        "npx",
        "-y",
        "mcp-remote@latest",
        url,
        "--header",
        f"Authorization:{token}",
    ] + sys.argv[1:]

    subprocess.run(args, check=False)


if __name__ == "__main__":
    main()
