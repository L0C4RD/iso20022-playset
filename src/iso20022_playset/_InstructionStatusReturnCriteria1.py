from . import base_types
from ._RequestedIndicator import RequestedIndicator

class InstructionStatusReturnCriteria1(base_types._BaseFieldType):

	__slots__ = ["_PmtInstrStsDtTmInd", "_PmtInstrStsInd", "_PmtInstrStsRsnInd"]
	@property
	def PmtInstrStsDtTmInd(self):
		return self._PmtInstrStsDtTmInd

	@PmtInstrStsDtTmInd.setter
	def PmtInstrStsDtTmInd(self, value):
		self._PmtInstrStsDtTmInd = value if type(value) != base_types.auto else self.make_default("PmtInstrStsDtTmInd")

	@PmtInstrStsDtTmInd.deleter
	def PmtInstrStsDtTmInd(self):
		del self._PmtInstrStsDtTmInd
		self._PmtInstrStsDtTmInd = None

	@property
	def PmtInstrStsInd(self):
		return self._PmtInstrStsInd

	@PmtInstrStsInd.setter
	def PmtInstrStsInd(self, value):
		self._PmtInstrStsInd = value if type(value) != base_types.auto else self.make_default("PmtInstrStsInd")

	@PmtInstrStsInd.deleter
	def PmtInstrStsInd(self):
		del self._PmtInstrStsInd
		self._PmtInstrStsInd = None

	@property
	def PmtInstrStsRsnInd(self):
		return self._PmtInstrStsRsnInd

	@PmtInstrStsRsnInd.setter
	def PmtInstrStsRsnInd(self, value):
		self._PmtInstrStsRsnInd = value if type(value) != base_types.auto else self.make_default("PmtInstrStsRsnInd")

	@PmtInstrStsRsnInd.deleter
	def PmtInstrStsRsnInd(self):
		del self._PmtInstrStsRsnInd
		self._PmtInstrStsRsnInd = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='PmtInstrStsDtTmInd', type=RequestedIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PmtInstrStsInd', type=RequestedIndicator, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PmtInstrStsRsnInd', type=RequestedIndicator, min=0, max=1, mutex_group=None, array=False),
	))

