from . import base_types
from ._CorporateActionInformation1 import CorporateActionInformation1
from ._DocumentIdentification8 import DocumentIdentification8
from ._CorporateActionDeactivationInstruction1 import CorporateActionDeactivationInstruction1

class AgentCADeactivationCancellationRequestV01(base_types._BaseFieldType):

	__slots__ = ["_AgtCADeactvtnInstrId", "_Id", "_DeactvtnInstrDtls", "_CorpActnGnlInf"]
	@property
	def AgtCADeactvtnInstrId(self):
		return self._AgtCADeactvtnInstrId

	@AgtCADeactvtnInstrId.setter
	def AgtCADeactvtnInstrId(self, value):
		self._AgtCADeactvtnInstrId = value if type(value) != base_types.auto else self.make_default("AgtCADeactvtnInstrId")

	@AgtCADeactvtnInstrId.deleter
	def AgtCADeactvtnInstrId(self):
		del self._AgtCADeactvtnInstrId
		self._AgtCADeactvtnInstrId = None

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
	def DeactvtnInstrDtls(self):
		return self._DeactvtnInstrDtls

	@DeactvtnInstrDtls.setter
	def DeactvtnInstrDtls(self, value):
		self._DeactvtnInstrDtls = value if type(value) != base_types.auto else self.make_default("DeactvtnInstrDtls")

	@DeactvtnInstrDtls.deleter
	def DeactvtnInstrDtls(self):
		del self._DeactvtnInstrDtls
		self._DeactvtnInstrDtls = None

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

	_field_defs = frozenset((
		base_types.FieldEntry(name='AgtCADeactvtnInstrId', type=DocumentIdentification8, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Id', type=DocumentIdentification8, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DeactvtnInstrDtls', type=CorporateActionDeactivationInstruction1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CorpActnGnlInf', type=CorporateActionInformation1, min=1, max=1, mutex_group=None, array=False),
	))

