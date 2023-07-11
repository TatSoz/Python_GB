# ✔ Создайте функцию для сортировки файлов по директориям: видео, изображения, текст и т.п.
# ✔ Каждая группа включает файлы с несколькими расширениями.
# ✔ В исходной папке должны остаться только те файлы, которые не подошли для сортировки.


from pathlib import Path


def group_files(path):
    p = Path(path)
    for f in p.iterdir():
        for k, v in GROUPS.items():
            if f.suffix[1:] in v:
                save_path = Path(p / k)
                break
        else:
            save_path = Path(p / "misc")
        if not Path.exists(save_path):
            Path.mkdir(save_path)
        f.replace(save_path / f.name)


if __name__ == "__main__":
    GROUPS = {
        Path('video'): ['avi', 'mkv'],
        Path('image'): ['jpg', 'png', 'jpeg'],
        Path('text'): ['pdf', 'doc', 'txt'],
        Path('binary'): ['bin', 'dll'],
    }
    group_files('../../Files')




