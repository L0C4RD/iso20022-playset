from . import base_types
from ._PartyAndSignature2 import PartyAndSignature2
from ._UndertakingNonExtensionStatusAdvice1 import UndertakingNonExtensionStatusAdvice1

class UndertakingNonExtensionNotificationV01(base_types._BaseFieldType):

	__slots__ = ["_DgtlSgntr", "_UdrtkgNonXtnsnNtfctnDtls"]
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
	def UdrtkgNonXtnsnNtfctnDtls(self):
		return self._UdrtkgNonXtnsnNtfctnDtls

	@UdrtkgNonXtnsnNtfctnDtls.setter
	def UdrtkgNonXtnsnNtfctnDtls(self, value):
		self._UdrtkgNonXtnsnNtfctnDtls = value if type(value) != base_types.auto else self.make_default("UdrtkgNonXtnsnNtfctnDtls")

	@UdrtkgNonXtnsnNtfctnDtls.deleter
	def UdrtkgNonXtnsnNtfctnDtls(self):
		del self._UdrtkgNonXtnsnNtfctnDtls
		self._UdrtkgNonXtnsnNtfctnDtls = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='DgtlSgntr', type=PartyAndSignature2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UdrtkgNonXtnsnNtfctnDtls', type=UndertakingNonExtensionStatusAdvice1, min=1, max=1, mutex_group=None, array=False),
	))

