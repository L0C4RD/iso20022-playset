from . import base_types
from ._DocumentIdentification8 import DocumentIdentification8
from ._CorporateActionInformation1 import CorporateActionInformation1
from ._CorporateActionElection1 import CorporateActionElection1
from ._SecuritiesAccount7 import SecuritiesAccount7
from ._ContactPerson1 import ContactPerson1
from ._CorporateActionElection2 import CorporateActionElection2

class AgentCAElectionAmendmentRequestV01(base_types._BaseFieldType):

	__slots__ = ["_OrgnlElctnDtls", "_AmddElctnDtls", "_CtctDtls", "_AcctDtls", "_Id", "_AgtCAElctnAdvcId", "_CorpActnGnlInf"]
	@property
	def OrgnlElctnDtls(self):
		return self._OrgnlElctnDtls

	@OrgnlElctnDtls.setter
	def OrgnlElctnDtls(self, value):
		self._OrgnlElctnDtls = value if type(value) != base_types.auto else self.make_default("OrgnlElctnDtls")

	@OrgnlElctnDtls.deleter
	def OrgnlElctnDtls(self):
		del self._OrgnlElctnDtls
		self._OrgnlElctnDtls = None

	@property
	def AmddElctnDtls(self):
		return self._AmddElctnDtls

	@AmddElctnDtls.setter
	def AmddElctnDtls(self, value):
		self._AmddElctnDtls = value if type(value) != base_types.auto else self.make_default("AmddElctnDtls")

	@AmddElctnDtls.deleter
	def AmddElctnDtls(self):
		del self._AmddElctnDtls
		self._AmddElctnDtls = None

	@property
	def CtctDtls(self):
		return self._CtctDtls

	@CtctDtls.setter
	def CtctDtls(self, value):
		self._CtctDtls = value if type(value) != base_types.auto else self.make_default("CtctDtls")

	@CtctDtls.deleter
	def CtctDtls(self):
		del self._CtctDtls
		self._CtctDtls = None

	@property
	def AcctDtls(self):
		return self._AcctDtls

	@AcctDtls.setter
	def AcctDtls(self, value):
		self._AcctDtls = value if type(value) != base_types.auto else self.make_default("AcctDtls")

	@AcctDtls.deleter
	def AcctDtls(self):
		del self._AcctDtls
		self._AcctDtls = None

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

	_field_defs = frozenset((
		base_types.FieldEntry(name='OrgnlElctnDtls', type=CorporateActionElection1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AmddElctnDtls', type=CorporateActionElection2, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CtctDtls', type=ContactPerson1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AcctDtls', type=SecuritiesAccount7, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Id', type=DocumentIdentification8, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AgtCAElctnAdvcId', type=DocumentIdentification8, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CorpActnGnlInf', type=CorporateActionInformation1, min=1, max=1, mutex_group=None, array=False),
	))

