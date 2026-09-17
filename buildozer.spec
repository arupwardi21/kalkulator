[app]
title = 55five Tracker
package.name = tracker55
package.domain = com.arup.tracker
source.dir =.
source.include_exts = py
version = 1.0
requirements = python3,kivy==2.3.0
orientation = portrait
fullscreen = 0

[buildozer]
log_level = 2

[app:android]
android.archs = arm64-v8a, armeabi-v7a
android.permissions = INTERNET
