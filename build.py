from pathlib import Path

def build():
    output_dir = Path("dist")
    output_dir.mkdir(exist_ok=True)
    file = output_dir / "app.txt"
    file.write_text("Build successful!")

if __name__ == "__main__":
    build()