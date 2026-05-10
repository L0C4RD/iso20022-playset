from . import base_types
from ._CorporateActionElection3 import CorporateActionElection3
from ._DocumentIdentification8 import DocumentIdentification8
from ._CorporateActionInformation1 import CorporateActionInformation1

class AgentCAElectionCancellationRequestV01(base_types._BaseFieldType):

	__slots__ = ["_ElctnDtls", "_Id", "_AgtCAElctnAdvcId", "_CorpActnGnlInf"]
	@property
	def AgtCAElctnAdvcId(self):
		return self._AgtCAElctnAdvcId

	@AgtCAElctnAdvcId.setter
	def AgtCAElctnAdvcId(self, value):
		self._AgtCAElctnAdvcId = value if type(value) != base_types.auto else self.make_default("AgtCAElctnAdvcId")

	@AgtCAElctnAdvcId.deleter
	def AgtCAElctnAdvcId(self):
		del self._AgtCAElctnAdvcId
		self._AgtCAElctnAdvcId = None

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
	def ElctnDtls(self):
		return self._ElctnDtls

	@ElctnDtls.setter
	def ElctnDtls(self, value):
		self._ElctnDtls = value if type(value) != base_types.auto else self.make_default("ElctnDtls")

	@ElctnDtls.deleter
	def ElctnDtls(self):
		del self._ElctnDtls
		self._ElctnDtls = None

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

	_field_defs = frozenset((
		base_types.FieldEntry(name='AgtCAElctnAdvcId', type=DocumentIdentification8, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CorpActnGnlInf', type=CorporateActionInformation1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ElctnDtls', type=CorporateActionElection3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Id', type=DocumentIdentification8, min=1, max=1, mutex_group=None, array=False),
	))

