from . import base_types
from .PartyAndSignature2 import PartyAndSignature2
from .Amendment7 import Amendment7

class UndertakingAmendmentResponseMessage1(base_types._BaseFieldType):

	__slots__ = ["_UdrtkgAmdmntRspnDtls", "_DgtlSgntr"]
	@property
	def UdrtkgAmdmntRspnDtls(self):
		return self._UdrtkgAmdmntRspnDtls

	@UdrtkgAmdmntRspnDtls.setter
	def UdrtkgAmdmntRspnDtls(self, value):
		self._UdrtkgAmdmntRspnDtls = value if type(value) != base_types.auto else self.make_default("UdrtkgAmdmntRspnDtls")

	@UdrtkgAmdmntRspnDtls.deleter
	def UdrtkgAmdmntRspnDtls(self):
		del self._UdrtkgAmdmntRspnDtls
		self._UdrtkgAmdmntRspnDtls = None

	@property
	def DgtlSgntr(self):
		return self._DgtlSgntr

	@DgtlSgntr.setter
	def DgtlSgntr(self, value):
		self._DgtlSgntr = value if type(value) != base_types.auto else self.make_default("DgtlSgntr")

	@DgtlSgntr.deleter
	def DgtlSgntr(self):
		del self._DgtlSgntr
		self._DgtlSgntr = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='UdrtkgAmdmntRspnDtls', type=Amendment7, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DgtlSgntr', type=PartyAndSignature2, min=0, max=1, mutex_group=None, array=False),
	))

