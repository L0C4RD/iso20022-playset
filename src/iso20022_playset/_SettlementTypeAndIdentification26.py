from . import base_types
from .DateAndDateTime2Choice import DateAndDateTime2Choice
from .DeliveryReceiptType2Code import DeliveryReceiptType2Code
from .RestrictedFINXMax16Text import RestrictedFINXMax16Text

class SettlementTypeAndIdentification26(base_types._BaseFieldType):

	__slots__ = ["_TxId", "_Pmt", "_SttlmDt"]
	@property
	def TxId(self):
		return self._TxId

	@TxId.setter
	def TxId(self, value):
		self._TxId = value if type(value) != base_types.auto else self.make_default("TxId")

	@TxId.deleter
	def TxId(self):
		del self._TxId
		self._TxId = None

	@property
	def Pmt(self):
		return self._Pmt

	@Pmt.setter
	def Pmt(self, value):
		self._Pmt = value if type(value) != base_types.auto else self.make_default("Pmt")

	@Pmt.deleter
	def Pmt(self):
		del self._Pmt
		self._Pmt = None

	@property
	def SttlmDt(self):
		return self._SttlmDt

	@SttlmDt.setter
	def SttlmDt(self, value):
		self._SttlmDt = value if type(value) != base_types.auto else self.make_default("SttlmDt")

	@SttlmDt.deleter
	def SttlmDt(self):
		del self._SttlmDt
		self._SttlmDt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='TxId', type=RestrictedFINXMax16Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Pmt', type=DeliveryReceiptType2Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SttlmDt', type=DateAndDateTime2Choice, min=0, max=1, mutex_group=None, array=False),
	))

