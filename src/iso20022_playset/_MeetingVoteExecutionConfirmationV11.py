# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import DetailedInstructionStatus19
from . import Max2048Text
from . import Max35Text
from . import MeetingReference10
from . import Pagination1
from . import SecurityIdentification19
from . import SupplementaryData1

class MeetingVoteExecutionConfirmationV11(base_types._BaseFieldType):

	__slots__ = ["_FinInstrmId", "_MtgInstrId", "_MtgRef", "_Pgntn", "_SplmtryData", "_VoteExctnConfId", "_VoteInstrs", "_VoteInstrsConfURLAdr"]
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
	def MtgInstrId(self):
		return self._MtgInstrId

	@MtgInstrId.setter
	def MtgInstrId(self, value):
		self._MtgInstrId = value if value is not None else base_types.UninitialisedField(self, 'MtgInstrId', Max35Text, False)

	@MtgInstrId.deleter
	def MtgInstrId(self):
		del self._MtgInstrId
		self._MtgInstrId = base_types.UninitialisedField(self, 'MtgInstrId', Max35Text, False)

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
	def Pgntn(self):
		return self._Pgntn

	@Pgntn.setter
	def Pgntn(self, value):
		self._Pgntn = value if value is not None else base_types.UninitialisedField(self, 'Pgntn', Pagination1, False)

	@Pgntn.deleter
	def Pgntn(self):
		del self._Pgntn
		self._Pgntn = base_types.UninitialisedField(self, 'Pgntn', Pagination1, False)

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
	def VoteExctnConfId(self):
		return self._VoteExctnConfId

	@VoteExctnConfId.setter
	def VoteExctnConfId(self, value):
		self._VoteExctnConfId = value if value is not None else base_types.UninitialisedField(self, 'VoteExctnConfId', Max35Text, False)

	@VoteExctnConfId.deleter
	def VoteExctnConfId(self):
		del self._VoteExctnConfId
		self._VoteExctnConfId = base_types.UninitialisedField(self, 'VoteExctnConfId', Max35Text, False)

	@property
	def VoteInstrs(self):
		return self._VoteInstrs

	@VoteInstrs.setter
	def VoteInstrs(self, value):
		self._VoteInstrs = value if value is not None else base_types.UninitialisedField(self, 'VoteInstrs', DetailedInstructionStatus19, True)

	@VoteInstrs.deleter
	def VoteInstrs(self):
		del self._VoteInstrs
		self._VoteInstrs = base_types.UninitialisedField(self, 'VoteInstrs', DetailedInstructionStatus19, True)

	@property
	def VoteInstrsConfURLAdr(self):
		return self._VoteInstrsConfURLAdr

	@VoteInstrsConfURLAdr.setter
	def VoteInstrsConfURLAdr(self, value):
		self._VoteInstrsConfURLAdr = value if value is not None else base_types.UninitialisedField(self, 'VoteInstrsConfURLAdr', Max2048Text, False)

	@VoteInstrsConfURLAdr.deleter
	def VoteInstrsConfURLAdr(self):
		del self._VoteInstrsConfURLAdr
		self._VoteInstrsConfURLAdr = base_types.UninitialisedField(self, 'VoteInstrsConfURLAdr', Max2048Text, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='FinInstrmId', type=SecurityIdentification19, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MtgInstrId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MtgRef', type=MeetingReference10, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Pgntn', type=Pagination1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='VoteExctnConfId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='VoteInstrs', type=DetailedInstructionStatus19, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='VoteInstrsConfURLAdr', type=Max2048Text, min=0, max=1, mutex_group=None, array=False),
	))