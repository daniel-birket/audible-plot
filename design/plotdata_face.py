"""Temporary module to document the PlotData class"""
import numpy as np
import math

class PlotData(object):
    """Class to hold data to be plotted and associated descriptors."""

    def __init__(self, p: np.ndarray) -> None:
        """Initialize the plot data from the array. Default the rest."""
        self._points: np.ndarray = p
        self.autoxrange()
        self.autoyrange()
        self._xlabel: str = "x"
        self._ylabel: str = "y"
        self._xdescr: str  = ""
        self._ydescr: str  = ""
        self._title: str = ""
        self._description: str = ""
        self._line_labels: list[str] = []
        self._line_descrs: list[str] = []
        pass

    @property
    def points(self) -> np.ndarray:
        """Numpy n-dimension array of points. X-values first."""
        return self._points

    @points.setter
    def points(self, p: np.ndarray) -> None:
        self._points = p
        pass

    @points.deleter
    def points(self) -> None:
        self._points = np.ndarray([[0, 0], [1, 1]])
        pass


    @property
    def xrange(self) -> tuple[float, float]:
        """Min and Max of the x-values."""
        return self._xrange

    @xrange.setter
    def xrange(self, xr: tuple[float, float]) -> None:
        """Set the min and max of the x-values. If min = max, then
        perform autoxrange. If min > max, then swap them."""
        self._xrange = xr
        pass

    @xrange.deleter
    def xrange(self) -> None:
        self.xrange = (0, 0)
        pass


    @property
    def yrange(self) -> tuple[float, float]:
        """Min and Max of the y-values, for all functions."""
        return self._yrange

    @yrange.setter
    def yrange(self, yr: tuple[float, float]) -> None:
        """Set the min and max of the y-values. If min = max, then
        perform autoyrange. If min > max, then swap them."""
        self._yrange = yr
        pass

    @yrange.deleter
    def yrange(self) -> None:
        self.yrange = (0, 0)
        pass


    @property
    def xlabel(self) -> str:
        """Short label of x-axis"""
        return self._xlabel

    @xlabel.setter
    def xlabel(self, xl: str):
        self._xlabel = xl
        pass

    @xlabel.deleter
    def xlabel(self) -> None:
        self._xlabel = ""
        pass


    @property
    def ylabel(self) -> str:
        """Short label of y-axis"""
        return self._ylabel

    @ylabel.setter
    def ylabel(self, yl: str):
        self._ylabel = yl
        pass

    @ylabel.deleter
    def ylabel(self) -> None:
        self._ylabel = ""
        pass


    @property
    def xdescr(self) -> str:
        """Verbose description of x-data."""
        return self._xdescr

    @xdescr.setter
    def xdescr(self, xd: str):
        self._xdescr = xd
        pass

    @xdescr.deleter
    def xdescr(self) -> None:
        self._xdescr = ""
        pass


    @property
    def ydescr(self) -> str:
        """Verbose description of y-data."""
        return self._ydescr

    @ydescr.setter
    def ydescr(self, yd: str):
        self._ydescr = yd
        pass

    @ydescr.deleter
    def ydescr(self) -> None:
        self._ydescr = ""
        pass


    @property
    def line_labels(self) -> list[str]:
        """List of labels for lines."""
        return self._line_labels

    @line_labels.setter
    def line_labels(self, ll: list[str]) -> None:
        self._line_labels = ll
        pass

    @line_labels.deleter
    def line_labels(self) -> None:
        self._line_labels = ["" for _ in range(self.ysize)]
        pass


    @property
    def line_descrs(self) -> list[str]:
        """List of labels for lines."""
        return self._line_descrs

    @line_descrs.setter
    def line_descrs(self, ld: list[str]) -> None:
        self._line_descrs = ld
        pass

    @line_descrs.deleter
    def line_descrs(self) -> None:
        self._line_descrs = ["" for _ in range(self.ysize)]
        pass


    @property
    def title(self) -> str:
        """Title of plot."""
        if self._title:
            return self._title
        else:
            return self.ylabel + " versus " + self.xlabel

    @title.setter
    def title(self, t: str) -> None:
        self._title = t
        pass

    @title.deleter
    def title(self) -> None:
        self._title = ""
        pass


    @property
    def description(self) -> str:
        """Verbose description of plot."""
        return self._description

    @description.setter
    def description(self, d: str) -> None:
        self._description = d
        pass

    @description.deleter
    def description(self) -> None:
        self._description = ""
        pass


    @property
    def line_labels(self) -> list[str]:
        """List of strings of line labels for legend."""
        if _line_labels:
            return _line_labels
        else:
            ys = self.ysize()
            if ys > 1:
                _line_labels = ["Line "+str(i) for i in range(1, ys+1)]
            else:
                _line_labels = self.ylabel

    @line_labels.setter
    def line_labels(self, ll: list[str]) -> None:
        self._line_labels = ll
        pass

    @line_labels.deleter
    def line_labels(self) -> None:
        _line_labels = []
        pass

    @property
    def line_descrs(self) -> list[str]:
        """List of strings of line descriptions."""
        return _line_descrs

    @line_descrs.setter
    def line_descrs(self, ld: list[str]) -> None:
        self._line_descrs = ld
        pass

    @line_descrs.deleter
    def line_descrs(self) -> None:
        _line_descrs = []
        pass


    @staticmethod
    def round_range(r: tuple[float, float]) -> float:
        """Round the min and max down and up to the next round interval"""
        ad = abs(r[1] - r[0])   # absolute distance from min to max
        dp = int(math.log10(ad))     # position of decimal point
        fac = 10^dp                  # factor of decimal point
        lo = math.floor(r[0] / fac) * fac
        hi = math.ceil(r[1] / fac) * fac
        return (lo, hi)        
                
    def autoxrange(self) -> None:
        """Set the min and max of the x values, rounded down and up
        the order (log10) of the difference between the data min and max."""
        self._xrange = (0.0, 1.0)
        pass

    def autoyrange(self) -> None:
        """Set the min and max of the y values, rounded down and up
        the order (log10) of the difference between the data min and max."""
        self._yrange = (0.0, 1.0)
        pass

    def xsize(self) -> int:
        """Get n, the x dimension size of the point array."""
        return 0

    def ysize(self) -> int:
        """Get m, the number of y functions in the point array."""
        return 0
