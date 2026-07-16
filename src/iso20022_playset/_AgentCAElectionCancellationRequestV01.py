# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CorporateActionElection3
from . import CorporateActionInformation1
from . import DocumentIdentification8

class AgentCAElectionCancellationRequestV01(base_types._BaseFieldType):

	__slots__ = ["_AgtCAElctnAdvcId", "_CorpActnGnlInf", "_ElctnDtls", "_Id"]
	@property
	def AgtCAElctnAdvcId(self):
		return self._AgtCAElctnAdvcId

	@AgtCAElctnAdvcId.setter
	def AgtCAElctnAdvcId(self, value):
		self._AgtCAElctnAdvcId = value if value is not None else base_types.UninitialisedField(self, 'AgtCAElctnAdvcId', DocumentIdentification8, False)

	@AgtCAElctnAdvcId.deleter
	def AgtCAElctnAdvcId(self):
		del self._AgtCAElctnAdvcId
		self._AgtCAElctnAdvcId = base_types.UninitialisedField(self, 'AgtCAElctnAdvcId', DocumentIdentification8, False)

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
	def ElctnDtls(self):
		return self._ElctnDtls

	@ElctnDtls.setter
	def ElctnDtls(self, value):
		self._ElctnDtls = value if value is not None else base_types.UninitialisedField(self, 'ElctnDtls', CorporateActionElection3, False)

	@ElctnDtls.deleter
	def ElctnDtls(self):
		del self._ElctnDtls
		self._ElctnDtls = base_types.UninitialisedField(self, 'ElctnDtls', CorporateActionElection3, False)

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
		base_types.FieldEntry(name='AgtCAElctnAdvcId', type=DocumentIdentification8, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CorpActnGnlInf', type=CorporateActionInformation1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ElctnDtls', type=CorporateActionElection3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Id', type=DocumentIdentification8, min=1, max=1, mutex_group=None, array=False),
	))