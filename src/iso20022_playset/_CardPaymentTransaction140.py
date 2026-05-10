from . import base_types
from .CardPaymentTransactionDetails53 import CardPaymentTransactionDetails53
from .TransactionIdentifier1 import TransactionIdentifier1
from .CardPaymentTransaction138 import CardPaymentTransaction138
from .CardPaymentServiceType12Code import CardPaymentServiceType12Code
from .AuthorisationResult18 import AuthorisationResult18
from .CardAccount16 import CardAccount16
from .Min3Max4Text import Min3Max4Text
from .CardPaymentServiceType15Code import CardPaymentServiceType15Code
from .TrueFalseIndicator import TrueFalseIndicator
from .Max35Text import Max35Text
from .FailureReason3Code import FailureReason3Code
from .Max70Text import Max70Text
from .Max140Text import Max140Text
from .CardPaymentServiceType9Code import CardPaymentServiceType9Code

class CardPaymentTransaction140(base_types._BaseFieldType):

	__slots__ = ["_TxDtls", "_AcctFr", "_TxId", "_CstmrCnsnt", "_IntrchngData", "_Rvsl", "_TxCaptr", "_AuthstnRslt", "_AddtlTxData", "_CardPrgrmmPropsd", "_AcctTo", "_LastTxFlg", "_SvcAttr", "_MrchntCITId", "_FailrRsn", "_InitrTxId", "_RcptTxId", "_CardPrgrmmApld", "_AddtlSvc", "_OrgnlTx", "_SaleRefId", "_RcncltnId", "_MrchntRefData", "_TxSucss", "_TxTp", "_IssrCITId", "_MrchntCtgyCd", "_MrchntOvrrd"]
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
	def AcctFr(self):
		return self._AcctFr

	@AcctFr.setter
	def AcctFr(self, value):
		self._AcctFr = value if type(value) != base_types.auto else self.make_default("AcctFr")

	@AcctFr.deleter
	def AcctFr(self):
		del self._AcctFr
		self._AcctFr = None

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
	def IntrchngData(self):
		return self._IntrchngData

	@IntrchngData.setter
	def IntrchngData(self, value):
		self._IntrchngData = value if type(value) != base_types.auto else self.make_default("IntrchngData")

	@IntrchngData.deleter
	def IntrchngData(self):
		del self._IntrchngData
		self._IntrchngData = None

	@property
	def Rvsl(self):
		return self._Rvsl

	@Rvsl.setter
	def Rvsl(self, value):
		self._Rvsl = value if type(value) != base_types.auto else self.make_default("Rvsl")

	@Rvsl.deleter
	def Rvsl(self):
		del self._Rvsl
		self._Rvsl = None

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
	def AuthstnRslt(self):
		return self._AuthstnRslt

	@AuthstnRslt.setter
	def AuthstnRslt(self, value):
		self._AuthstnRslt = value if type(value) != base_types.auto else self.make_default("AuthstnRslt")

	@AuthstnRslt.deleter
	def AuthstnRslt(self):
		del self._AuthstnRslt
		self._AuthstnRslt = None

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
	def AcctTo(self):
		return self._AcctTo

	@AcctTo.setter
	def AcctTo(self, value):
		self._AcctTo = value if type(value) != base_types.auto else self.make_default("AcctTo")

	@AcctTo.deleter
	def AcctTo(self):
		del self._AcctTo
		self._AcctTo = None

	@property
	def LastTxFlg(self):
		return self._LastTxFlg

	@LastTxFlg.setter
	def LastTxFlg(self, value):
		self._LastTxFlg = value if type(value) != base_types.auto else self.make_default("LastTxFlg")

	@LastTxFlg.deleter
	def LastTxFlg(self):
		del self._LastTxFlg
		self._LastTxFlg = None

	@property
	def SvcAttr(self):
		return self._SvcAttr

	@SvcAttr.setter
	def SvcAttr(self, value):
		self._SvcAttr = value if type(value) != base_types.auto else self.make_default("SvcAttr")

	@SvcAttr.deleter
	def SvcAttr(self):
		del self._SvcAttr
		self._SvcAttr = None

	@property
	def MrchntCITId(self):
		return self._MrchntCITId

	@MrchntCITId.setter
	def MrchntCITId(self, value):
		self._MrchntCITId = value if type(value) != base_types.auto else self.make_default("MrchntCITId")

	@MrchntCITId.deleter
	def MrchntCITId(self):
		del self._MrchntCITId
		self._MrchntCITId = None

	@property
	def FailrRsn(self):
		return self._FailrRsn

	@FailrRsn.setter
	def FailrRsn(self, value):
		self._FailrRsn = value if type(value) != base_types.auto else self.make_default("FailrRsn")

	@FailrRsn.deleter
	def FailrRsn(self):
		del self._FailrRsn
		self._FailrRsn = None

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
	def AddtlSvc(self):
		return self._AddtlSvc

	@AddtlSvc.setter
	def AddtlSvc(self, value):
		self._AddtlSvc = value if type(value) != base_types.auto else self.make_default("AddtlSvc")

	@AddtlSvc.deleter
	def AddtlSvc(self):
		del self._AddtlSvc
		self._AddtlSvc = None

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
	def MrchntRefData(self):
		return self._MrchntRefData

	@MrchntRefData.setter
	def MrchntRefData(self, value):
		self._MrchntRefData = value if type(value) != base_types.auto else self.make_default("MrchntRefData")

	@MrchntRefData.deleter
	def MrchntRefData(self):
		del self._MrchntRefData
		self._MrchntRefData = None

	@property
	def TxSucss(self):
		return self._TxSucss

	@TxSucss.setter
	def TxSucss(self, value):
		self._TxSucss = value if type(value) != base_types.auto else self.make_default("TxSucss")

	@TxSucss.deleter
	def TxSucss(self):
		del self._TxSucss
		self._TxSucss = None

	@property
	def TxTp(self):
		return self._TxTp

	@TxTp.setter
	def TxTp(self, value):
		self._TxTp = value if type(value) != base_types.auto else self.make_default("TxTp")

	@TxTp.deleter
	def TxTp(self):
		del self._TxTp
		self._TxTp = None

	@property
	def IssrCITId(self):
		return self._IssrCITId

	@IssrCITId.setter
	def IssrCITId(self, value):
		self._IssrCITId = value if type(value) != base_types.auto else self.make_default("IssrCITId")

	@IssrCITId.deleter
	def IssrCITId(self):
		del self._IssrCITId
		self._IssrCITId = None

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
	def MrchntOvrrd(self):
		return self._MrchntOvrrd

	@MrchntOvrrd.setter
	def MrchntOvrrd(self, value):
		self._MrchntOvrrd = value if type(value) != base_types.auto else self.make_default("MrchntOvrrd")

	@MrchntOvrrd.deleter
	def MrchntOvrrd(self):
		del self._MrchntOvrrd
		self._MrchntOvrrd = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='TxDtls', type=CardPaymentTransactionDetails53, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AcctFr', type=CardAccount16, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxId', type=TransactionIdentifier1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CstmrCnsnt', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IntrchngData', type=Max140Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Rvsl', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxCaptr', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AuthstnRslt', type=AuthorisationResult18, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AddtlTxData', type=Max70Text, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='CardPrgrmmPropsd', type=Max35Text, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='AcctTo', type=CardAccount16, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LastTxFlg', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SvcAttr', type=CardPaymentServiceType15Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MrchntCITId', type=Max140Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FailrRsn', type=FailureReason3Code, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='InitrTxId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RcptTxId', type=Max140Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CardPrgrmmApld', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AddtlSvc', type=CardPaymentServiceType9Code, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='OrgnlTx', type=CardPaymentTransaction138, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SaleRefId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RcncltnId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MrchntRefData', type=Max70Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxSucss', type=TrueFalseIndicator, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxTp', type=CardPaymentServiceType12Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IssrCITId', type=Max140Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MrchntCtgyCd', type=Min3Max4Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MrchntOvrrd', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
	))

