# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import EligiblePosition17
from . import InstructionType2Choice
from . import InstructionTypeStatus8Choice
from . import MeetingReference10
from . import PartyIdentification226Choice
from . import PartyIdentification246Choice
from . import SecurityIdentification19
from . import SupplementaryData1

class MeetingInstructionStatusV12(base_types._BaseFieldType):

	__slots__ = ["_CnfrmgPty", "_FinInstrmId", "_InstrTp", "_InstrTpSts", "_MtgRef", "_Pos", "_RghtsHldr", "_SplmtryData", "_VoteCstgPty"]
	@property
	def CnfrmgPty(self):
		return self._CnfrmgPty

	@CnfrmgPty.setter
	def CnfrmgPty(self, value):
		self._CnfrmgPty = value if value is not None else base_types.UninitialisedField(self, 'CnfrmgPty', PartyIdentification226Choice, False)

	@CnfrmgPty.deleter
	def CnfrmgPty(self):
		del self._CnfrmgPty
		self._CnfrmgPty = base_types.UninitialisedField(self, 'CnfrmgPty', PartyIdentification226Choice, False)

	@property
	def FinInstrmId(self):
		return self._FinInstrmId

	@FinInstrmId.setter
	def FinInstrmId(self, value):
		self._FinInstrmId = value if value is not None else base_types.UninitialisedField(self, 'FinInstrmId', SecurityIdentification19, False)

	@FinInstrmId.deleter
	def FinInstrmId(self):
		del self._FinInstrmId
		self._FinInstrmId = base_types.UninitialisedField(self, 'FinInstrmId', SecurityIdentification19, False)

	@property
	def InstrTp(self):
		return self._InstrTp

	@InstrTp.setter
	def InstrTp(self, value):
		self._InstrTp = value if value is not None else base_types.UninitialisedField(self, 'InstrTp', InstructionType2Choice, False)

	@InstrTp.deleter
	def InstrTp(self):
		del self._InstrTp
		self._InstrTp = base_types.UninitialisedField(self, 'InstrTp', InstructionType2Choice, False)

	@property
	def InstrTpSts(self):
		return self._InstrTpSts

	@InstrTpSts.setter
	def InstrTpSts(self, value):
		self._InstrTpSts = value if value is not None else base_types.UninitialisedField(self, 'InstrTpSts', InstructionTypeStatus8Choice, False)

	@InstrTpSts.deleter
	def InstrTpSts(self):
		del self._InstrTpSts
		self._InstrTpSts = base_types.UninitialisedField(self, 'InstrTpSts', InstructionTypeStatus8Choice, False)

	@property
	def MtgRef(self):
		return self._MtgRef

	@MtgRef.setter
	def MtgRef(self, value):
		self._MtgRef = value if value is not None else base_types.UninitialisedField(self, 'MtgRef', MeetingReference10, False)

	@MtgRef.deleter
	def MtgRef(self):
		del self._MtgRef
		self._MtgRef = base_types.UninitialisedField(self, 'MtgRef', MeetingReference10, False)

	@property
	def Pos(self):
		return self._Pos

	@Pos.setter
	def Pos(self, value):
		self._Pos = value if value is not None else base_types.UninitialisedField(self, 'Pos', EligiblePosition17, False)

	@Pos.deleter
	def Pos(self):
		del self._Pos
		self._Pos = base_types.UninitialisedField(self, 'Pos', EligiblePosition17, False)

	@property
	def RghtsHldr(self):
		return self._RghtsHldr

	@RghtsHldr.setter
	def RghtsHldr(self, value):
		self._RghtsHldr = value if value is not None else base_types.UninitialisedField(self, 'RghtsHldr', PartyIdentification246Choice, True)

	@RghtsHldr.deleter
	def RghtsHldr(self):
		del self._RghtsHldr
		self._RghtsHldr = base_types.UninitialisedField(self, 'RghtsHldr', PartyIdentification246Choice, True)

	@property
	def SplmtryData(self):
		return self._SplmtryData

	@SplmtryData.setter
	def SplmtryData(self, value):
		self._SplmtryData = value if value is not None else base_types.UninitialisedField(self, 'SplmtryData', SupplementaryData1, True)

	@SplmtryData.deleter
	def SplmtryData(self):
		del self._SplmtryData
		self._SplmtryData = base_types.UninitialisedField(self, 'SplmtryData', SupplementaryData1, True)

	@property
	def VoteCstgPty(self):
		return self._VoteCstgPty

	@VoteCstgPty.setter
	def VoteCstgPty(self, value):
		self._VoteCstgPty = value if value is not None else base_types.UninitialisedField(self, 'VoteCstgPty', PartyIdentification226Choice, False)

	@VoteCstgPty.deleter
	def VoteCstgPty(self):
		del self._VoteCstgPty
		self._VoteCstgPty = base_types.UninitialisedField(self, 'VoteCstgPty', PartyIdentification226Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='CnfrmgPty', type=PartyIdentification226Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FinInstrmId', type=SecurityIdentification19, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InstrTp', type=InstructionType2Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InstrTpSts', type=InstructionTypeStatus8Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MtgRef', type=MeetingReference10, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Pos', type=EligiblePosition17, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RghtsHldr', type=PartyIdentification246Choice, min=0, max=250, mutex_group=None, array=True),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='VoteCstgPty', type=PartyIdentification226Choice, min=1, max=1, mutex_group=None, array=False),
	))