# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import PartyAndSignature2
from . import UndertakingNonExtensionStatusAdvice1

class UndertakingNonExtensionNotificationV01(base_types._BaseFieldType):

	__slots__ = ["_DgtlSgntr", "_UdrtkgNonXtnsnNtfctnDtls"]
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
	def UdrtkgNonXtnsnNtfctnDtls(self):
		return self._UdrtkgNonXtnsnNtfctnDtls

	@UdrtkgNonXtnsnNtfctnDtls.setter
	def UdrtkgNonXtnsnNtfctnDtls(self, value):
		self._UdrtkgNonXtnsnNtfctnDtls = value if value is not None else base_types.UninitialisedField(self, 'UdrtkgNonXtnsnNtfctnDtls', UndertakingNonExtensionStatusAdvice1, False)

	@UdrtkgNonXtnsnNtfctnDtls.deleter
	def UdrtkgNonXtnsnNtfctnDtls(self):
		del self._UdrtkgNonXtnsnNtfctnDtls
		self._UdrtkgNonXtnsnNtfctnDtls = base_types.UninitialisedField(self, 'UdrtkgNonXtnsnNtfctnDtls', UndertakingNonExtensionStatusAdvice1, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='DgtlSgntr', type=PartyAndSignature2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UdrtkgNonXtnsnNtfctnDtls', type=UndertakingNonExtensionStatusAdvice1, min=1, max=1, mutex_group=None, array=False),
	))