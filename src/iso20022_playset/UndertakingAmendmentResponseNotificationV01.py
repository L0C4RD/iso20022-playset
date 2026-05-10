from . import base_types
from .Amendment9 import Amendment9
from .PartyAndSignature2 import PartyAndSignature2
from .Max2000Text import Max2000Text

class UndertakingAmendmentResponseNotificationV01(base_types._BaseFieldType):

	__slots__ = ["_AddtlInf", "_UdrtkgAmdmntRspnNtfctnDtls", "_DgtlSgntr"]
	@property
	def AddtlInf(self):
		return self._AddtlInf

	@AddtlInf.setter
	def AddtlInf(self, value):
		self._AddtlInf = value if type(value) != base_types.auto else self.make_default("AddtlInf")

	@AddtlInf.deleter
	def AddtlInf(self):
		del self._AddtlInf
		self._AddtlInf = None

	@property
	def UdrtkgAmdmntRspnNtfctnDtls(self):
		return self._UdrtkgAmdmntRspnNtfctnDtls

	@UdrtkgAmdmntRspnNtfctnDtls.setter
	def UdrtkgAmdmntRspnNtfctnDtls(self, value):
		self._UdrtkgAmdmntRspnNtfctnDtls = value if type(value) != base_types.auto else self.make_default("UdrtkgAmdmntRspnNtfctnDtls")

	@UdrtkgAmdmntRspnNtfctnDtls.deleter
	def UdrtkgAmdmntRspnNtfctnDtls(self):
		del self._UdrtkgAmdmntRspnNtfctnDtls
		self._UdrtkgAmdmntRspnNtfctnDtls = None

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
		base_types.FieldEntry(name='AddtlInf', type=Max2000Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UdrtkgAmdmntRspnNtfctnDtls', type=Amendment9, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DgtlSgntr', type=PartyAndSignature2, min=0, max=1, mutex_group=None, array=False),
	))

