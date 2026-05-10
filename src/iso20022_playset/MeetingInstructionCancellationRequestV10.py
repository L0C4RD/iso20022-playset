import base_types
import Max35Text
import SecurityIdentification19
import CancelInstruction5
import SupplementaryData1
import MeetingReference10

class MeetingInstructionCancellationRequestV10(base_types._BaseFieldType):

	__slots__ = ["_ToBeCancInstr", "_SplmtryData", "_MtgInstrId", "_MtgRef", "_FinInstrmId"]
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
	def MtgInstrId(self):
		return self._MtgInstrId

	@MtgInstrId.setter
	def MtgInstrId(self, value):
		self._MtgInstrId = value if type(value) != auto else self.make_default("MtgInstrId")

	@MtgInstrId.deleter
	def MtgInstrId(self):
		del self._MtgInstrId
		self._MtgInstrId = None

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
	def FinInstrmId(self):
		return self._FinInstrmId

	@FinInstrmId.setter
	def FinInstrmId(self, value):
		self._FinInstrmId = value if type(value) != auto else self.make_default("FinInstrmId")

	@FinInstrmId.deleter
	def FinInstrmId(self):
		del self._FinInstrmId
		self._FinInstrmId = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='ToBeCancInstr', type=CancelInstruction5, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='MtgInstrId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MtgRef', type=MeetingReference10, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FinInstrmId', type=SecurityIdentification19, min=1, max=1, mutex_group=None, array=False),
	))

