# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CorporateActionInformation1
from . import DocumentIdentification8
from . import EntitlementAdvice1

class AgentCADistributionBreakdownAdviceV01(base_types._BaseFieldType):

	__slots__ = ["_CorpActnDstrbtnDtls", "_CorpActnGnlInf", "_Id"]
	@property
	def CorpActnDstrbtnDtls(self):
		return self._CorpActnDstrbtnDtls

	@CorpActnDstrbtnDtls.setter
	def CorpActnDstrbtnDtls(self, value):
		self._CorpActnDstrbtnDtls = value if value is not None else base_types.UninitialisedField(self, 'CorpActnDstrbtnDtls', EntitlementAdvice1, False)

	@CorpActnDstrbtnDtls.deleter
	def CorpActnDstrbtnDtls(self):
		del self._CorpActnDstrbtnDtls
		self._CorpActnDstrbtnDtls = base_types.UninitialisedField(self, 'CorpActnDstrbtnDtls', EntitlementAdvice1, False)

	@property
	def CorpActnGnlInf(self):
		return self._CorpActnGnlInf

	@CorpActnGnlInf.setter
	def CorpActnGnlInf(self, value):
		self._CorpActnGnlInf = value if value is not None else base_types.UninitialisedField(self, 'CorpActnGnlInf', CorporateActionInformation1, False)

	@CorpActnGnlInf.deleter
	def CorpActnGnlInf(self):
		del self._CorpActnGnlInf
		self._CorpActnGnlInf = base_types.UninitialisedField(self, 'CorpActnGnlInf', CorporateActionInformation1, False)

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

	_field_defs = frozenset((
		base_types.FieldEntry(name='CorpActnDstrbtnDtls', type=EntitlementAdvice1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CorpActnGnlInf', type=CorporateActionInformation1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Id', type=DocumentIdentification8, min=1, max=1, mutex_group=None, array=False),
	))