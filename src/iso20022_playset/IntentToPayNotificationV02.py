from . import base_types
from .IntentToPay2 import IntentToPay2
from .BICIdentification1 import BICIdentification1
from .MessageIdentification1 import MessageIdentification1
from .SimpleIdentificationInformation import SimpleIdentificationInformation

class IntentToPayNotificationV02(base_types._BaseFieldType):

	__slots__ = ["_NtfctnId", "_TxId", "_SubmitrTxRef", "_InttToPay", "_BuyrBk", "_SellrBk"]
	@property
	def NtfctnId(self):
		return self._NtfctnId

	@NtfctnId.setter
	def NtfctnId(self, value):
		self._NtfctnId = value if type(value) != base_types.auto else self.make_default("NtfctnId")

	@NtfctnId.deleter
	def NtfctnId(self):
		del self._NtfctnId
		self._NtfctnId = None

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
	def SubmitrTxRef(self):
		return self._SubmitrTxRef

	@SubmitrTxRef.setter
	def SubmitrTxRef(self, value):
		self._SubmitrTxRef = value if type(value) != base_types.auto else self.make_default("SubmitrTxRef")

	@SubmitrTxRef.deleter
	def SubmitrTxRef(self):
		del self._SubmitrTxRef
		self._SubmitrTxRef = None

	@property
	def InttToPay(self):
		return self._InttToPay

	@InttToPay.setter
	def InttToPay(self, value):
		self._InttToPay = value if type(value) != base_types.auto else self.make_default("InttToPay")

	@InttToPay.deleter
	def InttToPay(self):
		del self._InttToPay
		self._InttToPay = None

	@property
	def BuyrBk(self):
		return self._BuyrBk

	@BuyrBk.setter
	def BuyrBk(self, value):
		self._BuyrBk = value if type(value) != base_types.auto else self.make_default("BuyrBk")

	@BuyrBk.deleter
	def BuyrBk(self):
		del self._BuyrBk
		self._BuyrBk = None

	@property
	def SellrBk(self):
		return self._SellrBk

	@SellrBk.setter
	def SellrBk(self, value):
		self._SellrBk = value if type(value) != base_types.auto else self.make_default("SellrBk")

	@SellrBk.deleter
	def SellrBk(self):
		del self._SellrBk
		self._SellrBk = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='NtfctnId', type=MessageIdentification1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxId', type=SimpleIdentificationInformation, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SubmitrTxRef', type=SimpleIdentificationInformation, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InttToPay', type=IntentToPay2, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BuyrBk', type=BICIdentification1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SellrBk', type=BICIdentification1, min=1, max=1, mutex_group=None, array=False),
	))

