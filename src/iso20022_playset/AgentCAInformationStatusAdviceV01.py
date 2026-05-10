from . import base_types
from .CorporateActionAdditionalInformation1 import CorporateActionAdditionalInformation1
from .CorporateActionInformationStatus1Choice import CorporateActionInformationStatus1Choice
from .DocumentIdentification8 import DocumentIdentification8

class AgentCAInformationStatusAdviceV01(base_types._BaseFieldType):

	__slots__ = ["_Id", "_CorpActnAddtlInf", "_InfStsDtls", "_AgtCAInfAdvcId"]
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
	def CorpActnAddtlInf(self):
		return self._CorpActnAddtlInf

	@CorpActnAddtlInf.setter
	def CorpActnAddtlInf(self, value):
		self._CorpActnAddtlInf = value if type(value) != auto else self.make_default("CorpActnAddtlInf")

	@CorpActnAddtlInf.deleter
	def CorpActnAddtlInf(self):
		del self._CorpActnAddtlInf
		self._CorpActnAddtlInf = None

	@property
	def InfStsDtls(self):
		return self._InfStsDtls

	@InfStsDtls.setter
	def InfStsDtls(self, value):
		self._InfStsDtls = value if type(value) != auto else self.make_default("InfStsDtls")

	@InfStsDtls.deleter
	def InfStsDtls(self):
		del self._InfStsDtls
		self._InfStsDtls = None

	@property
	def AgtCAInfAdvcId(self):
		return self._AgtCAInfAdvcId

	@AgtCAInfAdvcId.setter
	def AgtCAInfAdvcId(self, value):
		self._AgtCAInfAdvcId = value if type(value) != auto else self.make_default("AgtCAInfAdvcId")

	@AgtCAInfAdvcId.deleter
	def AgtCAInfAdvcId(self):
		del self._AgtCAInfAdvcId
		self._AgtCAInfAdvcId = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Id', type=DocumentIdentification8, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CorpActnAddtlInf', type=CorporateActionAdditionalInformation1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InfStsDtls', type=CorporateActionInformationStatus1Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AgtCAInfAdvcId', type=DocumentIdentification8, min=1, max=1, mutex_group=None, array=False),
	))

