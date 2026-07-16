# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CorporateActionInformation2
from . import CorporateActionNotificationAdvice1
from . import DocumentIdentification8
from . import NotificationCancellation1

class AgentCANotificationCancellationRequestV01(base_types._BaseFieldType):

	__slots__ = ["_CorpActnGnlInf", "_CorpActnNtfctnDtls", "_Id", "_NtfctnCxlTpAndLkg"]
	@property
	def CorpActnGnlInf(self):
		return self._CorpActnGnlInf

	@CorpActnGnlInf.setter
	def CorpActnGnlInf(self, value):
		self._CorpActnGnlInf = value if value is not None else base_types.UninitialisedField(self, 'CorpActnGnlInf', CorporateActionInformation2, False)

	@CorpActnGnlInf.deleter
	def CorpActnGnlInf(self):
		del self._CorpActnGnlInf
		self._CorpActnGnlInf = base_types.UninitialisedField(self, 'CorpActnGnlInf', CorporateActionInformation2, False)

	@property
	def CorpActnNtfctnDtls(self):
		return self._CorpActnNtfctnDtls

	@CorpActnNtfctnDtls.setter
	def CorpActnNtfctnDtls(self, value):
		self._CorpActnNtfctnDtls = value if value is not None else base_types.UninitialisedField(self, 'CorpActnNtfctnDtls', CorporateActionNotificationAdvice1, False)

	@CorpActnNtfctnDtls.deleter
	def CorpActnNtfctnDtls(self):
		del self._CorpActnNtfctnDtls
		self._CorpActnNtfctnDtls = base_types.UninitialisedField(self, 'CorpActnNtfctnDtls', CorporateActionNotificationAdvice1, False)

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
	def NtfctnCxlTpAndLkg(self):
		return self._NtfctnCxlTpAndLkg

	@NtfctnCxlTpAndLkg.setter
	def NtfctnCxlTpAndLkg(self, value):
		self._NtfctnCxlTpAndLkg = value if value is not None else base_types.UninitialisedField(self, 'NtfctnCxlTpAndLkg', NotificationCancellation1, False)

	@NtfctnCxlTpAndLkg.deleter
	def NtfctnCxlTpAndLkg(self):
		del self._NtfctnCxlTpAndLkg
		self._NtfctnCxlTpAndLkg = base_types.UninitialisedField(self, 'NtfctnCxlTpAndLkg', NotificationCancellation1, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='CorpActnGnlInf', type=CorporateActionInformation2, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CorpActnNtfctnDtls', type=CorporateActionNotificationAdvice1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Id', type=DocumentIdentification8, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NtfctnCxlTpAndLkg', type=NotificationCancellation1, min=1, max=1, mutex_group=None, array=False),
	))