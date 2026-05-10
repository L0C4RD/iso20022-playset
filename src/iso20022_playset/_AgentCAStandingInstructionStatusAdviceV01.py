from . import base_types
from ._StandingInstructionCancellationStatus1Choice import StandingInstructionCancellationStatus1Choice
from ._DocumentIdentification8 import DocumentIdentification8
from ._CorporateActionStandingInstructionGeneralInformation1 import CorporateActionStandingInstructionGeneralInformation1
from ._StandingInstructionStatus1Choice import StandingInstructionStatus1Choice

class AgentCAStandingInstructionStatusAdviceV01(base_types._BaseFieldType):

	__slots__ = ["_StgInstrReqSts", "_StgInstrGnlInf", "_AgtCAStgInstrCxlReqId", "_StgInstrCxlReqSts", "_Id", "_AgtCAStgInstrReqId"]
	@property
	def StgInstrReqSts(self):
		return self._StgInstrReqSts

	@StgInstrReqSts.setter
	def StgInstrReqSts(self, value):
		self._StgInstrReqSts = value if type(value) != base_types.auto else self.make_default("StgInstrReqSts")

	@StgInstrReqSts.deleter
	def StgInstrReqSts(self):
		del self._StgInstrReqSts
		self._StgInstrReqSts = None

	@property
	def StgInstrGnlInf(self):
		return self._StgInstrGnlInf

	@StgInstrGnlInf.setter
	def StgInstrGnlInf(self, value):
		self._StgInstrGnlInf = value if type(value) != base_types.auto else self.make_default("StgInstrGnlInf")

	@StgInstrGnlInf.deleter
	def StgInstrGnlInf(self):
		del self._StgInstrGnlInf
		self._StgInstrGnlInf = None

	@property
	def AgtCAStgInstrCxlReqId(self):
		return self._AgtCAStgInstrCxlReqId

	@AgtCAStgInstrCxlReqId.setter
	def AgtCAStgInstrCxlReqId(self, value):
		self._AgtCAStgInstrCxlReqId = value if type(value) != base_types.auto else self.make_default("AgtCAStgInstrCxlReqId")

	@AgtCAStgInstrCxlReqId.deleter
	def AgtCAStgInstrCxlReqId(self):
		del self._AgtCAStgInstrCxlReqId
		self._AgtCAStgInstrCxlReqId = None

	@property
	def StgInstrCxlReqSts(self):
		return self._StgInstrCxlReqSts

	@StgInstrCxlReqSts.setter
	def StgInstrCxlReqSts(self, value):
		self._StgInstrCxlReqSts = value if type(value) != base_types.auto else self.make_default("StgInstrCxlReqSts")

	@StgInstrCxlReqSts.deleter
	def StgInstrCxlReqSts(self):
		del self._StgInstrCxlReqSts
		self._StgInstrCxlReqSts = None

	@property
	def Id(self):
		return self._Id

	@Id.setter
	def Id(self, value):
		self._Id = value if type(value) != base_types.auto else self.make_default("Id")

	@Id.deleter
	def Id(self):
		del self._Id
		self._Id = None

	@property
	def AgtCAStgInstrReqId(self):
		return self._AgtCAStgInstrReqId

	@AgtCAStgInstrReqId.setter
	def AgtCAStgInstrReqId(self, value):
		self._AgtCAStgInstrReqId = value if type(value) != base_types.auto else self.make_default("AgtCAStgInstrReqId")

	@AgtCAStgInstrReqId.deleter
	def AgtCAStgInstrReqId(self):
		del self._AgtCAStgInstrReqId
		self._AgtCAStgInstrReqId = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='StgInstrReqSts', type=StandingInstructionStatus1Choice, min=0, max=1, mutex_group=2, array=False),
		base_types.FieldEntry(name='StgInstrGnlInf', type=CorporateActionStandingInstructionGeneralInformation1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AgtCAStgInstrCxlReqId', type=DocumentIdentification8, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='StgInstrCxlReqSts', type=StandingInstructionCancellationStatus1Choice, min=0, max=1, mutex_group=2, array=False),
		base_types.FieldEntry(name='Id', type=DocumentIdentification8, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AgtCAStgInstrReqId', type=DocumentIdentification8, min=0, max=1, mutex_group=1, array=False),
	))

