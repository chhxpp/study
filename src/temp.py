from pathlib import Path
import shutil

base_dir = Path(__file__).parent.parent / 'test/'

for f in base_dir.rglob('*'):
    if f.is_file():
        ext = f.suffix[1:]  # 获取扩展名（不带点）
        if ext:  # 有扩展名
            target_dir = base_dir / ext
            target_dir.mkdir(exist_ok=True)
            target_file = target_dir / f.name
            shutil.move(str(f), str(target_file))