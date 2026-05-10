from . import base_types
from .Max35Text import Max35Text
from .SecurityIdentification19 import SecurityIdentification19
from .SupplementaryData1 import SupplementaryData1
from .MeetingReference10 import MeetingReference10
from .CancelInstruction5 import CancelInstruction5

class MeetingInstructionCancellationRequestV10(base_types._BaseFieldType):

	__slots__ = ["_ToBeCancInstr", "_MtgRef", "_SplmtryData", "_FinInstrmId", "_MtgInstrId"]
	@property
	def ToBeCancInstr(self):
		return self._ToBeCancInstr

	@ToBeCancInstr.setter
	def ToBeCancInstr(self, value):
		self._ToBeCancInstr = value if type(value) != auto else self.make_default("ToBeCancInstr")

	@ToBeCancInstr.deleter
	def ToBeCancInstr(self):
		del self._ToBeCancInstr
		self._ToBeCancInstr = None

	@property
	def MtgRef(self):
		return self._MtgRef

	@MtgRef.setter
	def MtgRef(self, value):
		self._MtgRef = value if type(value) != auto else self.make_default("MtgRef")

	@MtgRef.deleter
	def MtgRef(self):
		del self._MtgRef
		self._MtgRef = None

	@property
	def SplmtryData(self):
		return self._SplmtryData

	@SplmtryData.setter
	def SplmtryData(self, value):
		self._SplmtryData = value if type(value) != auto else self.make_default("SplmtryData")

	@SplmtryData.deleter
	def SplmtryData(self):
		del self._SplmtryData
		self._SplmtryData = None

	@property
	def FinInstrmId(self):
		return self._FinInstrmId

	@FinInstrmId.setter
	def FinInstrmId(self, value):
		self._FinInstrmId = value if type(value) != auto else self.make_default("FinInstrmId")

	@FinInstrmId.deleter
	def FinInstrmId(self):
		del self._FinInstrmId
		self._FinInstrmId = None

	@property
	def MtgInstrId(self):
		return self._MtgInstrId

	@MtgInstrId.setter
	def MtgInstrId(self, value):
		self._MtgInstrId = value if type(value) != auto else self.make_default("MtgInstrId")

	@MtgInstrId.deleter
	def MtgInstrId(self):
		del self._MtgInstrId
		self._MtgInstrId = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='ToBeCancInstr', type=CancelInstruction5, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='MtgRef', type=MeetingReference10, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='FinInstrmId', type=SecurityIdentification19, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MtgInstrId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
	))

