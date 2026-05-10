from . import base_types
from .MeetingInstructionCancellation1 import MeetingInstructionCancellation1
from .MeetingInstructionIdentification1 import MeetingInstructionIdentification1
from .Instruction8 import Instruction8
from .MeetingReference10 import MeetingReference10
from .SupplementaryData1 import SupplementaryData1
from .SecurityIdentification19 import SecurityIdentification19
from .Max35Text import Max35Text
from .Pagination1 import Pagination1
from .DocumentIdentification32 import DocumentIdentification32

class MeetingInstructionV10(base_types._BaseFieldType):

	__slots__ = ["_MtgInstrId", "_OthrDocId", "_Instr", "_SplmtryData", "_InstrCxlReqId", "_FinInstrmId", "_Pgntn", "_CancInstrId", "_MtgRef"]
	@property
	def MtgInstrId(self):
		return self._MtgInstrId

	@MtgInstrId.setter
	def MtgInstrId(self, value):
		self._MtgInstrId = value if type(value) != base_types.auto else self.make_default("MtgInstrId")

	@MtgInstrId.deleter
	def MtgInstrId(self):
		del self._MtgInstrId
		self._MtgInstrId = None

	@property
	def OthrDocId(self):
		return self._OthrDocId

	@OthrDocId.setter
	def OthrDocId(self, value):
		self._OthrDocId = value if type(value) != base_types.auto else self.make_default("OthrDocId")

	@OthrDocId.deleter
	def OthrDocId(self):
		del self._OthrDocId
		self._OthrDocId = None

	@property
	def Instr(self):
		return self._Instr

	@Instr.setter
	def Instr(self, value):
		self._Instr = value if type(value) != base_types.auto else self.make_default("Instr")

	@Instr.deleter
	def Instr(self):
		del self._Instr
		self._Instr = None

	@property
	def SplmtryData(self):
		return self._SplmtryData

	@SplmtryData.setter
	def SplmtryData(self, value):
		self._SplmtryData = value if type(value) != base_types.auto else self.make_default("SplmtryData")

	@SplmtryData.deleter
	def SplmtryData(self):
		del self._SplmtryData
		self._SplmtryData = None

	@property
	def InstrCxlReqId(self):
		return self._InstrCxlReqId

	@InstrCxlReqId.setter
	def InstrCxlReqId(self, value):
		self._InstrCxlReqId = value if type(value) != base_types.auto else self.make_default("InstrCxlReqId")

	@InstrCxlReqId.deleter
	def InstrCxlReqId(self):
		del self._InstrCxlReqId
		self._InstrCxlReqId = None

	@property
	def FinInstrmId(self):
		return self._FinInstrmId

	@FinInstrmId.setter
	def FinInstrmId(self, value):
		self._FinInstrmId = value if type(value) != base_types.auto else self.make_default("FinInstrmId")

	@FinInstrmId.deleter
	def FinInstrmId(self):
		del self._FinInstrmId
		self._FinInstrmId = None

	@property
	def Pgntn(self):
		return self._Pgntn

	@Pgntn.setter
	def Pgntn(self, value):
		self._Pgntn = value if type(value) != base_types.auto else self.make_default("Pgntn")

	@Pgntn.deleter
	def Pgntn(self):
		del self._Pgntn
		self._Pgntn = None

	@property
	def CancInstrId(self):
		return self._CancInstrId

	@CancInstrId.setter
	def CancInstrId(self, value):
		self._CancInstrId = value if type(value) != base_types.auto else self.make_default("CancInstrId")

	@CancInstrId.deleter
	def CancInstrId(self):
		del self._CancInstrId
		self._CancInstrId = None

	@property
	def MtgRef(self):
		return self._MtgRef

	@MtgRef.setter
	def MtgRef(self, value):
		self._MtgRef = value if type(value) != base_types.auto else self.make_default("MtgRef")

	@MtgRef.deleter
	def MtgRef(self):
		del self._MtgRef
		self._MtgRef = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='MtgInstrId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OthrDocId', type=DocumentIdentification32, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Instr', type=Instruction8, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='InstrCxlReqId', type=MeetingInstructionCancellation1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='FinInstrmId', type=SecurityIdentification19, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Pgntn', type=Pagination1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CancInstrId', type=MeetingInstructionIdentification1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='MtgRef', type=MeetingReference10, min=1, max=1, mutex_group=None, array=False),
	))

