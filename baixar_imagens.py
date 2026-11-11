"""Baixa a foto original de cada produto (página do fornecedor) e salva em lote-XX/<id>.webp (até 800px, 100 fotos por pasta).
Uso: pip install requests pillow  &&  python baixar_imagens.py   (pode interromper e rodar de novo: continua de onde parou)"""
import io, json, pathlib, re, time, concurrent.futures as cf
import requests
from PIL import Image
ROOT = pathlib.Path(__file__).parent
P = json.loads((ROOT / "data/products.js").read_text(encoding="utf-8").split("=", 1)[1].strip().rstrip(";"))
H = {"User-Agent": "Mozilla/5.0 (catalogo pessoal)"}
def img_url(page):
    t = requests.get(page, headers=H, timeout=25).text
    m = re.search(r'property=["\']og:image["\'][^>]*content=["\']([^"\']+)', t) or re.search(r'content=["\']([^"\']+)["\'][^>]*property=["\']og:image', t)
    if not m: raise ValueError("sem og:image")
    u = m.group(1).replace("&amp;", "&"); u = "https:" + u if u.startswith("//") else u
    return re.sub(r"([?&])width=\d+&?", r"\1", re.sub(r"_\d*x\d*(?=\.\w+)", "", u))  # tira sufixo de miniatura
def run(p):
    f = ROOT / f"lote-{p['lote']}" / f"{p['id']}.webp"; f.parent.mkdir(exist_ok=True)
    if f.exists(): return None
    for t in range(3):
        try:
            im = Image.open(io.BytesIO(requests.get(img_url(p["url"]), headers=H, timeout=30).content))
            im = im.convert("RGBA" if im.mode in ("RGBA", "LA", "P") else "RGB"); im.thumbnail((800, 800))
            im.save(f, "WEBP", quality=82, method=6); return None
        except Exception as e: err = e; time.sleep(2 * (t + 1))
    return f"{p['nome'][:60]} | {p['url']} | {err}"
falhas = []
with cf.ThreadPoolExecutor(6) as ex:
    for i, r in enumerate(ex.map(run, P), 1):
        if r: falhas.append(r)
        if i % 100 == 0: print(f"{i}/{len(P)} (falhas: {len(falhas)})", flush=True)
(ROOT / "falhas.txt").write_text("\n".join(falhas), encoding="utf-8"); print("Pronto. Falhas:", len(falhas), "(veja falhas.txt)")
