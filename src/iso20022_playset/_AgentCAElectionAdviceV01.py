# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ContactPerson1
from . import CorporateActionAdditionalInformation1
from . import CorporateActionElection3
from . import CorporateActionInformation1
from . import DocumentIdentification8
from . import ElectionAdviceFunction1

class AgentCAElectionAdviceV01(base_types._BaseFieldType):

	__slots__ = ["_AddtlInf", "_CorpActnGnlInf", "_CtctDtls", "_ElctnAdvcTpAndLkg", "_ElctnDtls", "_Id"]
	@property
	def AddtlInf(self):
		return self._AddtlInf

	@AddtlInf.setter
	def AddtlInf(self, value):
		self._AddtlInf = value if value is not None else base_types.UninitialisedField(self, 'AddtlInf', CorporateActionAdditionalInformation1, False)

	@AddtlInf.deleter
	def AddtlInf(self):
		del self._AddtlInf
		self._AddtlInf = base_types.UninitialisedField(self, 'AddtlInf', CorporateActionAdditionalInformation1, False)

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
	def CtctDtls(self):
		return self._CtctDtls

	@CtctDtls.setter
	def CtctDtls(self, value):
		self._CtctDtls = value if value is not None else base_types.UninitialisedField(self, 'CtctDtls', ContactPerson1, False)

	@CtctDtls.deleter
	def CtctDtls(self):
		del self._CtctDtls
		self._CtctDtls = base_types.UninitialisedField(self, 'CtctDtls', ContactPerson1, False)

	@property
	def ElctnAdvcTpAndLkg(self):
		return self._ElctnAdvcTpAndLkg

	@ElctnAdvcTpAndLkg.setter
	def ElctnAdvcTpAndLkg(self, value):
		self._ElctnAdvcTpAndLkg = value if value is not None else base_types.UninitialisedField(self, 'ElctnAdvcTpAndLkg', ElectionAdviceFunction1, False)

	@ElctnAdvcTpAndLkg.deleter
	def ElctnAdvcTpAndLkg(self):
		del self._ElctnAdvcTpAndLkg
		self._ElctnAdvcTpAndLkg = base_types.UninitialisedField(self, 'ElctnAdvcTpAndLkg', ElectionAdviceFunction1, False)

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
		base_types.FieldEntry(name='AddtlInf', type=CorporateActionAdditionalInformation1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CorpActnGnlInf', type=CorporateActionInformation1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CtctDtls', type=ContactPerson1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ElctnAdvcTpAndLkg', type=ElectionAdviceFunction1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ElctnDtls', type=CorporateActionElection3, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Id', type=DocumentIdentification8, min=1, max=1, mutex_group=None, array=False),
	))