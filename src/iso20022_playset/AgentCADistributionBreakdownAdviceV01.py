from . import base_types
import CorporateActionInformation1
import DocumentIdentification8
import EntitlementAdvice1

class AgentCADistributionBreakdownAdviceV01(base_types._BaseFieldType):

	__slots__ = ["_CorpActnGnlInf", "_CorpActnDstrbtnDtls", "_Id"]
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
	def CorpActnDstrbtnDtls(self):
		return self._CorpActnDstrbtnDtls

	@CorpActnDstrbtnDtls.setter
	def CorpActnDstrbtnDtls(self, value):
		self._CorpActnDstrbtnDtls = value if type(value) != auto else self.make_default("CorpActnDstrbtnDtls")

	@CorpActnDstrbtnDtls.deleter
	def CorpActnDstrbtnDtls(self):
		del self._CorpActnDstrbtnDtls
		self._CorpActnDstrbtnDtls = None

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

	_field_defs = frozenset((
		base_types.FieldEntry(name='CorpActnGnlInf', type=CorporateActionInformation1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CorpActnDstrbtnDtls', type=EntitlementAdvice1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Id', type=DocumentIdentification8, min=1, max=1, mutex_group=None, array=False),
	))

