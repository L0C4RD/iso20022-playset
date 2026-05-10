from . import base_types
from .PartyAndSignature2 import PartyAndSignature2
from .Max2000Text import Max2000Text
from .Amendment3 import Amendment3

class UndertakingAmendmentRequestV01(base_types._BaseFieldType):

	__slots__ = ["_DgtlSgntr", "_UdrtkgAmdmntReqDtls", "_InstrsToBk"]
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

	@property
	def UdrtkgAmdmntReqDtls(self):
		return self._UdrtkgAmdmntReqDtls

	@UdrtkgAmdmntReqDtls.setter
	def UdrtkgAmdmntReqDtls(self, value):
		self._UdrtkgAmdmntReqDtls = value if type(value) != base_types.auto else self.make_default("UdrtkgAmdmntReqDtls")

	@UdrtkgAmdmntReqDtls.deleter
	def UdrtkgAmdmntReqDtls(self):
		del self._UdrtkgAmdmntReqDtls
		self._UdrtkgAmdmntReqDtls = None

	@property
	def InstrsToBk(self):
		return self._InstrsToBk

	@InstrsToBk.setter
	def InstrsToBk(self, value):
		self._InstrsToBk = value if type(value) != base_types.auto else self.make_default("InstrsToBk")

	@InstrsToBk.deleter
	def InstrsToBk(self):
		del self._InstrsToBk
		self._InstrsToBk = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='DgtlSgntr', type=PartyAndSignature2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UdrtkgAmdmntReqDtls', type=Amendment3, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InstrsToBk', type=Max2000Text, min=0, max=5, mutex_group=None, array=True),
	))

