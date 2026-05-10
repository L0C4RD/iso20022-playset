from . import base_types
from ._LoyaltyAccount3 import LoyaltyAccount3
from ._PaymentAccount3 import PaymentAccount3
from ._PaymentReceipt6 import PaymentReceipt6
from ._TransactionIdentifier1 import TransactionIdentifier1
from ._StoredValueAccount2 import StoredValueAccount2

class BalanceInquiryResponse6(base_types._BaseFieldType):

	__slots__ = ["_PmtAcct", "_StordValAcct", "_SaleTxId", "_LltyAcct", "_Rct", "_POITxId"]
	@property
	def LltyAcct(self):
		return self._LltyAcct

	@LltyAcct.setter
	def LltyAcct(self, value):
		self._LltyAcct = value if type(value) != base_types.auto else self.make_default("LltyAcct")

	@LltyAcct.deleter
	def LltyAcct(self):
		del self._LltyAcct
		self._LltyAcct = None

	@property
	def POITxId(self):
		return self._POITxId

	@POITxId.setter
	def POITxId(self, value):
		self._POITxId = value if type(value) != base_types.auto else self.make_default("POITxId")

	@POITxId.deleter
	def POITxId(self):
		del self._POITxId
		self._POITxId = None

	@property
	def PmtAcct(self):
		return self._PmtAcct

	@PmtAcct.setter
	def PmtAcct(self, value):
		self._PmtAcct = value if type(value) != base_types.auto else self.make_default("PmtAcct")

	@PmtAcct.deleter
	def PmtAcct(self):
		del self._PmtAcct
		self._PmtAcct = None

	@property
	def Rct(self):
		return self._Rct

	@Rct.setter
	def Rct(self, value):
		self._Rct = value if type(value) != base_types.auto else self.make_default("Rct")

	@Rct.deleter
	def Rct(self):
		del self._Rct
		self._Rct = None

	@property
	def SaleTxId(self):
		return self._SaleTxId

	@SaleTxId.setter
	def SaleTxId(self, value):
		self._SaleTxId = value if type(value) != base_types.auto else self.make_default("SaleTxId")

	@SaleTxId.deleter
	def SaleTxId(self):
		del self._SaleTxId
		self._SaleTxId = None

	@property
	def StordValAcct(self):
		return self._StordValAcct

	@StordValAcct.setter
	def StordValAcct(self, value):
		self._StordValAcct = value if type(value) != base_types.auto else self.make_default("StordValAcct")

	@StordValAcct.deleter
	def StordValAcct(self):
		del self._StordValAcct
		self._StordValAcct = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='LltyAcct', type=LoyaltyAccount3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='POITxId', type=TransactionIdentifier1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PmtAcct', type=PaymentAccount3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Rct', type=PaymentReceipt6, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SaleTxId', type=TransactionIdentifier1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StordValAcct', type=StoredValueAccount2, min=0, max=None, mutex_group=None, array=True),
	))

