from . import base_types
from ._AmountAndDirection102 import AmountAndDirection102

class StressLiquidResourceRequirement1(base_types._BaseFieldType):

	__slots__ = ["_SttlmOrDlvry", "_VartnMrgnPmtOblgtn", "_Othr", "_OprlOutflw"]
	@property
	def OprlOutflw(self):
		return self._OprlOutflw

	@OprlOutflw.setter
	def OprlOutflw(self, value):
		self._OprlOutflw = value if type(value) != base_types.auto else self.make_default("OprlOutflw")

	@OprlOutflw.deleter
	def OprlOutflw(self):
		del self._OprlOutflw
		self._OprlOutflw = None

	@property
	def Othr(self):
		return self._Othr

	@Othr.setter
	def Othr(self, value):
		self._Othr = value if type(value) != base_types.auto else self.make_default("Othr")

	@Othr.deleter
	def Othr(self):
		del self._Othr
		self._Othr = None

	@property
	def SttlmOrDlvry(self):
		return self._SttlmOrDlvry

	@SttlmOrDlvry.setter
	def SttlmOrDlvry(self, value):
		self._SttlmOrDlvry = value if type(value) != base_types.auto else self.make_default("SttlmOrDlvry")

	@SttlmOrDlvry.deleter
	def SttlmOrDlvry(self):
		del self._SttlmOrDlvry
		self._SttlmOrDlvry = None

	@property
	def VartnMrgnPmtOblgtn(self):
		return self._VartnMrgnPmtOblgtn

	@VartnMrgnPmtOblgtn.setter
	def VartnMrgnPmtOblgtn(self, value):
		self._VartnMrgnPmtOblgtn = value if type(value) != base_types.auto else self.make_default("VartnMrgnPmtOblgtn")

	@VartnMrgnPmtOblgtn.deleter
	def VartnMrgnPmtOblgtn(self):
		del self._VartnMrgnPmtOblgtn
		self._VartnMrgnPmtOblgtn = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='OprlOutflw', type=AmountAndDirection102, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Othr', type=AmountAndDirection102, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SttlmOrDlvry', type=AmountAndDirection102, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='VartnMrgnPmtOblgtn', type=AmountAndDirection102, min=1, max=1, mutex_group=None, array=False),
	))

