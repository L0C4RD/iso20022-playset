# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CorporateActionStandingInstructionGeneralInformation1
from . import DocumentIdentification8
from . import StandingInstructionCancellationStatus1Choice
from . import StandingInstructionStatus1Choice

class AgentCAStandingInstructionStatusAdviceV01(base_types._BaseFieldType):

	__slots__ = ["_AgtCAStgInstrCxlReqId", "_AgtCAStgInstrReqId", "_Id", "_StgInstrCxlReqSts", "_StgInstrGnlInf", "_StgInstrReqSts"]
	@property
	def AgtCAStgInstrCxlReqId(self):
		return self._AgtCAStgInstrCxlReqId

	@AgtCAStgInstrCxlReqId.setter
	def AgtCAStgInstrCxlReqId(self, value):
		self._AgtCAStgInstrCxlReqId = value if value is not None else base_types.UninitialisedField(self, 'AgtCAStgInstrCxlReqId', DocumentIdentification8, False)

	@AgtCAStgInstrCxlReqId.deleter
	def AgtCAStgInstrCxlReqId(self):
		del self._AgtCAStgInstrCxlReqId
		self._AgtCAStgInstrCxlReqId = base_types.UninitialisedField(self, 'AgtCAStgInstrCxlReqId', DocumentIdentification8, False)

	@property
	def AgtCAStgInstrReqId(self):
		return self._AgtCAStgInstrReqId

	@AgtCAStgInstrReqId.setter
	def AgtCAStgInstrReqId(self, value):
		self._AgtCAStgInstrReqId = value if value is not None else base_types.UninitialisedField(self, 'AgtCAStgInstrReqId', DocumentIdentification8, False)

	@AgtCAStgInstrReqId.deleter
	def AgtCAStgInstrReqId(self):
		del self._AgtCAStgInstrReqId
		self._AgtCAStgInstrReqId = base_types.UninitialisedField(self, 'AgtCAStgInstrReqId', DocumentIdentification8, False)

	@property
	def Id(self):
		return self._Id

	@Id.setter
	def Id(self, value):
		self._Id = value if value is not None else base_types.UninitialisedField(self, 'Id', DocumentIdentification8, False)

	@Id.deleter
	def Id(self):
		del self._Id
		self._Id = base_types.UninitialisedField(self, 'Id', DocumentIdentification8, False)

	@property
	def StgInstrCxlReqSts(self):
		return self._StgInstrCxlReqSts

	@StgInstrCxlReqSts.setter
	def StgInstrCxlReqSts(self, value):
		self._StgInstrCxlReqSts = value if value is not None else base_types.UninitialisedField(self, 'StgInstrCxlReqSts', StandingInstructionCancellationStatus1Choice, False)

	@StgInstrCxlReqSts.deleter
	def StgInstrCxlReqSts(self):
		del self._StgInstrCxlReqSts
		self._StgInstrCxlReqSts = base_types.UninitialisedField(self, 'StgInstrCxlReqSts', StandingInstructionCancellationStatus1Choice, False)

	@property
	def StgInstrGnlInf(self):
		return self._StgInstrGnlInf

	@StgInstrGnlInf.setter
	def StgInstrGnlInf(self, value):
		self._StgInstrGnlInf = value if value is not None else base_types.UninitialisedField(self, 'StgInstrGnlInf', CorporateActionStandingInstructionGeneralInformation1, False)

	@StgInstrGnlInf.deleter
	def StgInstrGnlInf(self):
		del self._StgInstrGnlInf
		self._StgInstrGnlInf = base_types.UninitialisedField(self, 'StgInstrGnlInf', CorporateActionStandingInstructionGeneralInformation1, False)

	@property
	def StgInstrReqSts(self):
		return self._StgInstrReqSts

	@StgInstrReqSts.setter
	def StgInstrReqSts(self, value):
		self._StgInstrReqSts = value if value is not None else base_types.UninitialisedField(self, 'StgInstrReqSts', StandingInstructionStatus1Choice, False)

	@StgInstrReqSts.deleter
	def StgInstrReqSts(self):
		del self._StgInstrReqSts
		self._StgInstrReqSts = base_types.UninitialisedField(self, 'StgInstrReqSts', StandingInstructionStatus1Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AgtCAStgInstrCxlReqId', type=DocumentIdentification8, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='AgtCAStgInstrReqId', type=DocumentIdentification8, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Id', type=DocumentIdentification8, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StgInstrCxlReqSts', type=StandingInstructionCancellationStatus1Choice, min=0, max=1, mutex_group=2, array=False),
		base_types.FieldEntry(name='StgInstrGnlInf', type=CorporateActionStandingInstructionGeneralInformation1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StgInstrReqSts', type=StandingInstructionStatus1Choice, min=0, max=1, mutex_group=2, array=False),
	))