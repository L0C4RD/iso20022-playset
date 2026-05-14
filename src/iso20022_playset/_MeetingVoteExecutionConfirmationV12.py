# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._DetailedInstructionStatus22 import DetailedInstructionStatus22
from ._Max2048Text import Max2048Text
from ._Max35Text import Max35Text
from ._MeetingReference10 import MeetingReference10
from ._Pagination1 import Pagination1
from ._SecurityIdentification19 import SecurityIdentification19
from ._SupplementaryData1 import SupplementaryData1

class MeetingVoteExecutionConfirmationV12(base_types._BaseFieldType):

	__slots__ = ["_FinInstrmId", "_MtgInstrId", "_MtgRef", "_Pgntn", "_SplmtryData", "_VoteExctnConfId", "_VoteInstrs", "_VoteInstrsConfURLAdr"]
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
	def MtgRef(self):
		return self._MtgRef

	@MtgRef.setter
	def MtgRef(self, value):
		self._MtgRef = value if type(value) != base_types.auto else self.make_default("MtgRef")

	@MtgRef.deleter
	def MtgRef(self):
		del self._MtgRef
		self._MtgRef = None

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
	def VoteExctnConfId(self):
		return self._VoteExctnConfId

	@VoteExctnConfId.setter
	def VoteExctnConfId(self, value):
		self._VoteExctnConfId = value if type(value) != base_types.auto else self.make_default("VoteExctnConfId")

	@VoteExctnConfId.deleter
	def VoteExctnConfId(self):
		del self._VoteExctnConfId
		self._VoteExctnConfId = None

	@property
	def VoteInstrs(self):
		return self._VoteInstrs

	@VoteInstrs.setter
	def VoteInstrs(self, value):
		self._VoteInstrs = value if type(value) != base_types.auto else self.make_default("VoteInstrs")

	@VoteInstrs.deleter
	def VoteInstrs(self):
		del self._VoteInstrs
		self._VoteInstrs = None

	@property
	def VoteInstrsConfURLAdr(self):
		return self._VoteInstrsConfURLAdr

	@VoteInstrsConfURLAdr.setter
	def VoteInstrsConfURLAdr(self, value):
		self._VoteInstrsConfURLAdr = value if type(value) != base_types.auto else self.make_default("VoteInstrsConfURLAdr")

	@VoteInstrsConfURLAdr.deleter
	def VoteInstrsConfURLAdr(self):
		del self._VoteInstrsConfURLAdr
		self._VoteInstrsConfURLAdr = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='FinInstrmId', type=SecurityIdentification19, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MtgInstrId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MtgRef', type=MeetingReference10, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Pgntn', type=Pagination1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='VoteExctnConfId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='VoteInstrs', type=DetailedInstructionStatus22, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='VoteInstrsConfURLAdr', type=Max2048Text, min=0, max=1, mutex_group=None, array=False),
	))