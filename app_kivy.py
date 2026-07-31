import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.spinner import Spinner
from kivy.uix.scrollview import ScrollView
from kivy.uix.popup import Popup
from kivy.uix.progressbar import ProgressBar
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.config import Config
import yt_dlp
import os
import threading
import platform

# Configurações
Config.set('graphics', 'resizable', '1')
Window.size = (400, 700)

kivy.require('2.0.0')

# Formatos
AUDIO_FORMATS = ["MP3", "AAC", "M4A", "FLAC", "WAV", "OGG", "OPUS"]
VIDEO_FORMATS = ["MP4", "MKV", "WEBM", "AVI", "MOV"]
TRANSCRIPT_FORMATS = ["TXT"]
FORMATS_WITH_BITRATE = {"MP3", "AAC", "M4A"}
WHISPER_MODELS = ["tiny", "base", "small", "medium", "large"]

# Caminho do FFmpeg
if platform.system() == "Android":
    try:
        from jnius import autoclass
        PythonActivity = autoclass('org.kivy.android.PythonActivity')
        FFMPEG_PATH = os.path.join(PythonActivity.mActivity.getFilesDir().toString(), "ffmpeg")
    except:
        FFMPEG_PATH = "ffmpeg"
else:
    FFMPEG_PATH = r"C:\Users\Murilo Brenner\AppData\Local\Microsoft\WinGet\Packages\Gyan.FFmpeg_Microsoft.Winget.Source_8wekyb3d8bbwe\ffmpeg-8.1.2-full_build\bin\ffmpeg.exe"

class BitTunerApp(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = 10
        self.spacing = 10
        
        # Cores tema retro
        self.bg_color = [0.1, 0.11, 0.17, 1]  # Azul escuro
        self.surface_color = [0.12, 0.12, 0.18, 1]
        self.panel_color = [0.18, 0.17, 0.26, 1]
        self.text_color = [1, 0.93, 0.82, 1]
        self.accent_color = [1, 0, 0.27, 1]
        self.button_bg = [1, 0, 0.27, 1]
        self.button_text = [1, 1, 1, 1]
        
        self.build_ui()
    
    def build_ui(self):
        # Header
        header = BoxLayout(orientation='vertical', size_hint_y=None, height=80)
        header.add_widget(Label(
            text='BITTUNER',
            font_size=32,
            bold=True,
            color=self.text_color,
            size_hint_y=None,
            height=40
        ))
        header.add_widget(Label(
            text='RETRO GAMING DOWNLOADER',
            font_size=12,
            color=[0.55, 0.61, 0.71, 1],
            size_hint_y=None,
            height=30
        ))
        self.add_widget(header)
        
        # URLs
        self.add_widget(Label(
            text='URLs (uma por linha)',
            font_size=16,
            bold=True,
            color=self.text_color,
            size_hint_y=None,
            height=30
        ))
        self.urls = TextInput(
            multiline=True,
            size_hint_y=None,
            height=100,
            background_color=self.panel_color,
            foreground_color=self.text_color,
            hint_text='Cole as URLs aqui...'
        )
        self.add_widget(self.urls)
        
        # Destino
        self.add_widget(Label(
            text='PASTA DE DESTINO',
            font_size=16,
            bold=True,
            color=self.text_color,
            size_hint_y=None,
            height=30
        ))
        dest_row = BoxLayout(orientation='horizontal', size_hint_y=None, height=50)
        self.output_dir = TextInput(
            text=os.path.join(os.path.expanduser("~"), "Downloads", "YouTube Downloads"),
            background_color=self.panel_color,
            foreground_color=self.text_color
        )
        btn_browse = Button(
            text='BROWSE',
            background_color=self.panel_color,
            color=self.accent_color,
            size_hint_x=0.3
        )
        btn_browse.bind(on_press=self.browse_folder)
        dest_row.add_widget(self.output_dir)
        dest_row.add_widget(btn_browse)
        self.add_widget(dest_row)
        
        # Formato
        self.add_widget(Label(
            text='FORMATO',
            font_size=16,
            bold=True,
            color=self.text_color,
            size_hint_y=None,
            height=30
        ))
        fmt_row = BoxLayout(orientation='horizontal', size_hint_y=None, height=50)
        self.fmt = Spinner(
            text='MP3',
            values=AUDIO_FORMATS + VIDEO_FORMATS + TRANSCRIPT_FORMATS,
            background_color=self.panel_color,
            color=self.text_color
        )
        self.fmt.bind(text=self.on_fmt_change)
        self.quality = Spinner(
            text='192',
            values=['128', '192', '256', '320'],
            background_color=self.panel_color,
            color=self.text_color
        )
        fmt_row.add_widget(self.fmt)
        fmt_row.add_widget(self.quality)
        self.add_widget(fmt_row)
        
        # Modelo Whisper (inicialmente oculto)
        self.model_label = Label(
            text='MODELO WHISPER',
            font_size=16,
            bold=True,
            color=self.text_color,
            size_hint_y=None,
            height=30,
            opacity=0
        )
        self.add_widget(self.model_label)
        self.model = Spinner(
            text='small',
            values=WHISPER_MODELS,
            background_color=self.panel_color,
            color=self.text_color,
            size_hint_y=None,
            height=50,
            opacity=0
        )
        self.add_widget(self.model)
        
        # Botão Download
        self.btn_download = Button(
            text='BAIXAR AGORA',
            font_size=20,
            bold=True,
            background_color=self.button_bg,
            color=self.button_text,
            size_hint_y=None,
            height=60
        )
        self.btn_download.bind(on_press=self.start_download)
        self.add_widget(self.btn_download)
        
        # Progress
        self.progress = ProgressBar(
            size_hint_y=None,
            height=20,
            opacity=0
        )
        self.add_widget(self.progress)
        
        # Log
        self.add_widget(Label(
            text='LOG',
            font_size=16,
            bold=True,
            color=self.text_color,
            size_hint_y=None,
            height=30
        ))
        self.log = TextInput(
            multiline=True,
            size_hint_y=None,
            height=150,
            background_color=self.panel_color,
            foreground_color=self.text_color,
            readonly=True
        )
        self.add_widget(self.log)
        
        # Status
        self.status = Label(
            text='>> PRONTO PARA RECEBER URLs',
            font_size=12,
            color=[0.55, 0.61, 0.71, 1],
            size_hint_y=None,
            height=30
        )
        self.add_widget(self.status)
    
    def browse_folder(self, instance):
        # Em Android, usar filechooser nativo
        if platform.system() == "Android":
            try:
                from android.storage import primary_external_storage_path
                from jnius import autoclass
                PythonActivity = autoclass('org.kivy.android.PythonActivity')
                Intent = autoclass('android.content.Intent')
                DocumentsContract = autoclass('android.provider.DocumentsContract')
                
                intent = Intent(Intent.ACTION_OPEN_DOCUMENT_TREE)
                PythonActivity.mActivity.startActivityForResult(intent, 42)
            except:
                self.log.text += "Erro: Seletor de pasta não disponível\n"
        else:
            # Desktop - usar popup simples
            content = BoxLayout(orientation='vertical')
            content.add_widget(Label(text='Digite o caminho da pasta:'))
            path_input = TextInput(text=self.output_dir.text)
            content.add_widget(path_input)
            
            def set_path(instance):
                if path_input.text:
                    self.output_dir.text = path_input.text
                popup.dismiss()
            
            btn_ok = Button(text='OK', size_hint_y=None, height=50)
            btn_ok.bind(on_press=set_path)
            content.add_widget(btn_ok)
            
            popup = Popup(title='Selecionar Pasta', content=content, size_hint=(0.8, 0.4))
            popup.open()
    
    def on_fmt_change(self, spinner, text):
        if text in TRANSCRIPT_FORMATS:
            self.quality.opacity = 0
            self.quality.size_hint_y = None
            self.quality.height = 0
            self.model_label.opacity = 1
            self.model.opacity = 1
            self.model.height = 50
        elif text in AUDIO_FORMATS:
            if text in FORMATS_WITH_BITRATE:
                self.quality.opacity = 1
                self.quality.height = 50
            else:
                self.quality.opacity = 0
                self.quality.height = 0
            self.model_label.opacity = 0
            self.model.opacity = 0
            self.model.height = 0
        else:
            self.quality.opacity = 0
            self.quality.height = 0
            self.model_label.opacity = 0
            self.model.opacity = 0
            self.model.height = 0
    
    def start_download(self, instance):
        self.btn_download.disabled = True
        self.progress.opacity = 1
        self.log.text = ''
        self.status.text = '>> BAIXANDO...'
        
        thread = threading.Thread(target=self.download_worker)
        thread.daemon = True
        thread.start()
    
    def download_worker(self):
        urls = [u.strip() for u in self.urls.text.splitlines() if u.strip()]
        output_dir = self.output_dir.text
        fmt = self.fmt.text
        quality = self.quality.text
        
        for url in urls:
            self.download_single(url, output_dir, fmt, quality)
        
        Clock.schedule_once(lambda dt: self.finish_download(), 0)
    
    def download_single(self, url, output_dir, fmt, quality):
        is_audio = fmt in AUDIO_FORMATS
        fmt_lower = fmt.lower()
        
        def progress_hook(d):
            if d["status"] == "downloading":
                percent = d.get("_percent_str", "?%")
                Clock.schedule_once(lambda dt: self.update_log(f"[{percent}] Baixando...\n"), 0)
        
        if is_audio:
            opts = {
                "format": "bestaudio/best",
                "outtmpl": os.path.join(output_dir, "%(title)s.%(ext)s"),
                "postprocessors": [{
                    "key": "FFmpegExtractAudio",
                    "preferredcodec": fmt_lower,
                    "preferredquality": quality if fmt in FORMATS_WITH_BITRATE else "0",
                }],
                "ffmpeg_location": FFMPEG_PATH,
                "quiet": True,
            }
        else:
            opts = {
                "format": "bestvideo+bestaudio/best",
                "outtmpl": os.path.join(output_dir, "%(title)s.%(ext)s"),
                "merge_output_format": fmt_lower,
                "ffmpeg_location": FFMPEG_PATH,
                "keepvideo": False,
                "quiet": True,
            }
        
        try:
            with yt_dlp.YoutubeDL(opts) as ydl:
                ydl.download([url])
            Clock.schedule_once(lambda dt: self.update_log(f"✔ {url} concluído!\n"), 0)
        except Exception as e:
            Clock.schedule_once(lambda dt: self.update_log(f"✗ Erro: {e}\n"), 0)
    
    def update_log(self, text):
        self.log.text += text
    
    def finish_download(self):
        self.btn_download.disabled = False
        self.progress.opacity = 0
        self.status.text = '>> PRONTO'
        self.log.text += '✔ Download concluído!\n'

class BitTunerAppMain(App):
    def build(self):
        self.title = 'BitTuner'
        return BitTunerApp()

if __name__ == '__main__':
    BitTunerAppMain().run()
