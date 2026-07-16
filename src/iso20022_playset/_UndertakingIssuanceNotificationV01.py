# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import PartyAndSignature2
from . import UndertakingAdvice2

class UndertakingIssuanceNotificationV01(base_types._BaseFieldType):

	__slots__ = ["_DgtlSgntr", "_UdrtkgIssncNtfctnDtls"]
	@property
	def DgtlSgntr(self):
		return self._DgtlSgntr

	@DgtlSgntr.setter
	def DgtlSgntr(self, value):
		self._DgtlSgntr = value if value is not None else base_types.UninitialisedField(self, 'DgtlSgntr', PartyAndSignature2, False)

	@DgtlSgntr.deleter
	def DgtlSgntr(self):
		del self._DgtlSgntr
		self._DgtlSgntr = base_types.UninitialisedField(self, 'DgtlSgntr', PartyAndSignature2, False)

	@property
	def UdrtkgIssncNtfctnDtls(self):
		return self._UdrtkgIssncNtfctnDtls

	@UdrtkgIssncNtfctnDtls.setter
	def UdrtkgIssncNtfctnDtls(self, value):
		self._UdrtkgIssncNtfctnDtls = value if value is not None else base_types.UninitialisedField(self, 'UdrtkgIssncNtfctnDtls', UndertakingAdvice2, False)

	@UdrtkgIssncNtfctnDtls.deleter
	def UdrtkgIssncNtfctnDtls(self):
		del self._UdrtkgIssncNtfctnDtls
		self._UdrtkgIssncNtfctnDtls = base_types.UninitialisedField(self, 'UdrtkgIssncNtfctnDtls', UndertakingAdvice2, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='DgtlSgntr', type=PartyAndSignature2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UdrtkgIssncNtfctnDtls', type=UndertakingAdvice2, min=1, max=1, mutex_group=None, array=False),
	))