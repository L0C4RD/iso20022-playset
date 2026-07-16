# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Amendment7
from . import PartyAndSignature2

class UndertakingAmendmentResponseV01(base_types._BaseFieldType):

	__slots__ = ["_DgtlSgntr", "_UdrtkgAmdmntRspnDtls"]
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
	def UdrtkgAmdmntRspnDtls(self):
		return self._UdrtkgAmdmntRspnDtls

	@UdrtkgAmdmntRspnDtls.setter
	def UdrtkgAmdmntRspnDtls(self, value):
		self._UdrtkgAmdmntRspnDtls = value if value is not None else base_types.UninitialisedField(self, 'UdrtkgAmdmntRspnDtls', Amendment7, False)

	@UdrtkgAmdmntRspnDtls.deleter
	def UdrtkgAmdmntRspnDtls(self):
		del self._UdrtkgAmdmntRspnDtls
		self._UdrtkgAmdmntRspnDtls = base_types.UninitialisedField(self, 'UdrtkgAmdmntRspnDtls', Amendment7, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='DgtlSgntr', type=PartyAndSignature2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UdrtkgAmdmntRspnDtls', type=Amendment7, min=1, max=1, mutex_group=None, array=False),
	))