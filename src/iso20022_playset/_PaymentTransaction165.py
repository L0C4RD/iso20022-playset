# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._AuthorisationResult18 import AuthorisationResult18
from ._CardPaymentServiceType15Code import CardPaymentServiceType15Code
from ._CardPaymentServiceType16Code import CardPaymentServiceType16Code
from ._CardPaymentServiceType9Code import CardPaymentServiceType9Code
from ._CardPaymentToken5 import CardPaymentToken5
from ._CardPaymentTransaction131 import CardPaymentTransaction131
from ._CardPaymentTransactionDetails53 import CardPaymentTransactionDetails53
from ._CustomerOrder1 import CustomerOrder1
from ._Max140Text import Max140Text
from ._Max35Text import Max35Text
from ._Max70Text import Max70Text
from ._Min3Max4Text import Min3Max4Text
from ._PaymentInstrumentType2Code import PaymentInstrumentType2Code
from ._PaymentTypeInformation26 import PaymentTypeInformation26
from ._TransactionIdentifier1 import TransactionIdentifier1
from ._TrueFalseIndicator import TrueFalseIndicator

class PaymentTransaction165(base_types._BaseFieldType):

	__slots__ = ["_AddtlSvc", "_AddtlTxData", "_AuthstnRslt", "_CardPrgrmmApld", "_CardPrgrmmPropsd", "_CstmrCnsnt", "_CstmrOrdr", "_CstmrTkn", "_IssrCITId", "_IssrRefData", "_LastTxFlg", "_MrchntCITId", "_MrchntCtgyCd", "_MrchntRefData", "_OrgnlTx", "_PmtInstrm", "_PmtTpInf", "_RcncltnId", "_SaleRefId", "_SaleToAcqrrData", "_SaleToIssrData", "_SaleToPOIData", "_SvcAttr", "_TxCaptr", "_TxDtls", "_TxId", "_TxTp"]
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
	def CstmrOrdr(self):
		return self._CstmrOrdr

	@CstmrOrdr.setter
	def CstmrOrdr(self, value):
		self._CstmrOrdr = value if type(value) != base_types.auto else self.make_default("CstmrOrdr")

	@CstmrOrdr.deleter
	def CstmrOrdr(self):
		del self._CstmrOrdr
		self._CstmrOrdr = None

	@property
	def CstmrTkn(self):
		return self._CstmrTkn

	@CstmrTkn.setter
	def CstmrTkn(self, value):
		self._CstmrTkn = value if type(value) != base_types.auto else self.make_default("CstmrTkn")

	@CstmrTkn.deleter
	def CstmrTkn(self):
		del self._CstmrTkn
		self._CstmrTkn = None

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
	def IssrRefData(self):
		return self._IssrRefData

	@IssrRefData.setter
	def IssrRefData(self, value):
		self._IssrRefData = value if type(value) != base_types.auto else self.make_default("IssrRefData")

	@IssrRefData.deleter
	def IssrRefData(self):
		del self._IssrRefData
		self._IssrRefData = None

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
	def PmtInstrm(self):
		return self._PmtInstrm

	@PmtInstrm.setter
	def PmtInstrm(self, value):
		self._PmtInstrm = value if type(value) != base_types.auto else self.make_default("PmtInstrm")

	@PmtInstrm.deleter
	def PmtInstrm(self):
		del self._PmtInstrm
		self._PmtInstrm = None

	@property
	def PmtTpInf(self):
		return self._PmtTpInf

	@PmtTpInf.setter
	def PmtTpInf(self, value):
		self._PmtTpInf = value if type(value) != base_types.auto else self.make_default("PmtTpInf")

	@PmtTpInf.deleter
	def PmtTpInf(self):
		del self._PmtTpInf
		self._PmtTpInf = None

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
	def SaleToAcqrrData(self):
		return self._SaleToAcqrrData

	@SaleToAcqrrData.setter
	def SaleToAcqrrData(self, value):
		self._SaleToAcqrrData = value if type(value) != base_types.auto else self.make_default("SaleToAcqrrData")

	@SaleToAcqrrData.deleter
	def SaleToAcqrrData(self):
		del self._SaleToAcqrrData
		self._SaleToAcqrrData = None

	@property
	def SaleToIssrData(self):
		return self._SaleToIssrData

	@SaleToIssrData.setter
	def SaleToIssrData(self, value):
		self._SaleToIssrData = value if type(value) != base_types.auto else self.make_default("SaleToIssrData")

	@SaleToIssrData.deleter
	def SaleToIssrData(self):
		del self._SaleToIssrData
		self._SaleToIssrData = None

	@property
	def SaleToPOIData(self):
		return self._SaleToPOIData

	@SaleToPOIData.setter
	def SaleToPOIData(self, value):
		self._SaleToPOIData = value if type(value) != base_types.auto else self.make_default("SaleToPOIData")

	@SaleToPOIData.deleter
	def SaleToPOIData(self):
		del self._SaleToPOIData
		self._SaleToPOIData = None

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

	_field_defs = frozenset((
		base_types.FieldEntry(name='AddtlSvc', type=CardPaymentServiceType9Code, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='AddtlTxData', type=Max70Text, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='AuthstnRslt', type=AuthorisationResult18, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CardPrgrmmApld', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CardPrgrmmPropsd', type=Max35Text, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='CstmrCnsnt', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CstmrOrdr', type=CustomerOrder1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CstmrTkn', type=CardPaymentToken5, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IssrCITId', type=Max140Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IssrRefData', type=Max140Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LastTxFlg', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MrchntCITId', type=Max140Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MrchntCtgyCd', type=Min3Max4Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MrchntRefData', type=Max70Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlTx', type=CardPaymentTransaction131, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PmtInstrm', type=PaymentInstrumentType2Code, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='PmtTpInf', type=PaymentTypeInformation26, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RcncltnId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SaleRefId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SaleToAcqrrData', type=Max70Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SaleToIssrData', type=Max70Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SaleToPOIData', type=Max70Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SvcAttr', type=CardPaymentServiceType15Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxCaptr', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxDtls', type=CardPaymentTransactionDetails53, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxId', type=TransactionIdentifier1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxTp', type=CardPaymentServiceType16Code, min=1, max=1, mutex_group=None, array=False),
	))