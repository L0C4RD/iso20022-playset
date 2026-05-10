from . import base_types
from ._BICIdentification1 import BICIdentification1
from ._DocumentIdentification3 import DocumentIdentification3
from ._DocumentIdentification5 import DocumentIdentification5
from ._IntentToPay2 import IntentToPay2
from ._MessageIdentification1 import MessageIdentification1
from ._PendingActivity2 import PendingActivity2
from ._SimpleIdentificationInformation import SimpleIdentificationInformation
from ._TransactionStatus4 import TransactionStatus4

class ForwardIntentToPayNotificationV02(base_types._BaseFieldType):

	__slots__ = ["_BuyrBk", "_EstblishdBaselnId", "_InttToPay", "_NtfctnId", "_ReqForActn", "_SellrBk", "_TxId", "_TxSts", "_UsrTxRef"]
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
	def EstblishdBaselnId(self):
		return self._EstblishdBaselnId

	@EstblishdBaselnId.setter
	def EstblishdBaselnId(self, value):
		self._EstblishdBaselnId = value if type(value) != base_types.auto else self.make_default("EstblishdBaselnId")

	@EstblishdBaselnId.deleter
	def EstblishdBaselnId(self):
		del self._EstblishdBaselnId
		self._EstblishdBaselnId = None

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
	def ReqForActn(self):
		return self._ReqForActn

	@ReqForActn.setter
	def ReqForActn(self, value):
		self._ReqForActn = value if type(value) != base_types.auto else self.make_default("ReqForActn")

	@ReqForActn.deleter
	def ReqForActn(self):
		del self._ReqForActn
		self._ReqForActn = None

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
	def TxSts(self):
		return self._TxSts

	@TxSts.setter
	def TxSts(self, value):
		self._TxSts = value if type(value) != base_types.auto else self.make_default("TxSts")

	@TxSts.deleter
	def TxSts(self):
		del self._TxSts
		self._TxSts = None

	@property
	def UsrTxRef(self):
		return self._UsrTxRef

	@UsrTxRef.setter
	def UsrTxRef(self, value):
		self._UsrTxRef = value if type(value) != base_types.auto else self.make_default("UsrTxRef")

	@UsrTxRef.deleter
	def UsrTxRef(self):
		del self._UsrTxRef
		self._UsrTxRef = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='BuyrBk', type=BICIdentification1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='EstblishdBaselnId', type=DocumentIdentification3, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InttToPay', type=IntentToPay2, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NtfctnId', type=MessageIdentification1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ReqForActn', type=PendingActivity2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SellrBk', type=BICIdentification1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxId', type=SimpleIdentificationInformation, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxSts', type=TransactionStatus4, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UsrTxRef', type=DocumentIdentification5, min=0, max=2, mutex_group=None, array=True),
	))

