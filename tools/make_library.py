"""產生網站的模型目錄 library.json（GitHub Actions 每次部署前自動跑，不用手改）。

規則（跟本機 serve.py 的模型庫一樣）：
- models/ 裡每個 .glb 是一個模型；同名 .meta.json 放標題、說明、預設清單（preset）。
- 同名 .landmarks/ 資料夾裡的每個 .json 是一份標註（檔名＝標註名稱）。上傳同名檔就是替換。
- 標成 sensitive（大體老師資料）的模型一律拒絕：這是公開網站。

用法：python tools/make_library.py
"""
import json
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
MODELS = ROOT / 'models'


def read_json(path):
    try:
        return json.loads(path.read_text(encoding='utf-8-sig'))
    except (OSError, ValueError):
        return None


def main():
    entries, problems = [], []
    for glb in sorted(MODELS.glob('*.glb')):
        meta = read_json(glb.with_suffix('.meta.json')) or {}
        if meta.get('sensitive'):
            sys.exit(f'拒絕：{glb.name} 標成敏感資料（大體老師），不能放上公開網站。')
        sets = []
        folder = glb.with_name(glb.stem + '.landmarks')
        for file in sorted(folder.glob('*.json')) if folder.is_dir() else []:
            doc = read_json(file)
            if not isinstance(doc, dict) or not isinstance(doc.get('landmarks'), dict):
                problems.append(f'{file.relative_to(ROOT)}：不是標註器「存成 JSON」的檔案，略過')
                continue
            sets.append({'name': file.stem, 'count': len(doc['landmarks']), 'savedAt': doc.get('exportedAt'),
                         'annotator': doc.get('annotator', ''), 'file': file.relative_to(ROOT).as_posix()})
        entries.append({'id': glb.stem, 'source': 'web', 'fileName': glb.name, 'sizeMB': round(glb.stat().st_size / 1e6, 1),
                        'title': meta.get('title') or glb.stem, 'description': meta.get('description', ''),
                        'preset': meta.get('preset', 'skull'), 'sensitive': False,
                        'file': glb.relative_to(ROOT).as_posix(), 'landmarkSets': sets})
    (ROOT / 'library.json').write_text(json.dumps(entries, ensure_ascii=False, indent=1), encoding='utf-8')
    for problem in problems:
        print('注意：' + problem)
    print(f'library.json：{len(entries)} 個模型、{sum(len(e["landmarkSets"]) for e in entries)} 份標註')


if __name__ == '__main__':
    main()
