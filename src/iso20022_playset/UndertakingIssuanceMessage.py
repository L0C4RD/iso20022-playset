from . import base_types
from .PartyAndSignature2 import PartyAndSignature2
from .Undertaking3 import Undertaking3

class UndertakingIssuanceMessage(base_types._BaseFieldType):

	__slots__ = ["_UdrtkgDtls", "_DgtlSgntr"]
	@property
	def UdrtkgDtls(self):
		return self._UdrtkgDtls

	@UdrtkgDtls.setter
	def UdrtkgDtls(self, value):
		self._UdrtkgDtls = value if type(value) != base_types.auto else self.make_default("UdrtkgDtls")

	@UdrtkgDtls.deleter
	def UdrtkgDtls(self):
		del self._UdrtkgDtls
		self._UdrtkgDtls = None

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
		base_types.FieldEntry(name='UdrtkgDtls', type=Undertaking3, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DgtlSgntr', type=PartyAndSignature2, min=0, max=1, mutex_group=None, array=False),
	))

