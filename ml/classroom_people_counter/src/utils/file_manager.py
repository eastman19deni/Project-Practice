from pathlib import Path

def ensure_dirs(cfg):
    paths = cfg.get('paths', {})
    for k,v in paths.items():
        Path(v).mkdir(parents=True, exist_ok=True)
