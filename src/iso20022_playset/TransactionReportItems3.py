from . import base_types
from .CountryCode import CountryCode
from .Max35Text import Max35Text
from .TransactionStatus4 import TransactionStatus4
from .BICIdentification1 import BICIdentification1
from .CurrencyAndAmount import CurrencyAndAmount
from .PartyIdentification26 import PartyIdentification26
from .PendingActivity2 import PendingActivity2
from .DocumentIdentification3 import DocumentIdentification3
from .DocumentIdentification5 import DocumentIdentification5
from .DocumentIdentification7 import DocumentIdentification7

class TransactionReportItems3(base_types._BaseFieldType):

	__slots__ = ["_PurchsOrdrRef", "_TtlNetAmt", "_OutsdngAmt", "_UsrTxRef", "_BuyrBkCtry", "_SellrBkCtry", "_Buyr", "_PdgReqForActn", "_SubmitgBk", "_Sellr", "_TxSts", "_TxId", "_EstblishdBaselnId", "_OblgrBk", "_BuyrBk", "_SellrBk"]
	@property
	def PurchsOrdrRef(self):
		return self._PurchsOrdrRef

	@PurchsOrdrRef.setter
	def PurchsOrdrRef(self, value):
		self._PurchsOrdrRef = value if type(value) != auto else self.make_default("PurchsOrdrRef")

	@PurchsOrdrRef.deleter
	def PurchsOrdrRef(self):
		del self._PurchsOrdrRef
		self._PurchsOrdrRef = None

	@property
	def TtlNetAmt(self):
		return self._TtlNetAmt

	@TtlNetAmt.setter
	def TtlNetAmt(self, value):
		self._TtlNetAmt = value if type(value) != auto else self.make_default("TtlNetAmt")

	@TtlNetAmt.deleter
	def TtlNetAmt(self):
		del self._TtlNetAmt
		self._TtlNetAmt = None

	@property
	def OutsdngAmt(self):
		return self._OutsdngAmt

	@OutsdngAmt.setter
	def OutsdngAmt(self, value):
		self._OutsdngAmt = value if type(value) != auto else self.make_default("OutsdngAmt")

	@OutsdngAmt.deleter
	def OutsdngAmt(self):
		del self._OutsdngAmt
		self._OutsdngAmt = None

	@property
	def UsrTxRef(self):
		return self._UsrTxRef

	@UsrTxRef.setter
	def UsrTxRef(self, value):
		self._UsrTxRef = value if type(value) != auto else self.make_default("UsrTxRef")

	@UsrTxRef.deleter
	def UsrTxRef(self):
		del self._UsrTxRef
		self._UsrTxRef = None

	@property
	def BuyrBkCtry(self):
		return self._BuyrBkCtry

	@BuyrBkCtry.setter
	def BuyrBkCtry(self, value):
		self._BuyrBkCtry = value if type(value) != auto else self.make_default("BuyrBkCtry")

	@BuyrBkCtry.deleter
	def BuyrBkCtry(self):
		del self._BuyrBkCtry
		self._BuyrBkCtry = None

	@property
	def SellrBkCtry(self):
		return self._SellrBkCtry

	@SellrBkCtry.setter
	def SellrBkCtry(self, value):
		self._SellrBkCtry = value if type(value) != auto else self.make_default("SellrBkCtry")

	@SellrBkCtry.deleter
	def SellrBkCtry(self):
		del self._SellrBkCtry
		self._SellrBkCtry = None

	@property
	def Buyr(self):
		return self._Buyr

	@Buyr.setter
	def Buyr(self, value):
		self._Buyr = value if type(value) != auto else self.make_default("Buyr")

	@Buyr.deleter
	def Buyr(self):
		del self._Buyr
		self._Buyr = None

	@property
	def PdgReqForActn(self):
		return self._PdgReqForActn

	@PdgReqForActn.setter
	def PdgReqForActn(self, value):
		self._PdgReqForActn = value if type(value) != auto else self.make_default("PdgReqForActn")

	@PdgReqForActn.deleter
	def PdgReqForActn(self):
		del self._PdgReqForActn
		self._PdgReqForActn = None

	@property
	def SubmitgBk(self):
		return self._SubmitgBk

	@SubmitgBk.setter
	def SubmitgBk(self, value):
		self._SubmitgBk = value if type(value) != auto else self.make_default("SubmitgBk")

	@SubmitgBk.deleter
	def SubmitgBk(self):
		del self._SubmitgBk
		self._SubmitgBk = None

	@property
	def Sellr(self):
		return self._Sellr

	@Sellr.setter
	def Sellr(self, value):
		self._Sellr = value if type(value) != auto else self.make_default("Sellr")

	@Sellr.deleter
	def Sellr(self):
		del self._Sellr
		self._Sellr = None

	@property
	def TxSts(self):
		return self._TxSts

	@TxSts.setter
	def TxSts(self, value):
		self._TxSts = value if type(value) != auto else self.make_default("TxSts")

	@TxSts.deleter
	def TxSts(self):
		del self._TxSts
		self._TxSts = None

	@property
	def TxId(self):
		return self._TxId

	@TxId.setter
	def TxId(self, value):
		self._TxId = value if type(value) != auto else self.make_default("TxId")

	@TxId.deleter
	def TxId(self):
		del self._TxId
		self._TxId = None

	@property
	def EstblishdBaselnId(self):
		return self._EstblishdBaselnId

	@EstblishdBaselnId.setter
	def EstblishdBaselnId(self, value):
		self._EstblishdBaselnId = value if type(value) != auto else self.make_default("EstblishdBaselnId")

	@EstblishdBaselnId.deleter
	def EstblishdBaselnId(self):
		del self._EstblishdBaselnId
		self._EstblishdBaselnId = None

	@property
	def OblgrBk(self):
		return self._OblgrBk

	@OblgrBk.setter
	def OblgrBk(self, value):
		self._OblgrBk = value if type(value) != auto else self.make_default("OblgrBk")

	@OblgrBk.deleter
	def OblgrBk(self):
		del self._OblgrBk
		self._OblgrBk = None

	@property
	def BuyrBk(self):
		return self._BuyrBk

	@BuyrBk.setter
	def BuyrBk(self, value):
		self._BuyrBk = value if type(value) != auto else self.make_default("BuyrBk")

	@BuyrBk.deleter
	def BuyrBk(self):
		del self._BuyrBk
		self._BuyrBk = None

	@property
	def SellrBk(self):
		return self._SellrBk

	@SellrBk.setter
	def SellrBk(self, value):
		self._SellrBk = value if type(value) != auto else self.make_default("SellrBk")

	@SellrBk.deleter
	def SellrBk(self):
		del self._SellrBk
		self._SellrBk = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='PurchsOrdrRef', type=DocumentIdentification7, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlNetAmt', type=CurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OutsdngAmt', type=CurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UsrTxRef', type=DocumentIdentification5, min=0, max=2, mutex_group=None, array=True),
		base_types.FieldEntry(name='BuyrBkCtry', type=CountryCode, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SellrBkCtry', type=CountryCode, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Buyr', type=PartyIdentification26, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PdgReqForActn', type=PendingActivity2, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SubmitgBk', type=BICIdentification1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Sellr', type=PartyIdentification26, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxSts', type=TransactionStatus4, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='EstblishdBaselnId', type=DocumentIdentification3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OblgrBk', type=BICIdentification1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='BuyrBk', type=BICIdentification1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SellrBk', type=BICIdentification1, min=1, max=1, mutex_group=None, array=False),
	))

