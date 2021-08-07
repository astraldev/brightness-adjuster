
from setuptools import setup
setup(
  name="brightness-adjuster",
  version="1.0.0",
  author="AstralDev",
  author_email="ekureedem480@gmail.com",
  license="GPL",
  keywords="controller adjuster brightness",
  python_requires=">=3",
  requires=["pygobject", "configparser"],
  scripts=["brightness-adjuster"],
  data_files=[("brightness-adjuster/ui", ["ui/style.css", "ui/ui.glade"]),
              (".brightness-adjuster", ["config.cfg"]),
              ("share/applications", ["brightness-adjuster.desktop"]),
              ("share/icons/hicolor/512x512/apps",["icons/512x512/brightness-adjuster.png"]),
              ("share/icons/hicolor/128x128/apps", ["icons/128x128/brightness-adjuster.png"]),
              ("share/icons/hicolor/64x64/apps", ["icons/64x64/brightness-adjuster.png"]),
              ("share/icons/hicolor/256x256/apps", ["icons/256x256/brightness-adjuster.png"]),
              ("share/icons/hicolor/scalable/apps", ["icons/scalable/brightness-adjuster.svg"])]
)