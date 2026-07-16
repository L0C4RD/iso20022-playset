# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Amendment1
from . import PartyAndSignature2

class UndertakingAmendmentMessage1(base_types._BaseFieldType):

	__slots__ = ["_DgtlSgntr", "_UdrtkgAmdmntDtls"]
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
	def UdrtkgAmdmntDtls(self):
		return self._UdrtkgAmdmntDtls

	@UdrtkgAmdmntDtls.setter
	def UdrtkgAmdmntDtls(self, value):
		self._UdrtkgAmdmntDtls = value if value is not None else base_types.UninitialisedField(self, 'UdrtkgAmdmntDtls', Amendment1, False)

	@UdrtkgAmdmntDtls.deleter
	def UdrtkgAmdmntDtls(self):
		del self._UdrtkgAmdmntDtls
		self._UdrtkgAmdmntDtls = base_types.UninitialisedField(self, 'UdrtkgAmdmntDtls', Amendment1, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='DgtlSgntr', type=PartyAndSignature2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UdrtkgAmdmntDtls', type=Amendment1, min=1, max=1, mutex_group=None, array=False),
	))