from . import base_types
from ._Amendment6 import Amendment6
from ._PartyAndSignature2 import PartyAndSignature2

class UndertakingAmendmentNotificationV01(base_types._BaseFieldType):

	__slots__ = ["_UdrtkgAmdmntNtfctnDtls", "_DgtlSgntr"]
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
	def UdrtkgAmdmntNtfctnDtls(self):
		return self._UdrtkgAmdmntNtfctnDtls

	@UdrtkgAmdmntNtfctnDtls.setter
	def UdrtkgAmdmntNtfctnDtls(self, value):
		self._UdrtkgAmdmntNtfctnDtls = value if type(value) != base_types.auto else self.make_default("UdrtkgAmdmntNtfctnDtls")

	@UdrtkgAmdmntNtfctnDtls.deleter
	def UdrtkgAmdmntNtfctnDtls(self):
		del self._UdrtkgAmdmntNtfctnDtls
		self._UdrtkgAmdmntNtfctnDtls = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='DgtlSgntr', type=PartyAndSignature2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UdrtkgAmdmntNtfctnDtls', type=Amendment6, min=1, max=1, mutex_group=None, array=False),
	))

