# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Amendment3
from . import Max2000Text
from . import PartyAndSignature2

class UndertakingAmendmentRequestV01(base_types._BaseFieldType):

	__slots__ = ["_DgtlSgntr", "_InstrsToBk", "_UdrtkgAmdmntReqDtls"]
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
	def InstrsToBk(self):
		return self._InstrsToBk

	@InstrsToBk.setter
	def InstrsToBk(self, value):
		self._InstrsToBk = value if value is not None else base_types.UninitialisedField(self, 'InstrsToBk', Max2000Text, True)

	@InstrsToBk.deleter
	def InstrsToBk(self):
		del self._InstrsToBk
		self._InstrsToBk = base_types.UninitialisedField(self, 'InstrsToBk', Max2000Text, True)

	@property
	def UdrtkgAmdmntReqDtls(self):
		return self._UdrtkgAmdmntReqDtls

	@UdrtkgAmdmntReqDtls.setter
	def UdrtkgAmdmntReqDtls(self, value):
		self._UdrtkgAmdmntReqDtls = value if value is not None else base_types.UninitialisedField(self, 'UdrtkgAmdmntReqDtls', Amendment3, False)

	@UdrtkgAmdmntReqDtls.deleter
	def UdrtkgAmdmntReqDtls(self):
		del self._UdrtkgAmdmntReqDtls
		self._UdrtkgAmdmntReqDtls = base_types.UninitialisedField(self, 'UdrtkgAmdmntReqDtls', Amendment3, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='DgtlSgntr', type=PartyAndSignature2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InstrsToBk', type=Max2000Text, min=0, max=5, mutex_group=None, array=True),
		base_types.FieldEntry(name='UdrtkgAmdmntReqDtls', type=Amendment3, min=1, max=1, mutex_group=None, array=False),
	))