from . import base_types
from .CorporateActionStandingInstructionGeneralInformation1 import CorporateActionStandingInstructionGeneralInformation1
from .CorporateActionStandingInstruction1 import CorporateActionStandingInstruction1
from .DocumentIdentification8 import DocumentIdentification8

class AgentCAStandingInstructionCancellationRequestV01(base_types._BaseFieldType):

	__slots__ = ["_AgtCAStgInstrReqId", "_StgInstrGnlInf", "_Id", "_StgInstrDtls"]
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
	def StgInstrDtls(self):
		return self._StgInstrDtls

	@StgInstrDtls.setter
	def StgInstrDtls(self, value):
		self._StgInstrDtls = value if type(value) != base_types.auto else self.make_default("StgInstrDtls")

	@StgInstrDtls.deleter
	def StgInstrDtls(self):
		del self._StgInstrDtls
		self._StgInstrDtls = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AgtCAStgInstrReqId', type=DocumentIdentification8, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StgInstrGnlInf', type=CorporateActionStandingInstructionGeneralInformation1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Id', type=DocumentIdentification8, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StgInstrDtls', type=CorporateActionStandingInstruction1, min=0, max=1, mutex_group=None, array=False),
	))

