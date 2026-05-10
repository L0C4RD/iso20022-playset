from . import base_types
import PartyAndSignature2
import UndertakingDemandWithdrawal1

class DemandWithdrawalNotificationV01(base_types._BaseFieldType):

	__slots__ = ["_DgtlSgntr", "_DmndWdrwlNtfctnDtls"]
	@property
	def DgtlSgntr(self):
		return self._DgtlSgntr

	@DgtlSgntr.setter
	def DgtlSgntr(self, value):
		self._DgtlSgntr = value if type(value) != auto else self.make_default("DgtlSgntr")

	@DgtlSgntr.deleter
	def DgtlSgntr(self):
		del self._DgtlSgntr
		self._DgtlSgntr = None

	@property
	def DmndWdrwlNtfctnDtls(self):
		return self._DmndWdrwlNtfctnDtls

	@DmndWdrwlNtfctnDtls.setter
	def DmndWdrwlNtfctnDtls(self, value):
		self._DmndWdrwlNtfctnDtls = value if type(value) != auto else self.make_default("DmndWdrwlNtfctnDtls")

	@DmndWdrwlNtfctnDtls.deleter
	def DmndWdrwlNtfctnDtls(self):
		del self._DmndWdrwlNtfctnDtls
		self._DmndWdrwlNtfctnDtls = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='DgtlSgntr', type=PartyAndSignature2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DmndWdrwlNtfctnDtls', type=UndertakingDemandWithdrawal1, min=1, max=1, mutex_group=None, array=False),
	))

