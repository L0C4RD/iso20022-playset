from . import base_types
from ._Max3NumericText import Max3NumericText
from ._UserInterface2Code import UserInterface2Code

class DisplayCapabilities1(base_types._BaseFieldType):

	__slots__ = ["_DispTp", "_LineWidth", "_NbOfLines"]
	@property
	def DispTp(self):
		return self._DispTp

	@DispTp.setter
	def DispTp(self, value):
		self._DispTp = value if type(value) != base_types.auto else self.make_default("DispTp")

	@DispTp.deleter
	def DispTp(self):
		del self._DispTp
		self._DispTp = None

	@property
	def LineWidth(self):
		return self._LineWidth

	@LineWidth.setter
	def LineWidth(self, value):
		self._LineWidth = value if type(value) != base_types.auto else self.make_default("LineWidth")

	@LineWidth.deleter
	def LineWidth(self):
		del self._LineWidth
		self._LineWidth = None

	@property
	def NbOfLines(self):
		return self._NbOfLines

	@NbOfLines.setter
	def NbOfLines(self, value):
		self._NbOfLines = value if type(value) != base_types.auto else self.make_default("NbOfLines")

	@NbOfLines.deleter
	def NbOfLines(self):
		del self._NbOfLines
		self._NbOfLines = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='DispTp', type=UserInterface2Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LineWidth', type=Max3NumericText, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NbOfLines', type=Max3NumericText, min=1, max=1, mutex_group=None, array=False),
	))

