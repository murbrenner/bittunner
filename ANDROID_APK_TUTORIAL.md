# Tutorial: Build APK Automático com GitHub Actions

Este tutorial explica como configurar o GitHub para fazer o build automático do APK Android do BitTuner.

## Por que GitHub Actions?

- **Gratuito** para repositórios públicos
- **Automático** - build acontece quando você faz push
- **Sem WSL** - roda em Linux na nuvem
- **Download fácil** - APK disponível como artefato
- **Histórico** - mantém versões anteriores

## Passo 1: Preparar o Repositório

### 1.1 Estrutura do Repositório

Seu repositório deve ter esta estrutura:

```
bittuner/
├── app_kivy.py              # App Kivy
├── requirements.txt        # Dependências
├── README.md              # Documentação
├── .github/
│   └── workflows/
│       └── build-apk.yml  # Workflow GitHub Actions
└── .gitignore             # Arquivos ignorados
```

### 1.2 Arquivos Necessários

Todos os arquivos já estão na pasta `bittuner-github` na sua Área de Trabalho.

## Passo 2: Criar Repositório no GitHub

1. Acesse https://github.com/new
2. Repository name: `bittuner`
3. Marque **Public** (necessário para GitHub Actions gratuito)
4. **NÃO** marque "Add a README file"
5. Clique em **Create repository**

## Passo 3: Upload dos Arquivos pela Web

### 3.1 Criar app_kivy.py

1. Clique em **"creating a new file"**
2. Nome: `app_kivy.py`
3. Cole o conteúdo do arquivo: `C:\Users\Murilo Brenner\Desktop\bittuner-github\app_kivy.py`
4. Commit: "Add app_kivy.py"

### 3.2 Criar requirements.txt

1. Clique em **"Add file"** → **"Create new file"**
2. Nome: `requirements.txt`
3. Conteúdo:

```
yt-dlp>=2024.1.1
faster-whisper>=1.0.0
certifi>=2023.7.22
kivy[base]>=2.1.0
buildozer>=1.4.0
cython>=3.0.0
pyjnius>=1.6.1
```

4. Commit: "Add requirements.txt"

### 3.3 Criar .github/workflows/build-apk.yml

1. Clique em **"Add file"** → **"Create new file"**
2. Nome: `.github/workflows/build-apk.yml`
3. Cole o conteúdo do arquivo: `C:\Users\Murilo Brenner\Desktop\bittuner-github\.github\workflows\build-apk.yml`
4. Commit: "Add GitHub Actions workflow"

### 3.4 Criar README.md

1. Clique em **"Add file"** → **"Create new file"**
2. Nome: `README.md`
3. Conteúdo:

```markdown
# BitTuner - YouTube/Instagram Downloader (Android APK)

Downloader de vídeos e áudios com tema retro gaming para Android.

## APK Automático

Este repositório usa GitHub Actions para fazer o build automático do APK.

## Como Baixar o APK

1. Acesse a aba **Actions** neste repositório
2. Clique no workflow mais recente
3. Role até **Artifacts**
4. Baixe o arquivo `bittuner-apk`
5. Extraia e instale no Android

## Recursos

- Download de Vídeos: MP4, MKV, WEBM, AVI, MOV
- Download de Áudios: MP3, AAC, M4A, FLAC, WAV, OGG, OPUS
- Suporte a YouTube, Instagram, TikTok e mais
- Tema 8-bit retro gaming

## Licença

MIT
```

4. Commit: "Add README"

### 3.5 Criar .gitignore

1. Clique em **"Add file"** → **"Create new file"**
2. Nome: `.gitignore`
3. Conteúdo:

```
__pycache__/
*.pyc
*.pyo
*.pyd
.Python
env/
venv/
.venv
*.log
Downloads/
bin/
*.apk
*.aab
buildozer/
```

4. Commit: "Add gitignore"

## Passo 4: Disparar o Build

Após fazer o push de todos os arquivos, o build vai começar automaticamente.

### 4.1 Verificar o Build

1. No repositório, clique na aba **Actions**
2. Você verá o workflow "Build Android APK" rodando
3. O build leva de 10-20 minutos (primeira vez é mais lento)

### 4.2 Baixar o APK

1. Quando o build terminar, clique no workflow
2. Role até a seção **Artifacts**
3. Clique em `bittuner-apk`
4. O arquivo `.apk` será baixado

## Passo 5: Instalar no Android

1. Transfira o APK para o celular
2. Ative "Instalação de apps desconhecidos"
3. Instale o APK

## Atualizações Automáticas

Toda vez que você fizer push no GitHub, um novo APK será gerado automaticamente.

## Disparar Build Manualmente

Se quiser fazer um novo build sem mudar código:

1. Vá em **Actions**
2. Clique em "Build Android APK"
3. Clique em **"Run workflow"**
4. Clique em **"Run workflow"** novamente

## Solução de Problemas

### Build falhou

1. Clique no workflow com erro
2. Veja os logs para identificar o problema
3. Corrija o código e faça um novo push

### APK não aparece

1. Verifique se o build completou com sucesso
2. Aguarde alguns minutos após o build completar
3. Verifique a seção Artifacts

### Build muito lento

O primeiro build demora mais (15-20 minutos) porque precisa baixar dependências. Builds subsequentes são mais rápidos (5-10 minutos).

## Vantagens

- ✅ Sem WSL necessário
- ✅ Build automático
- ✅ Histórico de versões
- ✅ Gratuito para repositórios públicos
- ✅ Download fácil via GitHub

## URL Final

Seu APK estará disponível em:
`https://github.com/SEU-USUARIO/bittuner/actions`
