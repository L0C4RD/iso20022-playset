from . import base_types
from .CorporateActionDeactivationInstruction1 import CorporateActionDeactivationInstruction1
from .DocumentIdentification8 import DocumentIdentification8
from .CorporateActionInformation1 import CorporateActionInformation1

class AgentCADeactivationInstructionV01(base_types._BaseFieldType):

	__slots__ = ["_Id", "_CorpActnGnlInf", "_DeactvtnDtls"]
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
	def CorpActnGnlInf(self):
		return self._CorpActnGnlInf

	@CorpActnGnlInf.setter
	def CorpActnGnlInf(self, value):
		self._CorpActnGnlInf = value if type(value) != base_types.auto else self.make_default("CorpActnGnlInf")

	@CorpActnGnlInf.deleter
	def CorpActnGnlInf(self):
		del self._CorpActnGnlInf
		self._CorpActnGnlInf = None

	@property
	def DeactvtnDtls(self):
		return self._DeactvtnDtls

	@DeactvtnDtls.setter
	def DeactvtnDtls(self, value):
		self._DeactvtnDtls = value if type(value) != base_types.auto else self.make_default("DeactvtnDtls")

	@DeactvtnDtls.deleter
	def DeactvtnDtls(self):
		del self._DeactvtnDtls
		self._DeactvtnDtls = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Id', type=DocumentIdentification8, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CorpActnGnlInf', type=CorporateActionInformation1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DeactvtnDtls', type=CorporateActionDeactivationInstruction1, min=1, max=1, mutex_group=None, array=False),
	))

