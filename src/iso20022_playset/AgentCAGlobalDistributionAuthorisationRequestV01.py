from . import base_types
from .GlobalDistributionRequest1 import GlobalDistributionRequest1
from .CorporateActionInformation1 import CorporateActionInformation1
from .DocumentIdentification8 import DocumentIdentification8

class AgentCAGlobalDistributionAuthorisationRequestV01(base_types._BaseFieldType):

	__slots__ = ["_GblDstrbtnDtls", "_Id", "_CorpActnGnlInf"]
	@property
	def GblDstrbtnDtls(self):
		return self._GblDstrbtnDtls

	@GblDstrbtnDtls.setter
	def GblDstrbtnDtls(self, value):
		self._GblDstrbtnDtls = value if type(value) != auto else self.make_default("GblDstrbtnDtls")

	@GblDstrbtnDtls.deleter
	def GblDstrbtnDtls(self):
		del self._GblDstrbtnDtls
		self._GblDstrbtnDtls = None

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

	_field_defs = frozenset((
		base_types.FieldEntry(name='GblDstrbtnDtls', type=GlobalDistributionRequest1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Id', type=DocumentIdentification8, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CorpActnGnlInf', type=CorporateActionInformation1, min=1, max=1, mutex_group=None, array=False),
	))

