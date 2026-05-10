from . import base_types
from ._CardPaymentTransaction138 import CardPaymentTransaction138
from ._CardPaymentTransactionDetails50 import CardPaymentTransactionDetails50
from ._Max140Text import Max140Text
from ._Max35Text import Max35Text
from ._Max70Text import Max70Text
from ._Min3Max4Text import Min3Max4Text
from ._TransactionIdentifier1 import TransactionIdentifier1
from ._TrueFalseIndicator import TrueFalseIndicator

class CardPaymentTransaction142(base_types._BaseFieldType):

	__slots__ = ["_AddtlTxData", "_CardPrgrmmApld", "_CardPrgrmmPropsd", "_CstmrCnsnt", "_InitrTxId", "_MrchntCtgyCd", "_OrgnlTx", "_RcncltnId", "_RcptTxId", "_SaleRefId", "_TxCaptr", "_TxDtls", "_TxId"]
	@property
	def AddtlTxData(self):
		return self._AddtlTxData

	@AddtlTxData.setter
	def AddtlTxData(self, value):
		self._AddtlTxData = value if type(value) != base_types.auto else self.make_default("AddtlTxData")

	@AddtlTxData.deleter
	def AddtlTxData(self):
		del self._AddtlTxData
		self._AddtlTxData = None

	@property
	def CardPrgrmmApld(self):
		return self._CardPrgrmmApld

	@CardPrgrmmApld.setter
	def CardPrgrmmApld(self, value):
		self._CardPrgrmmApld = value if type(value) != base_types.auto else self.make_default("CardPrgrmmApld")

	@CardPrgrmmApld.deleter
	def CardPrgrmmApld(self):
		del self._CardPrgrmmApld
		self._CardPrgrmmApld = None

	@property
	def CardPrgrmmPropsd(self):
		return self._CardPrgrmmPropsd

	@CardPrgrmmPropsd.setter
	def CardPrgrmmPropsd(self, value):
		self._CardPrgrmmPropsd = value if type(value) != base_types.auto else self.make_default("CardPrgrmmPropsd")

	@CardPrgrmmPropsd.deleter
	def CardPrgrmmPropsd(self):
		del self._CardPrgrmmPropsd
		self._CardPrgrmmPropsd = None

	@property
	def CstmrCnsnt(self):
		return self._CstmrCnsnt

	@CstmrCnsnt.setter
	def CstmrCnsnt(self, value):
		self._CstmrCnsnt = value if type(value) != base_types.auto else self.make_default("CstmrCnsnt")

	@CstmrCnsnt.deleter
	def CstmrCnsnt(self):
		del self._CstmrCnsnt
		self._CstmrCnsnt = None

	@property
	def InitrTxId(self):
		return self._InitrTxId

	@InitrTxId.setter
	def InitrTxId(self, value):
		self._InitrTxId = value if type(value) != base_types.auto else self.make_default("InitrTxId")

	@InitrTxId.deleter
	def InitrTxId(self):
		del self._InitrTxId
		self._InitrTxId = None

	@property
	def MrchntCtgyCd(self):
		return self._MrchntCtgyCd

	@MrchntCtgyCd.setter
	def MrchntCtgyCd(self, value):
		self._MrchntCtgyCd = value if type(value) != base_types.auto else self.make_default("MrchntCtgyCd")

	@MrchntCtgyCd.deleter
	def MrchntCtgyCd(self):
		del self._MrchntCtgyCd
		self._MrchntCtgyCd = None

	@property
	def OrgnlTx(self):
		return self._OrgnlTx

	@OrgnlTx.setter
	def OrgnlTx(self, value):
		self._OrgnlTx = value if type(value) != base_types.auto else self.make_default("OrgnlTx")

	@OrgnlTx.deleter
	def OrgnlTx(self):
		del self._OrgnlTx
		self._OrgnlTx = None

	@property
	def RcncltnId(self):
		return self._RcncltnId

	@RcncltnId.setter
	def RcncltnId(self, value):
		self._RcncltnId = value if type(value) != base_types.auto else self.make_default("RcncltnId")

	@RcncltnId.deleter
	def RcncltnId(self):
		del self._RcncltnId
		self._RcncltnId = None

	@property
	def RcptTxId(self):
		return self._RcptTxId

	@RcptTxId.setter
	def RcptTxId(self, value):
		self._RcptTxId = value if type(value) != base_types.auto else self.make_default("RcptTxId")

	@RcptTxId.deleter
	def RcptTxId(self):
		del self._RcptTxId
		self._RcptTxId = None

	@property
	def SaleRefId(self):
		return self._SaleRefId

	@SaleRefId.setter
	def SaleRefId(self, value):
		self._SaleRefId = value if type(value) != base_types.auto else self.make_default("SaleRefId")

	@SaleRefId.deleter
	def SaleRefId(self):
		del self._SaleRefId
		self._SaleRefId = None

	@property
	def TxCaptr(self):
		return self._TxCaptr

	@TxCaptr.setter
	def TxCaptr(self, value):
		self._TxCaptr = value if type(value) != base_types.auto else self.make_default("TxCaptr")

	@TxCaptr.deleter
	def TxCaptr(self):
		del self._TxCaptr
		self._TxCaptr = None

	@property
	def TxDtls(self):
		return self._TxDtls

	@TxDtls.setter
	def TxDtls(self, value):
		self._TxDtls = value if type(value) != base_types.auto else self.make_default("TxDtls")

	@TxDtls.deleter
	def TxDtls(self):
		del self._TxDtls
		self._TxDtls = None

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

	_field_defs = frozenset((
		base_types.FieldEntry(name='AddtlTxData', type=Max70Text, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='CardPrgrmmApld', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CardPrgrmmPropsd', type=Max35Text, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='CstmrCnsnt', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InitrTxId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MrchntCtgyCd', type=Min3Max4Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlTx', type=CardPaymentTransaction138, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RcncltnId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RcptTxId', type=Max140Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SaleRefId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxCaptr', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxDtls', type=CardPaymentTransactionDetails50, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxId', type=TransactionIdentifier1, min=1, max=1, mutex_group=None, array=False),
	))

