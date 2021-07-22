import sys
from PySide2 import QtCore
from PySide2.QtCore import Qt
from PySide2.QtGui import QColor, QPixmap
from PySide2.QtWidgets import *
import threading
import time
import requests
import sqlite3
import re
import numpy
from AnaEkran import Ui_AnaEkran
from GirisKayitEkran import Ui_GirisKayitEkran
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from decimal import Decimal