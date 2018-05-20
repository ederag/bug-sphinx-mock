import bar
from bar import pyqtSignal


class FooClass(bar.BarClass):
    """This is myclass"""
    
    signal_try = pyqtSignal(bool)
    
    pass

