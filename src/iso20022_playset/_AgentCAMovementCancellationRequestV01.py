from . import base_types
from .MovementInstruction1 import MovementInstruction1
from .DocumentIdentification8 import DocumentIdentification8
from .CorporateActionInformation1 import CorporateActionInformation1

class AgentCAMovementCancellationRequestV01(base_types._BaseFieldType):

	__slots__ = ["_MvmntDtls", "_Id", "_CorpActnGnlInf", "_AgtCAMvmntInstrId"]
	@property
	def MvmntDtls(self):
		return self._MvmntDtls

	@MvmntDtls.setter
	def MvmntDtls(self, value):
		self._MvmntDtls = value if type(value) != base_types.auto else self.make_default("MvmntDtls")

	@MvmntDtls.deleter
	def MvmntDtls(self):
		del self._MvmntDtls
		self._MvmntDtls = None

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
	def AgtCAMvmntInstrId(self):
		return self._AgtCAMvmntInstrId

	@AgtCAMvmntInstrId.setter
	def AgtCAMvmntInstrId(self, value):
		self._AgtCAMvmntInstrId = value if type(value) != base_types.auto else self.make_default("AgtCAMvmntInstrId")

	@AgtCAMvmntInstrId.deleter
	def AgtCAMvmntInstrId(self):
		del self._AgtCAMvmntInstrId
		self._AgtCAMvmntInstrId = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='MvmntDtls', type=MovementInstruction1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Id', type=DocumentIdentification8, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CorpActnGnlInf', type=CorporateActionInformation1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AgtCAMvmntInstrId', type=DocumentIdentification8, min=1, max=1, mutex_group=None, array=False),
	))

