[app]
title = SampleApp
package.name = nfsApk
package.domain = org.novfensec
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
source.include_patterns = images/*.png
version = 0.1
requirements = python3, kivy==2.3.0, kivymd==2.3.1, plyer==2.1.0, pillow, exceptiongroup, asynckivy, asyncgui, materialyoucolor, android
presplash.filename = %(source.dir)s/images/presplash.png
icon.filename = %(source.dir)s/images/favicon.png
orientation = portrait
fullscreen = 0

[android]
android.api = 35
android.minapi = 21
android.ndk = 25b
android.archs = arm64-v8a
android.permissions = INTERNET, WRITE_EXTERNAL_STORAGE; maxSdkVersion=18
android.accept_sdk_license = True
android.release_artifact = aab
android.debug_artifact = apk

[buildozer]
log_level = 2
warn_on_root = 1
