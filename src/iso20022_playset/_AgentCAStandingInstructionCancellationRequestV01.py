# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CorporateActionStandingInstruction1
from . import CorporateActionStandingInstructionGeneralInformation1
from . import DocumentIdentification8

class AgentCAStandingInstructionCancellationRequestV01(base_types._BaseFieldType):

	__slots__ = ["_AgtCAStgInstrReqId", "_Id", "_StgInstrDtls", "_StgInstrGnlInf"]
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
	def StgInstrDtls(self):
		return self._StgInstrDtls

	@StgInstrDtls.setter
	def StgInstrDtls(self, value):
		self._StgInstrDtls = value if value is not None else base_types.UninitialisedField(self, 'StgInstrDtls', CorporateActionStandingInstruction1, False)

	@StgInstrDtls.deleter
	def StgInstrDtls(self):
		del self._StgInstrDtls
		self._StgInstrDtls = base_types.UninitialisedField(self, 'StgInstrDtls', CorporateActionStandingInstruction1, False)

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

	_field_defs = frozenset((
		base_types.FieldEntry(name='AgtCAStgInstrReqId', type=DocumentIdentification8, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Id', type=DocumentIdentification8, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StgInstrDtls', type=CorporateActionStandingInstruction1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StgInstrGnlInf', type=CorporateActionStandingInstructionGeneralInformation1, min=1, max=1, mutex_group=None, array=False),
	))