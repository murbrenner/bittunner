[app]
# (str) Title of your application
title = BitTuner

# (str) Package name
package.name = bittuner

# (str) Package domain (needed for android/ios packaging)
package.domain = org.bittuner

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas,txt

# (str) Application versioning (method 1)
version = 1.0.0

# (list) Application requirements
requirements = python3,kivy,yt-dlp,certifi,pyjnius,android

# (str) Presplash of the application
#presplash.filename = %(source.dir)s/assets/presplash.png

# (str) Icon of the application
#icon.filename = %(source.dir)s/assets/icon.png

# (list) Android permissions
android.permissions = INTERNET,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE

# (int) Target Android API, should be as high as possible.
android.api = 33

# (int) Minimum Android API
android.minapi = 21

# (int) Android NDK version to use
android.ndk = 25b

# (int) Android SDK version to use
android.sdk = 33

# (str) Android NDK directory (if empty, it will be automatically downloaded.)
#android.ndk_path =

# (str) Android SDK directory (if empty, it will be automatically downloaded.)
#android.sdk_path =

# (str) Android entry point, default is ok for Kivy-based app
android.entrypoint = org.kivy.android.PythonActivity

# (list) Pattern to whitelist for the whole project
#android.whitelist =

# (str) Path to a custom whitelist file
#android.whitelist_src =

# (str) Path to a custom blacklist file
#android.blacklist_src =

# (list) Android archs to build for (arm64-v8a, armeabi-v7a)
android.archs = arm64-v8a,armeabi-v7a

# (bool) Indicate if the application should be fullscreen or not
android.fullscreen = False

# (list) Android additional libraries
android.add_libs = 

# (bool) Copy application's assets to the app
android.copy_libs = 1

# (str) The Android arch to build for
android.arch = arm64-v8a

# (str) OUYA Category. Must be one of GAME or APP
# If you leave this blank, OUYA support will be disabled.
#ouya.category = GAME

# (str) Filename of OUYA icon. It must be a 732x412 png image.
#ouya.icon.filename = %(source.dir)s/assets/ouya_icon.png

# (str) Filename of OUYA banner. It must be a 1920x500 png image.
#ouya.banner.filename = %(source.dir)s/assets/ouya_banner.png

# (str) Presplash background color (for android toolchain)
#android.presplash_color = #FFFFFF

# (str) Android logcat filter to use
#android.logcat_filters = *:S python:D

# (bool) Copy library instead of making a libpymodules.so
#android.copy_libs = 1

# (list) The Android archs to build for, separated by commas
#android.archs = arm64-v8a,armeabi-v7a,x86

# (int) android.minapi:
#android.minapi = 21

# (int) android.sdk:
#android.sdk = 33

# (str) android.ndk:
#android.ndk = 25b

# (int) android.minapi:
android.minapi = 21

# (int) android.sdk:
android.sdk = 33

# (str) android.ndk:
android.ndk = 25b

# (int) Android NDK version to use
android.ndk = 25b

# (int) Android SDK version to use
android.sdk = 33

# (str) Android entry point, default is ok for Kivy-based app
android.entrypoint = org.kivy.android.PythonActivity

# (list) Android additional libraries
android.add_libs = 

# (bool) Copy application's assets to the app
android.copy_libs = 1

# (str) The Android arch to build for
android.arch = arm64-v8a

# (str) Presplash background color (for android toolchain)
#android.presplash_color = #FFFFFF

# (str) Android logcat filter to use
#android.logcat_filters = *:S python:D

# (bool) Copy library instead of making a libpymodules.so
#android.copy_libs = 1

# (list) The Android archs to build for, separated by commas
#android.archs = arm64-v8a,armeabi-v7a,x86

[buildozer]
# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = False, 1 = True)
warn_on_root = 1
