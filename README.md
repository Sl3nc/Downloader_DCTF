# Downloader DCTF

## Descrição

O **Downloader DCTF** é uma aplicação automatizada desenvolvida em Python para facilitar o download em massa de arquivos DCTF WEB diretamente do portal ECAC da Receita Federal. O sistema utiliza automação de interface gráfica e manipulação de navegador para realizar buscas, preencher filtros e baixar os arquivos de forma segura e eficiente, minimizando a intervenção manual do usuário.

## Funcionalidades

- Interface gráfica intuitiva baseada em PySide6 (Qt).
- Automação do navegador Google Chrome para acesso ao ECAC.
- Preenchimento automático de filtros de pesquisa e datas.
- Download automático de todos os arquivos DCTF WEB disponíveis no período selecionado.
- Seleção do diretório de download pelo usuário.
- Controle de etapas com instruções detalhadas para o usuário.
- Manipulação automática da resolução de tela para garantir compatibilidade.
- Execução em thread separada para manter a interface responsiva.
- Mensagens de aviso, confirmação e conclusão do processo.

## Estrutura dos Arquivos

- `src/main.py`: Interface gráfica principal e orquestração do fluxo.
- `src/worker.py`: Worker responsável pela execução do download em thread separada.
- `src/step.py`: Gerenciamento das etapas e instruções do fluxo.
- `src/browser.py`: Automação do navegador Chrome e manipulação de downloads.
- `src/screen.py`: Manipulação da resolução de tela e posicionamento de janelas.
- `imgs/`: Imagens utilizadas para reconhecimento visual na automação.
- `json/instructions.json`: Arquivo JSON com as instruções e etapas do fluxo.

## Requisitos

- Python 3.8+
- Google Chrome instalado no caminho padrão do Windows.
- Dependências Python:
  - PySide6
  - pyautogui
  - pygetwindow
  - python-dateutil
  - pywin32

## Instalação

1. Clone este repositório:
   ```
   git clone https://github.com/seuusuario/Downloader_DCTF.git
   ```
2. Instale as dependências:
   ```
   pip install -r requirements.txt
   ```
3. Execute o programa:
   ```
   python src/main.py
   ```

## Uso

1. Abra o programa.
2. Siga as instruções exibidas na interface.
3. Selecione o período desejado e o diretório para salvar os arquivos.
4. Aguarde a automação concluir o download.
5. Ao final, a pasta de download será aberta automaticamente.

## Observações

- Não utilize o mouse ou teclado durante a execução automática para evitar falhas na automação.
- Caso ocorra algum erro, siga as instruções exibidas e reinicie o processo se necessário.

---
