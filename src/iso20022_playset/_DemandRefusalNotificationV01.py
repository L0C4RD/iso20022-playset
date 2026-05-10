from . import base_types
from ._PartyAndSignature2 import PartyAndSignature2
from ._DemandRefusal1 import DemandRefusal1

class DemandRefusalNotificationV01(base_types._BaseFieldType):

	__slots__ = ["_DmndRfslNtfctnDtls", "_DgtlSgntr"]
	@property
	def DmndRfslNtfctnDtls(self):
		return self._DmndRfslNtfctnDtls

	@DmndRfslNtfctnDtls.setter
	def DmndRfslNtfctnDtls(self, value):
		self._DmndRfslNtfctnDtls = value if type(value) != base_types.auto else self.make_default("DmndRfslNtfctnDtls")

	@DmndRfslNtfctnDtls.deleter
	def DmndRfslNtfctnDtls(self):
		del self._DmndRfslNtfctnDtls
		self._DmndRfslNtfctnDtls = None

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
		base_types.FieldEntry(name='DmndRfslNtfctnDtls', type=DemandRefusal1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='DgtlSgntr', type=PartyAndSignature2, min=0, max=1, mutex_group=None, array=False),
	))

