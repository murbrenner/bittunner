# BitTuner - YouTube/Instagram Downloader (Android APK)

Downloader de vídeos e áudios com tema retro gaming para Android.

## Recursos

- **Download de Vídeos**: MP4, MKV, WEBM, AVI, MOV (vídeo + áudio mesclados)
- **Download de Áudios**: MP3, AAC, M4A, FLAC, WAV, OGG, OPUS
- **Transcrição**: Transcrição automática usando Whisper (TXT)
- **Playlists**: Suporte completo para playlists
- **Plataformas**: YouTube, Instagram, TikTok, Twitter e mais
- **Tema Retro**: Interface com estilo 8-bit retro gaming

## Versão Android

Este é o projeto para gerar o APK Android usando Kivy + Buildozer.

## Como Gerar o APK

### Pré-requisitos

- Python 3.8+
- JDK 11+
- Kivy e Buildozer instalados

### Instalação

```bash
pip install -r requirements.txt
```

### Build do APK

```bash
buildozer android debug
```

Para release:
```bash
buildozer android release
```

## Uso

1. Cole as URLs (uma por linha)
2. Selecione o formato (MP3, MP4, etc.)
3. Para áudio, selecione a qualidade (128-320 kbps)
4. Clique em "BAIXAR AGORA"

## Formatos Suportados

### Áudio
- MP3, AAC, M4A (com seleção de bitrate)
- FLAC, WAV, OGG, OPUS

### Vídeo
- MP4, MKV, WEBM, AVI, MOV

### Transcrição
- TXT (usando Whisper)

## Licença

MIT License
