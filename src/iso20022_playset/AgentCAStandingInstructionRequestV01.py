from . import base_types
from .CorporateActionStandingInstruction1 import CorporateActionStandingInstruction1
from .CorporateActionStandingInstructionGeneralInformation1 import CorporateActionStandingInstructionGeneralInformation1
from .DocumentIdentification8 import DocumentIdentification8
from .ContactPerson1 import ContactPerson1

class AgentCAStandingInstructionRequestV01(base_types._BaseFieldType):

	__slots__ = ["_Id", "_StgInstrDtls", "_CtctDtls", "_StgInstrGnlInf"]
	@property
	def Id(self):
		return self._Id

	@Id.setter
	def Id(self, value):
		self._Id = value if type(value) != auto else self.make_default("Id")

	@Id.deleter
	def Id(self):
		del self._Id
		self._Id = None

	@property
	def StgInstrDtls(self):
		return self._StgInstrDtls

	@StgInstrDtls.setter
	def StgInstrDtls(self, value):
		self._StgInstrDtls = value if type(value) != auto else self.make_default("StgInstrDtls")

	@StgInstrDtls.deleter
	def StgInstrDtls(self):
		del self._StgInstrDtls
		self._StgInstrDtls = None

	@property
	def CtctDtls(self):
		return self._CtctDtls

	@CtctDtls.setter
	def CtctDtls(self, value):
		self._CtctDtls = value if type(value) != auto else self.make_default("CtctDtls")

	@CtctDtls.deleter
	def CtctDtls(self):
		del self._CtctDtls
		self._CtctDtls = None

	@property
	def StgInstrGnlInf(self):
		return self._StgInstrGnlInf

	@StgInstrGnlInf.setter
	def StgInstrGnlInf(self, value):
		self._StgInstrGnlInf = value if type(value) != auto else self.make_default("StgInstrGnlInf")

	@StgInstrGnlInf.deleter
	def StgInstrGnlInf(self):
		del self._StgInstrGnlInf
		self._StgInstrGnlInf = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Id', type=DocumentIdentification8, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StgInstrDtls', type=CorporateActionStandingInstruction1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CtctDtls', type=ContactPerson1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StgInstrGnlInf', type=CorporateActionStandingInstructionGeneralInformation1, min=1, max=1, mutex_group=None, array=False),
	))

