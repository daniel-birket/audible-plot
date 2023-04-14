"""Temporary Module to document the PlotVisual class."""

import enum
import math
import plotdata_face


class FileType(enum.StrEnum):
    """Enumeration of plot graphic file types."""

    PNG = enum.auto()
    GIF = enum.auto()
    JPEG = enum.auto()
    SVG = enum.auto()


class PlotVisual(object):
    """Class to define and visually plot a PlotData object."""

    def __init__(self, pd: PlotData) -> None:
        """Initialize a visual plot with PlotData."""
        self._filetype = FileType.PNG
        self._output = "plot"
        self._size = (640, 480)
        pass

    @property
    def filetype(self) -> FileType:
        "Type of output file. `png`, `gif`, `jpeg`, or `svg`."
        return self._filetype

    @filetype.setter
    def filetype(self, ft: FileType) -> None:
        self._filetype = ft
        pass

    @property
    def output(self) -> str:
        """Name of output graphic, tsv and gp files."""
        return self._output

    @output.setter
    def output(self, out: str) -> None:
        self._output = out
        pass

    @property
    def size(self) -> tuple[int, int]:
        return self._size

    @size.setter
    def size(self, s: tuple[int, int]):
        self._size = s
        pass

    def out_filename(self) -> str:
        """Get the output graphic filename from `output` and `filetype`."""
        return ""

    def tsv_filename(self) -> str:
        """Get the tab-seperated-values data filename from `output` and `.tsv`."""
        return ""

    def gp_filename(self) -> str:
        """Get the gnuplot commands filename from `output` and `.gp`."""
        return ""

    def write_tsv(self) -> None:
        """Write the `.tsv` data file with headers and data."""
        pass

    def write_gp(self) -> None:
        """Write the `.gp` commands file."""
        pass
