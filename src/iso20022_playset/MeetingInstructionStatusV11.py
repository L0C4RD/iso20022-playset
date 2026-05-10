from . import base_types
from .MeetingReference10 import MeetingReference10
from .SupplementaryData1 import SupplementaryData1
from .InstructionType2Choice import InstructionType2Choice
from .SecurityIdentification19 import SecurityIdentification19
from .PartyIdentification226Choice import PartyIdentification226Choice
from .InstructionTypeStatus7Choice import InstructionTypeStatus7Choice
from .PartyIdentification246Choice import PartyIdentification246Choice
from .EligiblePosition17 import EligiblePosition17

class MeetingInstructionStatusV11(base_types._BaseFieldType):

	__slots__ = ["_InstrTpSts", "_VoteCstgPty", "_RghtsHldr", "_InstrTp", "_SplmtryData", "_FinInstrmId", "_Pos", "_CnfrmgPty", "_MtgRef"]
	@property
	def InstrTpSts(self):
		return self._InstrTpSts

	@InstrTpSts.setter
	def InstrTpSts(self, value):
		self._InstrTpSts = value if type(value) != base_types.auto else self.make_default("InstrTpSts")

	@InstrTpSts.deleter
	def InstrTpSts(self):
		del self._InstrTpSts
		self._InstrTpSts = None

	@property
	def VoteCstgPty(self):
		return self._VoteCstgPty

	@VoteCstgPty.setter
	def VoteCstgPty(self, value):
		self._VoteCstgPty = value if type(value) != base_types.auto else self.make_default("VoteCstgPty")

	@VoteCstgPty.deleter
	def VoteCstgPty(self):
		del self._VoteCstgPty
		self._VoteCstgPty = None

	@property
	def RghtsHldr(self):
		return self._RghtsHldr

	@RghtsHldr.setter
	def RghtsHldr(self, value):
		self._RghtsHldr = value if type(value) != base_types.auto else self.make_default("RghtsHldr")

	@RghtsHldr.deleter
	def RghtsHldr(self):
		del self._RghtsHldr
		self._RghtsHldr = None

	@property
	def InstrTp(self):
		return self._InstrTp

	@InstrTp.setter
	def InstrTp(self, value):
		self._InstrTp = value if type(value) != base_types.auto else self.make_default("InstrTp")

	@InstrTp.deleter
	def InstrTp(self):
		del self._InstrTp
		self._InstrTp = None

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
	def Pos(self):
		return self._Pos

	@Pos.setter
	def Pos(self, value):
		self._Pos = value if type(value) != base_types.auto else self.make_default("Pos")

	@Pos.deleter
	def Pos(self):
		del self._Pos
		self._Pos = None

	@property
	def CnfrmgPty(self):
		return self._CnfrmgPty

	@CnfrmgPty.setter
	def CnfrmgPty(self, value):
		self._CnfrmgPty = value if type(value) != base_types.auto else self.make_default("CnfrmgPty")

	@CnfrmgPty.deleter
	def CnfrmgPty(self):
		del self._CnfrmgPty
		self._CnfrmgPty = None

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
		base_types.FieldEntry(name='InstrTpSts', type=InstructionTypeStatus7Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='VoteCstgPty', type=PartyIdentification226Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RghtsHldr', type=PartyIdentification246Choice, min=0, max=250, mutex_group=None, array=True),
		base_types.FieldEntry(name='InstrTp', type=InstructionType2Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='FinInstrmId', type=SecurityIdentification19, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Pos', type=EligiblePosition17, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CnfrmgPty', type=PartyIdentification226Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MtgRef', type=MeetingReference10, min=1, max=1, mutex_group=None, array=False),
	))

