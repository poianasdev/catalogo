# Catálogo LB Eletrônicos

Abra `index.html` para usar (funciona direto no computador). Sem fotos ele funciona igual, só com a inicial do nicho no lugar.

## 1. Baixar as fotos em alta qualidade
```
pip install requests pillow
python baixar_imagens.py
```
Pega a foto original na página de cada produto e cria as pastas `lote-01`, `lote-02`... ao lado do `index.html`, com 100 fotos cada (WebP, até 800px, ~40 KB por foto). Pode interromper e rodar de novo. Os que falharem ficam em `falhas.txt`.

## 2. Publicar grátis no GitHub Pages (só pelo navegador)
1. Descompacte o .zip. Crie uma conta e um repositório **público** (ex.: `catalogo`) no github.com.
2. Na página do repositório: **Add file > Upload files**. Arraste `index.html` e a pasta `data`. **Commit changes**.
3. **Settings > Pages > Deploy from a branch > `main` / `(root)` > Save**. Em 1 a 2 minutos o site fica em `https://SEU-USUARIO.github.io/catalogo/`.
4. Fotos: volte à página principal do repositório, **Add file > Upload files**, arraste **uma pasta `lote-XX`** e **Commit changes**. Repita para cada pasta. O GitHub aceita até 100 arquivos por envio, por isso cada pasta tem no máximo 100 fotos. Depois de cada envio o site leva cerca de 1 minuto para atualizar.

Atenção: em repositório público, qualquer pessoa com o link pode ver seus custos e fornecedor.

## Como usar
- Clique num produto, use **Buscar no Mercado Livre**, preencha preço médio, vendas/mês, concorrentes e frete. A margem aparece no card (verde = acima da meta, padrão 15%).
- **Taxas e backup**: ajuste comissão, taxa fixa, imposto e embalagem. Os valores iniciais são exemplos.
- Cada pessoa tem sua própria análise, salva no navegador dela. Use **Exportar CSV** ou o backup JSON para não perder dados.
