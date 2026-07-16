# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AmountAndDirection102

class StressLiquidResourceRequirement1(base_types._BaseFieldType):

	__slots__ = ["_OprlOutflw", "_Othr", "_SttlmOrDlvry", "_VartnMrgnPmtOblgtn"]
	@property
	def OprlOutflw(self):
		return self._OprlOutflw

	@OprlOutflw.setter
	def OprlOutflw(self, value):
		self._OprlOutflw = value if value is not None else base_types.UninitialisedField(self, 'OprlOutflw', AmountAndDirection102, False)

	@OprlOutflw.deleter
	def OprlOutflw(self):
		del self._OprlOutflw
		self._OprlOutflw = base_types.UninitialisedField(self, 'OprlOutflw', AmountAndDirection102, False)

	@property
	def Othr(self):
		return self._Othr

	@Othr.setter
	def Othr(self, value):
		self._Othr = value if value is not None else base_types.UninitialisedField(self, 'Othr', AmountAndDirection102, False)

	@Othr.deleter
	def Othr(self):
		del self._Othr
		self._Othr = base_types.UninitialisedField(self, 'Othr', AmountAndDirection102, False)

	@property
	def SttlmOrDlvry(self):
		return self._SttlmOrDlvry

	@SttlmOrDlvry.setter
	def SttlmOrDlvry(self, value):
		self._SttlmOrDlvry = value if value is not None else base_types.UninitialisedField(self, 'SttlmOrDlvry', AmountAndDirection102, False)

	@SttlmOrDlvry.deleter
	def SttlmOrDlvry(self):
		del self._SttlmOrDlvry
		self._SttlmOrDlvry = base_types.UninitialisedField(self, 'SttlmOrDlvry', AmountAndDirection102, False)

	@property
	def VartnMrgnPmtOblgtn(self):
		return self._VartnMrgnPmtOblgtn

	@VartnMrgnPmtOblgtn.setter
	def VartnMrgnPmtOblgtn(self, value):
		self._VartnMrgnPmtOblgtn = value if value is not None else base_types.UninitialisedField(self, 'VartnMrgnPmtOblgtn', AmountAndDirection102, False)

	@VartnMrgnPmtOblgtn.deleter
	def VartnMrgnPmtOblgtn(self):
		del self._VartnMrgnPmtOblgtn
		self._VartnMrgnPmtOblgtn = base_types.UninitialisedField(self, 'VartnMrgnPmtOblgtn', AmountAndDirection102, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='OprlOutflw', type=AmountAndDirection102, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Othr', type=AmountAndDirection102, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SttlmOrDlvry', type=AmountAndDirection102, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='VartnMrgnPmtOblgtn', type=AmountAndDirection102, min=1, max=1, mutex_group=None, array=False),
	))