# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import PartyAndSignature2
from . import UndertakingTerminationNotice1

class UndertakingTerminationNotificationV01(base_types._BaseFieldType):

	__slots__ = ["_DgtlSgntr", "_UdrtkgTermntnNtfctnDtls"]
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
	def UdrtkgTermntnNtfctnDtls(self):
		return self._UdrtkgTermntnNtfctnDtls

	@UdrtkgTermntnNtfctnDtls.setter
	def UdrtkgTermntnNtfctnDtls(self, value):
		self._UdrtkgTermntnNtfctnDtls = value if value is not None else base_types.UninitialisedField(self, 'UdrtkgTermntnNtfctnDtls', UndertakingTerminationNotice1, False)

	@UdrtkgTermntnNtfctnDtls.deleter
	def UdrtkgTermntnNtfctnDtls(self):
		del self._UdrtkgTermntnNtfctnDtls
		self._UdrtkgTermntnNtfctnDtls = base_types.UninitialisedField(self, 'UdrtkgTermntnNtfctnDtls', UndertakingTerminationNotice1, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='DgtlSgntr', type=PartyAndSignature2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UdrtkgTermntnNtfctnDtls', type=UndertakingTerminationNotice1, min=1, max=1, mutex_group=None, array=False),
	))