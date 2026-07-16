# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AuthorisationResult18
from . import CardPaymentServiceType15Code
from . import CardPaymentServiceType16Code
from . import CardPaymentServiceType9Code
from . import CardPaymentToken5
from . import CardPaymentTransaction131
from . import CardPaymentTransactionDetails53
from . import CustomerOrder1
from . import Max140Text
from . import Max35Text
from . import Max70Text
from . import Min3Max4Text
from . import PaymentInstrumentType2Code
from . import PaymentTypeInformation26
from . import TransactionIdentifier1
from . import TrueFalseIndicator

class PaymentTransaction165(base_types._BaseFieldType):

	__slots__ = ["_AddtlSvc", "_AddtlTxData", "_AuthstnRslt", "_CardPrgrmmApld", "_CardPrgrmmPropsd", "_CstmrCnsnt", "_CstmrOrdr", "_CstmrTkn", "_IssrCITId", "_IssrRefData", "_LastTxFlg", "_MrchntCITId", "_MrchntCtgyCd", "_MrchntRefData", "_OrgnlTx", "_PmtInstrm", "_PmtTpInf", "_RcncltnId", "_SaleRefId", "_SaleToAcqrrData", "_SaleToIssrData", "_SaleToPOIData", "_SvcAttr", "_TxCaptr", "_TxDtls", "_TxId", "_TxTp"]
	@property
	def AddtlSvc(self):
		return self._AddtlSvc

	@AddtlSvc.setter
	def AddtlSvc(self, value):
		self._AddtlSvc = value if value is not None else base_types.UninitialisedField(self, 'AddtlSvc', CardPaymentServiceType9Code, True)

	@AddtlSvc.deleter
	def AddtlSvc(self):
		del self._AddtlSvc
		self._AddtlSvc = base_types.UninitialisedField(self, 'AddtlSvc', CardPaymentServiceType9Code, True)

	@property
	def AddtlTxData(self):
		return self._AddtlTxData

	@AddtlTxData.setter
	def AddtlTxData(self, value):
		self._AddtlTxData = value if value is not None else base_types.UninitialisedField(self, 'AddtlTxData', Max70Text, True)

	@AddtlTxData.deleter
	def AddtlTxData(self):
		del self._AddtlTxData
		self._AddtlTxData = base_types.UninitialisedField(self, 'AddtlTxData', Max70Text, True)

	@property
	def AuthstnRslt(self):
		return self._AuthstnRslt

	@AuthstnRslt.setter
	def AuthstnRslt(self, value):
		self._AuthstnRslt = value if value is not None else base_types.UninitialisedField(self, 'AuthstnRslt', AuthorisationResult18, False)

	@AuthstnRslt.deleter
	def AuthstnRslt(self):
		del self._AuthstnRslt
		self._AuthstnRslt = base_types.UninitialisedField(self, 'AuthstnRslt', AuthorisationResult18, False)

	@property
	def CardPrgrmmApld(self):
		return self._CardPrgrmmApld

	@CardPrgrmmApld.setter
	def CardPrgrmmApld(self, value):
		self._CardPrgrmmApld = value if value is not None else base_types.UninitialisedField(self, 'CardPrgrmmApld', Max35Text, False)

	@CardPrgrmmApld.deleter
	def CardPrgrmmApld(self):
		del self._CardPrgrmmApld
		self._CardPrgrmmApld = base_types.UninitialisedField(self, 'CardPrgrmmApld', Max35Text, False)

	@property
	def CardPrgrmmPropsd(self):
		return self._CardPrgrmmPropsd

	@CardPrgrmmPropsd.setter
	def CardPrgrmmPropsd(self, value):
		self._CardPrgrmmPropsd = value if value is not None else base_types.UninitialisedField(self, 'CardPrgrmmPropsd', Max35Text, True)

	@CardPrgrmmPropsd.deleter
	def CardPrgrmmPropsd(self):
		del self._CardPrgrmmPropsd
		self._CardPrgrmmPropsd = base_types.UninitialisedField(self, 'CardPrgrmmPropsd', Max35Text, True)

	@property
	def CstmrCnsnt(self):
		return self._CstmrCnsnt

	@CstmrCnsnt.setter
	def CstmrCnsnt(self, value):
		self._CstmrCnsnt = value if value is not None else base_types.UninitialisedField(self, 'CstmrCnsnt', TrueFalseIndicator, False)

	@CstmrCnsnt.deleter
	def CstmrCnsnt(self):
		del self._CstmrCnsnt
		self._CstmrCnsnt = base_types.UninitialisedField(self, 'CstmrCnsnt', TrueFalseIndicator, False)

	@property
	def CstmrOrdr(self):
		return self._CstmrOrdr

	@CstmrOrdr.setter
	def CstmrOrdr(self, value):
		self._CstmrOrdr = value if value is not None else base_types.UninitialisedField(self, 'CstmrOrdr', CustomerOrder1, False)

	@CstmrOrdr.deleter
	def CstmrOrdr(self):
		del self._CstmrOrdr
		self._CstmrOrdr = base_types.UninitialisedField(self, 'CstmrOrdr', CustomerOrder1, False)

	@property
	def CstmrTkn(self):
		return self._CstmrTkn

	@CstmrTkn.setter
	def CstmrTkn(self, value):
		self._CstmrTkn = value if value is not None else base_types.UninitialisedField(self, 'CstmrTkn', CardPaymentToken5, False)

	@CstmrTkn.deleter
	def CstmrTkn(self):
		del self._CstmrTkn
		self._CstmrTkn = base_types.UninitialisedField(self, 'CstmrTkn', CardPaymentToken5, False)

	@property
	def IssrCITId(self):
		return self._IssrCITId

	@IssrCITId.setter
	def IssrCITId(self, value):
		self._IssrCITId = value if value is not None else base_types.UninitialisedField(self, 'IssrCITId', Max140Text, False)

	@IssrCITId.deleter
	def IssrCITId(self):
		del self._IssrCITId
		self._IssrCITId = base_types.UninitialisedField(self, 'IssrCITId', Max140Text, False)

	@property
	def IssrRefData(self):
		return self._IssrRefData

	@IssrRefData.setter
	def IssrRefData(self, value):
		self._IssrRefData = value if value is not None else base_types.UninitialisedField(self, 'IssrRefData', Max140Text, False)

	@IssrRefData.deleter
	def IssrRefData(self):
		del self._IssrRefData
		self._IssrRefData = base_types.UninitialisedField(self, 'IssrRefData', Max140Text, False)

	@property
	def LastTxFlg(self):
		return self._LastTxFlg

	@LastTxFlg.setter
	def LastTxFlg(self, value):
		self._LastTxFlg = value if value is not None else base_types.UninitialisedField(self, 'LastTxFlg', TrueFalseIndicator, False)

	@LastTxFlg.deleter
	def LastTxFlg(self):
		del self._LastTxFlg
		self._LastTxFlg = base_types.UninitialisedField(self, 'LastTxFlg', TrueFalseIndicator, False)

	@property
	def MrchntCITId(self):
		return self._MrchntCITId

	@MrchntCITId.setter
	def MrchntCITId(self, value):
		self._MrchntCITId = value if value is not None else base_types.UninitialisedField(self, 'MrchntCITId', Max140Text, False)

	@MrchntCITId.deleter
	def MrchntCITId(self):
		del self._MrchntCITId
		self._MrchntCITId = base_types.UninitialisedField(self, 'MrchntCITId', Max140Text, False)

	@property
	def MrchntCtgyCd(self):
		return self._MrchntCtgyCd

	@MrchntCtgyCd.setter
	def MrchntCtgyCd(self, value):
		self._MrchntCtgyCd = value if value is not None else base_types.UninitialisedField(self, 'MrchntCtgyCd', Min3Max4Text, False)

	@MrchntCtgyCd.deleter
	def MrchntCtgyCd(self):
		del self._MrchntCtgyCd
		self._MrchntCtgyCd = base_types.UninitialisedField(self, 'MrchntCtgyCd', Min3Max4Text, False)

	@property
	def MrchntRefData(self):
		return self._MrchntRefData

	@MrchntRefData.setter
	def MrchntRefData(self, value):
		self._MrchntRefData = value if value is not None else base_types.UninitialisedField(self, 'MrchntRefData', Max70Text, False)

	@MrchntRefData.deleter
	def MrchntRefData(self):
		del self._MrchntRefData
		self._MrchntRefData = base_types.UninitialisedField(self, 'MrchntRefData', Max70Text, False)

	@property
	def OrgnlTx(self):
		return self._OrgnlTx

	@OrgnlTx.setter
	def OrgnlTx(self, value):
		self._OrgnlTx = value if value is not None else base_types.UninitialisedField(self, 'OrgnlTx', CardPaymentTransaction131, False)

	@OrgnlTx.deleter
	def OrgnlTx(self):
		del self._OrgnlTx
		self._OrgnlTx = base_types.UninitialisedField(self, 'OrgnlTx', CardPaymentTransaction131, False)

	@property
	def PmtInstrm(self):
		return self._PmtInstrm

	@PmtInstrm.setter
	def PmtInstrm(self, value):
		self._PmtInstrm = value if value is not None else base_types.UninitialisedField(self, 'PmtInstrm', PaymentInstrumentType2Code, True)

	@PmtInstrm.deleter
	def PmtInstrm(self):
		del self._PmtInstrm
		self._PmtInstrm = base_types.UninitialisedField(self, 'PmtInstrm', PaymentInstrumentType2Code, True)

	@property
	def PmtTpInf(self):
		return self._PmtTpInf

	@PmtTpInf.setter
	def PmtTpInf(self, value):
		self._PmtTpInf = value if value is not None else base_types.UninitialisedField(self, 'PmtTpInf', PaymentTypeInformation26, False)

	@PmtTpInf.deleter
	def PmtTpInf(self):
		del self._PmtTpInf
		self._PmtTpInf = base_types.UninitialisedField(self, 'PmtTpInf', PaymentTypeInformation26, False)

	@property
	def RcncltnId(self):
		return self._RcncltnId

	@RcncltnId.setter
	def RcncltnId(self, value):
		self._RcncltnId = value if value is not None else base_types.UninitialisedField(self, 'RcncltnId', Max35Text, False)

	@RcncltnId.deleter
	def RcncltnId(self):
		del self._RcncltnId
		self._RcncltnId = base_types.UninitialisedField(self, 'RcncltnId', Max35Text, False)

	@property
	def SaleRefId(self):
		return self._SaleRefId

	@SaleRefId.setter
	def SaleRefId(self, value):
		self._SaleRefId = value if value is not None else base_types.UninitialisedField(self, 'SaleRefId', Max35Text, False)

	@SaleRefId.deleter
	def SaleRefId(self):
		del self._SaleRefId
		self._SaleRefId = base_types.UninitialisedField(self, 'SaleRefId', Max35Text, False)

	@property
	def SaleToAcqrrData(self):
		return self._SaleToAcqrrData

	@SaleToAcqrrData.setter
	def SaleToAcqrrData(self, value):
		self._SaleToAcqrrData = value if value is not None else base_types.UninitialisedField(self, 'SaleToAcqrrData', Max70Text, False)

	@SaleToAcqrrData.deleter
	def SaleToAcqrrData(self):
		del self._SaleToAcqrrData
		self._SaleToAcqrrData = base_types.UninitialisedField(self, 'SaleToAcqrrData', Max70Text, False)

	@property
	def SaleToIssrData(self):
		return self._SaleToIssrData

	@SaleToIssrData.setter
	def SaleToIssrData(self, value):
		self._SaleToIssrData = value if value is not None else base_types.UninitialisedField(self, 'SaleToIssrData', Max70Text, False)

	@SaleToIssrData.deleter
	def SaleToIssrData(self):
		del self._SaleToIssrData
		self._SaleToIssrData = base_types.UninitialisedField(self, 'SaleToIssrData', Max70Text, False)

	@property
	def SaleToPOIData(self):
		return self._SaleToPOIData

	@SaleToPOIData.setter
	def SaleToPOIData(self, value):
		self._SaleToPOIData = value if value is not None else base_types.UninitialisedField(self, 'SaleToPOIData', Max70Text, False)

	@SaleToPOIData.deleter
	def SaleToPOIData(self):
		del self._SaleToPOIData
		self._SaleToPOIData = base_types.UninitialisedField(self, 'SaleToPOIData', Max70Text, False)

	@property
	def SvcAttr(self):
		return self._SvcAttr

	@SvcAttr.setter
	def SvcAttr(self, value):
		self._SvcAttr = value if value is not None else base_types.UninitialisedField(self, 'SvcAttr', CardPaymentServiceType15Code, False)

	@SvcAttr.deleter
	def SvcAttr(self):
		del self._SvcAttr
		self._SvcAttr = base_types.UninitialisedField(self, 'SvcAttr', CardPaymentServiceType15Code, False)

	@property
	def TxCaptr(self):
		return self._TxCaptr

	@TxCaptr.setter
	def TxCaptr(self, value):
		self._TxCaptr = value if value is not None else base_types.UninitialisedField(self, 'TxCaptr', TrueFalseIndicator, False)

	@TxCaptr.deleter
	def TxCaptr(self):
		del self._TxCaptr
		self._TxCaptr = base_types.UninitialisedField(self, 'TxCaptr', TrueFalseIndicator, False)

	@property
	def TxDtls(self):
		return self._TxDtls

	@TxDtls.setter
	def TxDtls(self, value):
		self._TxDtls = value if value is not None else base_types.UninitialisedField(self, 'TxDtls', CardPaymentTransactionDetails53, False)

	@TxDtls.deleter
	def TxDtls(self):
		del self._TxDtls
		self._TxDtls = base_types.UninitialisedField(self, 'TxDtls', CardPaymentTransactionDetails53, False)

	@property
	def TxId(self):
		return self._TxId

	@TxId.setter
	def TxId(self, value):
		self._TxId = value if value is not None else base_types.UninitialisedField(self, 'TxId', TransactionIdentifier1, False)

	@TxId.deleter
	def TxId(self):
		del self._TxId
		self._TxId = base_types.UninitialisedField(self, 'TxId', TransactionIdentifier1, False)

	@property
	def TxTp(self):
		return self._TxTp

	@TxTp.setter
	def TxTp(self, value):
		self._TxTp = value if value is not None else base_types.UninitialisedField(self, 'TxTp', CardPaymentServiceType16Code, False)

	@TxTp.deleter
	def TxTp(self):
		del self._TxTp
		self._TxTp = base_types.UninitialisedField(self, 'TxTp', CardPaymentServiceType16Code, False)

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