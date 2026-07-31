# Tutorial: Gerar APK Android para BitTuner

Este tutorial explica como converter o BitTuner em um aplicativo Android usando **Kivy + Buildozer**.

## Por que Kivy + Buildozer?

O app atual usa **Tkinter**, que não roda em Android. **Kivy** é a melhor opção porque:
- Framework maduro e testado para mobile
- Suporte nativo para Android e iOS
- Buildozer automatiza todo o processo de build
- Widgets customizáveis e responsivos
- Comunidade ativa e documentação extensa

## Pré-requisitos

### 1. Instalar Python 3.8+
```bash
python --version
```

### 2. Instalar JDK 11+
```bash
java -version
```

### 3. Instalar dependências do sistema

#### Linux (Ubuntu/Debian)
```bash
sudo apt update
sudo apt install -y build-essential git ffmpeg libsdl2-dev libsdl2-image-dev libsdl2-mixer-dev libsdl2-ttf-dev libportmidi-dev libswscale-dev libavformat-dev libavcodec-dev zlib1g-dev
sudo apt install -y autoconf libtool pkg-config libncurses5-dev libncursesw5-dev libtinfo5 cmake libffi-dev libssl-dev
```

#### Windows
- Instale: https://www.python.org/downloads/
- Instale: https://adoptium.net/ (JDK 11)
- Instale: https://git-scm.com/download/win

### 4. Instalar Kivy e Buildozer
```bash
pip install kivy[base]
pip install buildozer
pip install cython
```

## Passo 1: Usar a versão Kivy do App

Já criei o arquivo `app_kivy.py` que é a versão do BitTuner usando Kivy. Este arquivo contém toda a lógica do app adaptada para Kivy.

### Testar no Desktop
```bash
python app_kivy.py
```

## Passo 2: Configurar o Buildozer

### 2.1 Inicializar o Buildozer
```bash
cd youtube_playlist_downloader
buildozer init
```

Isso cria o arquivo `buildozer.spec` com todas as configurações.

### 2.2 Editar buildozer.spec

Abra o arquivo `buildozer.spec` e ajuste as seguintes seções:

```spec
# Título do app
title = BitTuner

# Nome do pacote
package.name = bittuner

# Domínio (use seu domínio ou exemplo)
package.domain = org.bittuner

# Versão
version = 1.0.0

# Dependências Python
requirements = python3,kivy,yt-dlp,certifi,pyjnius,android

# Permissões Android
android.permissions = INTERNET,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE

# Orientação (landscape/portrait)
orientation = portrait

# Ícone (opcional)
icon.filename = assets/icon.png

# Presplash (tela de loading)
presplash.filename = assets/presplash.png
```

### 2.3 Adicionar FFmpeg ao APK

O FFmpeg precisa ser incluído no APK. Crie a pasta `assets/` e coloque o binário FFmpeg para Android ARM64:

```bash
mkdir assets
# Baixe FFmpeg para Android ARM64 de: https://github.com/BtbN/FFmpeg-Builds/releases
# Coloque o arquivo ffmpeg em assets/ffmpeg
```

No `buildozer.spec`, adicione:
```spec
android.include_assets = assets/ffmpeg
```

## Passo 3: Build do APK

### 3.1 Debug APK (mais rápido)
```bash
buildozer android debug
```

### 3.2 Release APK (otimizado para distribuição)
```bash
buildozer android release
```

### 3.3 Opções úteis
```bash
# Limpar cache e rebuild
buildozer android clean
buildozer android debug

# Ver logs de erro
buildozer android logcat

# Deploy direto no dispositivo conectado via USB
buildozer android deploy run
```

## Passo 4: Instalar no Android

### Via USB
1. Ative "Depuração USB" no celular
2. Conecte via USB
3. Execute:
```bash
buildozer android deploy run
```

### Via APK
1. Transfira o `.apk` da pasta `bin/` para o celular
2. Ative "Instalação de apps desconhecidos"
3. Instale o APK

## Passo 5: Ajustar Caminho do FFmpeg no Código

No `app_kivy.py`, ajuste o caminho do FFmpeg para Android:

```python
import platform

if platform.system() == "Android":
    from jnius import autoclass
    PythonActivity = autoclass('org.kivy.android.PythonActivity')
    FFMPEG_PATH = os.path.join(PythonActivity.mActivity.getFilesDir().toString(), "ffmpeg")
else:
    # Windows/Linux
    FFMPEG_PATH = r"C:\Users\Murilo Brenner\AppData\Local\Microsoft\WinGet\Packages\Gyan.FFmpeg_Microsoft.Winget.Source_8wekyb3d8bbwe\ffmpeg-8.1.2-full_build\bin\ffmpeg.exe"
```

## Solução de Problemas

### Erro: "command 'gcc' failed"
```bash
# Linux: Instale build-essential
sudo apt install build-essential

# Windows: Instale MinGW ou use WSL
```

### Erro: "SDK not found"
Configure no `buildozer.spec`:
```spec
android.sdk_path = /caminho/para/Android/Sdk
android.ndk_path = /caminho/para/Android/Sdk/ndk/25.2.9519653
```

### Erro: "JDK not found"
```bash
export JAVA_HOME=/caminho/para/jdk-11
```

### Build muito lento
- Use `buildozer android debug` durante desenvolvimento
- Cache do Buildozer acelera builds subsequentes

### APK muito grande
- Remova dependências desnecessárias do `buildozer.spec`
- Use `--strip` para remover símbolos de debug

### Erro de permissão no Android
Adicione ao `buildozer.spec`:
```spec
android.permissions = INTERNET,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE
```

## Recursos

- Kivy Docs: https://kivy.org/doc/stable/
- Buildozer Docs: https://buildozer.readthedocs.io/
- Kivy Android: https://github.com/kivy/python-for-android
- FFmpeg Android: https://github.com/BtbN/FFmpeg-Builds/releases

## Dicas Adicionais

### Testar no Emulador
```bash
# Inicie o emulador Android Studio
buildozer android deploy run
```

### Assinar o APK (Release)
Para publicar na Play Store, você precisa assinar o APK:
```spec
# No buildozer.spec
android.release_keystore = /caminho/para/keystore.jks
android.release_keyalias = seu_alias
android.release_keypassword = sua_senha
android.release_keystore_password = sua_senha
```

### Atualizar o App
- Aumente a versão no `buildozer.spec`
- Rebuild com `buildozer android release`
- O novo APK substituirá o anterior
