from . import base_types
from ._UndertakingAdvice2 import UndertakingAdvice2
from ._PartyAndSignature2 import PartyAndSignature2

class UndertakingIssuanceNotificationV01(base_types._BaseFieldType):

	__slots__ = ["_UdrtkgIssncNtfctnDtls", "_DgtlSgntr"]
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
	def UdrtkgIssncNtfctnDtls(self):
		return self._UdrtkgIssncNtfctnDtls

	@UdrtkgIssncNtfctnDtls.setter
	def UdrtkgIssncNtfctnDtls(self, value):
		self._UdrtkgIssncNtfctnDtls = value if type(value) != base_types.auto else self.make_default("UdrtkgIssncNtfctnDtls")

	@UdrtkgIssncNtfctnDtls.deleter
	def UdrtkgIssncNtfctnDtls(self):
		del self._UdrtkgIssncNtfctnDtls
		self._UdrtkgIssncNtfctnDtls = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='DgtlSgntr', type=PartyAndSignature2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UdrtkgIssncNtfctnDtls', type=UndertakingAdvice2, min=1, max=1, mutex_group=None, array=False),
	))

