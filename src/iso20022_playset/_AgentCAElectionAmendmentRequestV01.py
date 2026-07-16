# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ContactPerson1
from . import CorporateActionElection1
from . import CorporateActionElection2
from . import CorporateActionInformation1
from . import DocumentIdentification8
from . import SecuritiesAccount7

class AgentCAElectionAmendmentRequestV01(base_types._BaseFieldType):

	__slots__ = ["_AcctDtls", "_AgtCAElctnAdvcId", "_AmddElctnDtls", "_CorpActnGnlInf", "_CtctDtls", "_Id", "_OrgnlElctnDtls"]
	@property
	def AcctDtls(self):
		return self._AcctDtls

	@AcctDtls.setter
	def AcctDtls(self, value):
		self._AcctDtls = value if value is not None else base_types.UninitialisedField(self, 'AcctDtls', SecuritiesAccount7, False)

	@AcctDtls.deleter
	def AcctDtls(self):
		del self._AcctDtls
		self._AcctDtls = base_types.UninitialisedField(self, 'AcctDtls', SecuritiesAccount7, False)

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
	def AmddElctnDtls(self):
		return self._AmddElctnDtls

	@AmddElctnDtls.setter
	def AmddElctnDtls(self, value):
		self._AmddElctnDtls = value if value is not None else base_types.UninitialisedField(self, 'AmddElctnDtls', CorporateActionElection2, False)

	@AmddElctnDtls.deleter
	def AmddElctnDtls(self):
		del self._AmddElctnDtls
		self._AmddElctnDtls = base_types.UninitialisedField(self, 'AmddElctnDtls', CorporateActionElection2, False)

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
	def OrgnlElctnDtls(self):
		return self._OrgnlElctnDtls

	@OrgnlElctnDtls.setter
	def OrgnlElctnDtls(self, value):
		self._OrgnlElctnDtls = value if value is not None else base_types.UninitialisedField(self, 'OrgnlElctnDtls', CorporateActionElection1, False)

	@OrgnlElctnDtls.deleter
	def OrgnlElctnDtls(self):
		del self._OrgnlElctnDtls
		self._OrgnlElctnDtls = base_types.UninitialisedField(self, 'OrgnlElctnDtls', CorporateActionElection1, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AcctDtls', type=SecuritiesAccount7, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AgtCAElctnAdvcId', type=DocumentIdentification8, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AmddElctnDtls', type=CorporateActionElection2, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CorpActnGnlInf', type=CorporateActionInformation1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CtctDtls', type=ContactPerson1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Id', type=DocumentIdentification8, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlElctnDtls', type=CorporateActionElection1, min=1, max=1, mutex_group=None, array=False),
	))