# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CorporateActionAdditionalInformation1
from . import CorporateActionInformationStatus1Choice
from . import DocumentIdentification8

class AgentCAInformationStatusAdviceV01(base_types._BaseFieldType):

	__slots__ = ["_AgtCAInfAdvcId", "_CorpActnAddtlInf", "_Id", "_InfStsDtls"]
	@property
	def AgtCAInfAdvcId(self):
		return self._AgtCAInfAdvcId

	@AgtCAInfAdvcId.setter
	def AgtCAInfAdvcId(self, value):
		self._AgtCAInfAdvcId = value if value is not None else base_types.UninitialisedField(self, 'AgtCAInfAdvcId', DocumentIdentification8, False)

	@AgtCAInfAdvcId.deleter
	def AgtCAInfAdvcId(self):
		del self._AgtCAInfAdvcId
		self._AgtCAInfAdvcId = base_types.UninitialisedField(self, 'AgtCAInfAdvcId', DocumentIdentification8, False)

	@property
	def CorpActnAddtlInf(self):
		return self._CorpActnAddtlInf

	@CorpActnAddtlInf.setter
	def CorpActnAddtlInf(self, value):
		self._CorpActnAddtlInf = value if value is not None else base_types.UninitialisedField(self, 'CorpActnAddtlInf', CorporateActionAdditionalInformation1, False)

	@CorpActnAddtlInf.deleter
	def CorpActnAddtlInf(self):
		del self._CorpActnAddtlInf
		self._CorpActnAddtlInf = base_types.UninitialisedField(self, 'CorpActnAddtlInf', CorporateActionAdditionalInformation1, False)

	@property
	def Id(self):
		return self._Id

	@Id.setter
	def Id(self, value):
		self._Id = value if value is not None else base_types.UninitialisedField(self, 'Id', DocumentIdentification8, False)

	@Id.deleter
	def Id(self):
		del self._Id
		self._Id = base_types.UninitialisedField(self, 'Id', DocumentIdentification8, False)

	@property
	def InfStsDtls(self):
		return self._InfStsDtls

	@InfStsDtls.setter
	def InfStsDtls(self, value):
		self._InfStsDtls = value if value is not None else base_types.UninitialisedField(self, 'InfStsDtls', CorporateActionInformationStatus1Choice, False)

	@InfStsDtls.deleter
	def InfStsDtls(self):
		del self._InfStsDtls
		self._InfStsDtls = base_types.UninitialisedField(self, 'InfStsDtls', CorporateActionInformationStatus1Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AgtCAInfAdvcId', type=DocumentIdentification8, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CorpActnAddtlInf', type=CorporateActionAdditionalInformation1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Id', type=DocumentIdentification8, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InfStsDtls', type=CorporateActionInformationStatus1Choice, min=1, max=1, mutex_group=None, array=False),
	))