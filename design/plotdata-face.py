"""Temporary module to document the PlotData class"""
import numpy as np


class PlotData(object):
    """Class to hold data to be plotted and associated descriptors."""

    @property
    def points(self) -> np.ndarray:
        """Numpy n-dimension array of points. X-values first."""
        return self._points

    @points.setter
    def points(self, p: np.ndarray) -> None:
        self._points = p

    @points.deleter
    def points(self) -> None:
        self._points = np.ndarray([[0, 0], [1, 1]])

    @property
    def xrange(self) -> tuple[float, float]:
        """Min and Max of the x-values."""
        return self._xrange

    @xrange.setter
    def xrange(self, xr: tuple[float, float]):
        """Set the min and max of the x-values. If min = max, then
        perform autoxrange. If min > max, then swap them."""
        self._xrange = xr

    @xrange.deleter
    def xrange(self) -> None:
        self.xrange = (0, 0)

    @property
    def yrange(self) -> tuple[float, float]:
        """Min and Max of the y-values, for all functions."""
        return self._yrange

    @yrange.setter
    def yrange(self, yr: tuple[float, float]):
        """Set the min and max of the y-values. If min = max, then
        perform autoyrange. If min > max, then swap them."""
        self._yrange = yr

    @yrange.deleter
    def yrange(self) -> None:
        self.yrange = (0, 0)

    @property
    def xlabel(self) -> str:
        """Short label of x-axis"""
        return self._xlabel

    @xlabel.setter
    def xlabel(self, xl: str):
        self._xlabel = xl

    @xlabel.deleter
    def xlabel(self) -> None:
        self._xlabel = ""

    @property
    def ylabel(self) -> str:
        """Short label of y-axis"""
        return self._ylabel

    @ylabel.setter
    def ylabel(self, yl: str):
        self._ylabel = yl

    @ylabel.deleter
    def ylabel(self) -> None:
        self._ylabel = ""

    @property
    def xdescr(self) -> str:
        """Verbose description of x-data."""
        return self._xdescr

    @xdescr.setter
    def xdescr(self, xd: str):
        self._xdescr = xd

    @xdescr.deleter
    def xdescr(self) -> None:
        self._xdescr = ""

    @property
    def ydescr(self) -> str:
        """Verbose description of y-data."""
        return self._ydescr

    @ydescr.setter
    def ydescr(self, yd: str):
        self._ydescr = yd

    @ydescr.deleter
    def ydescr(self) -> None:
        self._ydescr = ""

    @property
    def line_labels(self) -> list[str]:
        """List of labels for lines."""
        return self._line_labels

    @line_labels.setter
    def line_labels(self, ll: list[str]) -> None:
        _line_labels = ll

    @line_labels.deleter
    def line_labels(self) -> None:
        _line_labels = ["" for _ in range(self.ysize)]

    @property
    def line_descrs(self) -> list[str]:
        """List of labels for lines."""
        return self._line_descrs

    @line_descrs.setter
    def line_descrs(self, ld: list[str]) -> None:
        _line_descrs = ld

    @line_descrs.deleter
    def line_descrs(self) -> None:
        _line_descrs = ["" for _ in range(self.ysize)]
        
    @property
    def title(self) -> str:
        return self._title

    @title.setter
    def title(self, t: str) -> None:
        _title = t

    @title.deleter
    def title(self) -> None:
        _title = ""

    @property
    def description(self) -> str:
        return self._description

    @description.setter
    def description(self, d: str) -> None:
        _description = d

    @description.deleter
    def description(self) -> None:
        _description = ""

    def autoxrange(self) -> None:
        """Set the min and max of the x values, rounded down and up
        one tenth of the difference between the simple min and max."""
        self._xrange = (0.0, 1.0)

    def autoyrange(self) -> None:
        """Set the min and max of the y values, rounded down and up
        one tenth of the difference between the simple min and max."""
        self._yrange = (0.0, 1.0)

    def xsize(self) -> int:
        """Get n, the x dimension size of the point array."""
        return 0

    def ysize(self) -> int:
        """Get m, the number of y functions in the point array."""
        return 0

    def __init__(self, p: np.ndarray) -> None:
        self.points = p
        self.autoxrange()
        self.autoyrange()
        self.xlabel = "x"
        self.ylabel = "y"
        self.xdescr = "x-data"
        self.ydescr = "y-data"
        self.title = "X-Y Plot"
        self.description = ""
