# Catálogo LB Eletrônicos

Abra `index.html` para usar (funciona direto no computador). Sem fotos ele funciona igual, só com a inicial do nicho no lugar.

## 1. Baixar as fotos em alta qualidade
```
pip install requests pillow
python baixar_imagens.py
```
Pega a foto original na página de cada produto e salva em `imagens/` (WebP, até 800px, ~40 KB cada). Pode interromper e rodar de novo. Os que falharem ficam em `falhas.txt`.

## 2. Publicar grátis no GitHub Pages
1. Crie uma conta e um repositório **público** (ex.: `catalogo`) no github.com.
2. Envie a pasta inteira com o **GitHub Desktop** (ou `git add . && git commit -m catalogo && git push`). O upload pelo navegador limita a 100 arquivos por vez, então não serve para as ~2.200 fotos.
3. No repositório: Settings > Pages > Branch `main`, pasta `/ (root)` > Save.
4. Em ~1 minuto o site fica em `https://SEU-USUARIO.github.io/catalogo/`.

Atenção: em repositório público, qualquer pessoa com o link pode ver seus custos e fornecedor.

## Como usar
- Clique num produto, use **Buscar no Mercado Livre**, preencha preço médio, vendas/mês, concorrentes e frete. A margem aparece no card (verde = acima da meta, padrão 15%).
- **Taxas e backup**: ajuste comissão, taxa fixa, imposto e embalagem. Os valores iniciais são exemplos.
- Cada pessoa tem sua própria análise, salva no navegador dela. Use **Exportar CSV** ou o backup JSON para não perder dados.
