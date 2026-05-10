from . import base_types
from .UndertakingTerminationNotice1 import UndertakingTerminationNotice1
from .PartyAndSignature2 import PartyAndSignature2

class UndertakingTerminationNotificationV01(base_types._BaseFieldType):

	__slots__ = ["_UdrtkgTermntnNtfctnDtls", "_DgtlSgntr"]
	@property
	def UdrtkgTermntnNtfctnDtls(self):
		return self._UdrtkgTermntnNtfctnDtls

	@UdrtkgTermntnNtfctnDtls.setter
	def UdrtkgTermntnNtfctnDtls(self, value):
		self._UdrtkgTermntnNtfctnDtls = value if type(value) != base_types.auto else self.make_default("UdrtkgTermntnNtfctnDtls")

	@UdrtkgTermntnNtfctnDtls.deleter
	def UdrtkgTermntnNtfctnDtls(self):
		del self._UdrtkgTermntnNtfctnDtls
		self._UdrtkgTermntnNtfctnDtls = None

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
		base_types.FieldEntry(name='UdrtkgTermntnNtfctnDtls', type=UndertakingTerminationNotice1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DgtlSgntr', type=PartyAndSignature2, min=0, max=1, mutex_group=None, array=False),
	))

