import base_types
import ContactPerson1
import ElectionAdviceFunction1
import CorporateActionInformation1
import DocumentIdentification8
import CorporateActionAdditionalInformation1
import CorporateActionElection3

class AgentCAElectionAdviceV01(base_types._BaseFieldType):

	__slots__ = ["_ElctnDtls", "_AddtlInf", "_Id", "_CorpActnGnlInf", "_ElctnAdvcTpAndLkg", "_CtctDtls"]
	@property
	def ElctnDtls(self):
		return self._ElctnDtls

	@ElctnDtls.setter
	def ElctnDtls(self, value):
		self._ElctnDtls = value if type(value) != auto else self.make_default("ElctnDtls")

	@ElctnDtls.deleter
	def ElctnDtls(self):
		del self._ElctnDtls
		self._ElctnDtls = None

	@property
	def AddtlInf(self):
		return self._AddtlInf

	@AddtlInf.setter
	def AddtlInf(self, value):
		self._AddtlInf = value if type(value) != auto else self.make_default("AddtlInf")

	@AddtlInf.deleter
	def AddtlInf(self):
		del self._AddtlInf
		self._AddtlInf = None

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
	def CorpActnGnlInf(self):
		return self._CorpActnGnlInf

	@CorpActnGnlInf.setter
	def CorpActnGnlInf(self, value):
		self._CorpActnGnlInf = value if type(value) != auto else self.make_default("CorpActnGnlInf")

	@CorpActnGnlInf.deleter
	def CorpActnGnlInf(self):
		del self._CorpActnGnlInf
		self._CorpActnGnlInf = None

	@property
	def ElctnAdvcTpAndLkg(self):
		return self._ElctnAdvcTpAndLkg

	@ElctnAdvcTpAndLkg.setter
	def ElctnAdvcTpAndLkg(self, value):
		self._ElctnAdvcTpAndLkg = value if type(value) != auto else self.make_default("ElctnAdvcTpAndLkg")

	@ElctnAdvcTpAndLkg.deleter
	def ElctnAdvcTpAndLkg(self):
		del self._ElctnAdvcTpAndLkg
		self._ElctnAdvcTpAndLkg = None

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

	_field_defs = frozenset((
		base_types.FieldEntry(name='ElctnDtls', type=CorporateActionElection3, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AddtlInf', type=CorporateActionAdditionalInformation1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Id', type=DocumentIdentification8, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CorpActnGnlInf', type=CorporateActionInformation1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ElctnAdvcTpAndLkg', type=ElectionAdviceFunction1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CtctDtls', type=ContactPerson1, min=0, max=1, mutex_group=None, array=False),
	))

