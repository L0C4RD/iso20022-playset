# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Amendment6
from . import PartyAndSignature2

class UndertakingAmendmentNotificationV01(base_types._BaseFieldType):

	__slots__ = ["_DgtlSgntr", "_UdrtkgAmdmntNtfctnDtls"]
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
	def UdrtkgAmdmntNtfctnDtls(self):
		return self._UdrtkgAmdmntNtfctnDtls

	@UdrtkgAmdmntNtfctnDtls.setter
	def UdrtkgAmdmntNtfctnDtls(self, value):
		self._UdrtkgAmdmntNtfctnDtls = value if value is not None else base_types.UninitialisedField(self, 'UdrtkgAmdmntNtfctnDtls', Amendment6, False)

	@UdrtkgAmdmntNtfctnDtls.deleter
	def UdrtkgAmdmntNtfctnDtls(self):
		del self._UdrtkgAmdmntNtfctnDtls
		self._UdrtkgAmdmntNtfctnDtls = base_types.UninitialisedField(self, 'UdrtkgAmdmntNtfctnDtls', Amendment6, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='DgtlSgntr', type=PartyAndSignature2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UdrtkgAmdmntNtfctnDtls', type=Amendment6, min=1, max=1, mutex_group=None, array=False),
	))