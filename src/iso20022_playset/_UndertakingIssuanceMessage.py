# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import PartyAndSignature2
from . import Undertaking3

class UndertakingIssuanceMessage(base_types._BaseFieldType):

	__slots__ = ["_DgtlSgntr", "_UdrtkgDtls"]
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
	def UdrtkgDtls(self):
		return self._UdrtkgDtls

	@UdrtkgDtls.setter
	def UdrtkgDtls(self, value):
		self._UdrtkgDtls = value if value is not None else base_types.UninitialisedField(self, 'UdrtkgDtls', Undertaking3, False)

	@UdrtkgDtls.deleter
	def UdrtkgDtls(self):
		del self._UdrtkgDtls
		self._UdrtkgDtls = base_types.UninitialisedField(self, 'UdrtkgDtls', Undertaking3, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='DgtlSgntr', type=PartyAndSignature2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UdrtkgDtls', type=Undertaking3, min=1, max=1, mutex_group=None, array=False),
	))