# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Max3NumericText
from . import UserInterface2Code

class DisplayCapabilities1(base_types._BaseFieldType):

	__slots__ = ["_DispTp", "_LineWidth", "_NbOfLines"]
	@property
	def DispTp(self):
		return self._DispTp

	@DispTp.setter
	def DispTp(self, value):
		self._DispTp = value if value is not None else base_types.UninitialisedField(self, 'DispTp', UserInterface2Code, False)

	@DispTp.deleter
	def DispTp(self):
		del self._DispTp
		self._DispTp = base_types.UninitialisedField(self, 'DispTp', UserInterface2Code, False)

	@property
	def LineWidth(self):
		return self._LineWidth

	@LineWidth.setter
	def LineWidth(self, value):
		self._LineWidth = value if value is not None else base_types.UninitialisedField(self, 'LineWidth', Max3NumericText, False)

	@LineWidth.deleter
	def LineWidth(self):
		del self._LineWidth
		self._LineWidth = base_types.UninitialisedField(self, 'LineWidth', Max3NumericText, False)

	@property
	def NbOfLines(self):
		return self._NbOfLines

	@NbOfLines.setter
	def NbOfLines(self, value):
		self._NbOfLines = value if value is not None else base_types.UninitialisedField(self, 'NbOfLines', Max3NumericText, False)

	@NbOfLines.deleter
	def NbOfLines(self):
		del self._NbOfLines
		self._NbOfLines = base_types.UninitialisedField(self, 'NbOfLines', Max3NumericText, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='DispTp', type=UserInterface2Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LineWidth', type=Max3NumericText, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NbOfLines', type=Max3NumericText, min=1, max=1, mutex_group=None, array=False),
	))