# SPDX-License-Identifier: Apache-2.0
# Copyright Contributors to the OpenTimelineIO project

from configparser import ConfigParser
from pathlib import Path

_theme = ConfigParser(interpolation=None)
with Path(__file__).with_name('dvr.ini').open(encoding='utf-8') as theme_file:
    _theme.read_file(theme_file)
COLORS = {name: tuple(map(int, value.split(','))) for name, value in _theme['colors'].items()}

VIEW_STYLESHEET = """
QMainWindow {
    background-color: rgba(%(window.background)s);
}

QScrollBar:horizontal {
    background: rgb(21, 21, 21);
    height: 15px;
    margin: 0px 20px 0 20px;
}

QScrollBar::handle:horizontal {
    background: rgba(%(scrollbar.handle.horizontal)s);
    min-width: 20px;
}

QScrollBar::add-line:horizontal {
    background: rgb(33, 33, 33);
    width: 20px;
    subcontrol-position: right;
    subcontrol-origin: margin;
}

QScrollBar::sub-line:horizontal {
    background: rgb(33, 33, 33);
    width: 20px;
    subcontrol-position: left;
    subcontrol-origin: margin;
}

QScrollBar:left-arrow:horizontal, QScrollBar::right-arrow:horizontal {
    width: 3px;
    height: 3px;
    background: transparent;
}

QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal {
    background: none;
}

QScrollBar:vertical {
    background: rgb(21, 21, 21);
    width: 15px;
    margin: 22px 0 22px 0;
}

QScrollBar::handle:vertical {
    background: rgb(255, 83, 112);
    min-height: 20px;
}

QScrollBar::add-line:vertical {
    background: rgb(33, 33, 33);
    height: 20px;
    subcontrol-position: bottom;
    subcontrol-origin: margin;
}

QScrollBar::sub-line:vertical {
    background: rgb(33, 33, 33);
    height: 20px;
    subcontrol-position: top;
    subcontrol-origin: margin;
}

QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {
    width: 3px;
    height: 3px;
    background: transparent;
}

QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {
    background: none;
}
""" % _theme['colors']
