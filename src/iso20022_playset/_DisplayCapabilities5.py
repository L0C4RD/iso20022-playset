from . import base_types
from ._UserInterface5Code import UserInterface5Code
from ._LanguageCode import LanguageCode
from ._Number import Number
from ._OutputFormat1Code import OutputFormat1Code

class DisplayCapabilities5(base_types._BaseFieldType):

	__slots__ = ["_AvlblFrmt", "_LineWidth", "_NbOfLines", "_Dstn", "_AvlblLang"]
	@property
	def AvlblFrmt(self):
		return self._AvlblFrmt

	@AvlblFrmt.setter
	def AvlblFrmt(self, value):
		self._AvlblFrmt = value if type(value) != base_types.auto else self.make_default("AvlblFrmt")

	@AvlblFrmt.deleter
	def AvlblFrmt(self):
		del self._AvlblFrmt
		self._AvlblFrmt = None

	@property
	def AvlblLang(self):
		return self._AvlblLang

	@AvlblLang.setter
	def AvlblLang(self, value):
		self._AvlblLang = value if type(value) != base_types.auto else self.make_default("AvlblLang")

	@AvlblLang.deleter
	def AvlblLang(self):
		del self._AvlblLang
		self._AvlblLang = None

	@property
	def Dstn(self):
		return self._Dstn

	@Dstn.setter
	def Dstn(self, value):
		self._Dstn = value if type(value) != base_types.auto else self.make_default("Dstn")

	@Dstn.deleter
	def Dstn(self):
		del self._Dstn
		self._Dstn = None

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
		base_types.FieldEntry(name='AvlblFrmt', type=OutputFormat1Code, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='AvlblLang', type=LanguageCode, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Dstn', type=UserInterface5Code, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='LineWidth', type=Number, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NbOfLines', type=Number, min=0, max=1, mutex_group=None, array=False),
	))

