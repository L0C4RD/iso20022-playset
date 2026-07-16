# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import LanguageCode
from . import Number
from . import OutputFormat1Code
from . import UserInterface9Code

class DisplayCapabilities7(base_types._BaseFieldType):

	__slots__ = ["_AvlblFrmt", "_AvlblLang", "_Dstn", "_LineWidth", "_NbOfLines"]
	@property
	def AvlblFrmt(self):
		return self._AvlblFrmt

	@AvlblFrmt.setter
	def AvlblFrmt(self, value):
		self._AvlblFrmt = value if value is not None else base_types.UninitialisedField(self, 'AvlblFrmt', OutputFormat1Code, True)

	@AvlblFrmt.deleter
	def AvlblFrmt(self):
		del self._AvlblFrmt
		self._AvlblFrmt = base_types.UninitialisedField(self, 'AvlblFrmt', OutputFormat1Code, True)

	@property
	def AvlblLang(self):
		return self._AvlblLang

	@AvlblLang.setter
	def AvlblLang(self, value):
		self._AvlblLang = value if value is not None else base_types.UninitialisedField(self, 'AvlblLang', LanguageCode, True)

	@AvlblLang.deleter
	def AvlblLang(self):
		del self._AvlblLang
		self._AvlblLang = base_types.UninitialisedField(self, 'AvlblLang', LanguageCode, True)

	@property
	def Dstn(self):
		return self._Dstn

	@Dstn.setter
	def Dstn(self, value):
		self._Dstn = value if value is not None else base_types.UninitialisedField(self, 'Dstn', UserInterface9Code, True)

	@Dstn.deleter
	def Dstn(self):
		del self._Dstn
		self._Dstn = base_types.UninitialisedField(self, 'Dstn', UserInterface9Code, True)

	@property
	def LineWidth(self):
		return self._LineWidth

	@LineWidth.setter
	def LineWidth(self, value):
		self._LineWidth = value if value is not None else base_types.UninitialisedField(self, 'LineWidth', Number, False)

	@LineWidth.deleter
	def LineWidth(self):
		del self._LineWidth
		self._LineWidth = base_types.UninitialisedField(self, 'LineWidth', Number, False)

	@property
	def NbOfLines(self):
		return self._NbOfLines

	@NbOfLines.setter
	def NbOfLines(self, value):
		self._NbOfLines = value if value is not None else base_types.UninitialisedField(self, 'NbOfLines', Number, False)

	@NbOfLines.deleter
	def NbOfLines(self):
		del self._NbOfLines
		self._NbOfLines = base_types.UninitialisedField(self, 'NbOfLines', Number, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AvlblFrmt', type=OutputFormat1Code, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='AvlblLang', type=LanguageCode, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Dstn', type=UserInterface9Code, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='LineWidth', type=Number, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NbOfLines', type=Number, min=0, max=1, mutex_group=None, array=False),
	))