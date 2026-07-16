# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AuthorisationResult18
from . import CardAccount16
from . import CardPaymentServiceType12Code
from . import CardPaymentServiceType15Code
from . import CardPaymentServiceType9Code
from . import CardPaymentTransaction138
from . import CardPaymentTransactionDetails53
from . import FailureReason3Code
from . import Max140Text
from . import Max35Text
from . import Max70Text
from . import Min3Max4Text
from . import TransactionIdentifier1
from . import TrueFalseIndicator

class CardPaymentTransaction140(base_types._BaseFieldType):

	__slots__ = ["_AcctFr", "_AcctTo", "_AddtlSvc", "_AddtlTxData", "_AuthstnRslt", "_CardPrgrmmApld", "_CardPrgrmmPropsd", "_CstmrCnsnt", "_FailrRsn", "_InitrTxId", "_IntrchngData", "_IssrCITId", "_LastTxFlg", "_MrchntCITId", "_MrchntCtgyCd", "_MrchntOvrrd", "_MrchntRefData", "_OrgnlTx", "_RcncltnId", "_RcptTxId", "_Rvsl", "_SaleRefId", "_SvcAttr", "_TxCaptr", "_TxDtls", "_TxId", "_TxSucss", "_TxTp"]
	@property
	def AcctFr(self):
		return self._AcctFr

	@AcctFr.setter
	def AcctFr(self, value):
		self._AcctFr = value if value is not None else base_types.UninitialisedField(self, 'AcctFr', CardAccount16, False)

	@AcctFr.deleter
	def AcctFr(self):
		del self._AcctFr
		self._AcctFr = base_types.UninitialisedField(self, 'AcctFr', CardAccount16, False)

	@property
	def AcctTo(self):
		return self._AcctTo

	@AcctTo.setter
	def AcctTo(self, value):
		self._AcctTo = value if value is not None else base_types.UninitialisedField(self, 'AcctTo', CardAccount16, False)

	@AcctTo.deleter
	def AcctTo(self):
		del self._AcctTo
		self._AcctTo = base_types.UninitialisedField(self, 'AcctTo', CardAccount16, False)

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
	def FailrRsn(self):
		return self._FailrRsn

	@FailrRsn.setter
	def FailrRsn(self, value):
		self._FailrRsn = value if value is not None else base_types.UninitialisedField(self, 'FailrRsn', FailureReason3Code, True)

	@FailrRsn.deleter
	def FailrRsn(self):
		del self._FailrRsn
		self._FailrRsn = base_types.UninitialisedField(self, 'FailrRsn', FailureReason3Code, True)

	@property
	def InitrTxId(self):
		return self._InitrTxId

	@InitrTxId.setter
	def InitrTxId(self, value):
		self._InitrTxId = value if value is not None else base_types.UninitialisedField(self, 'InitrTxId', Max35Text, False)

	@InitrTxId.deleter
	def InitrTxId(self):
		del self._InitrTxId
		self._InitrTxId = base_types.UninitialisedField(self, 'InitrTxId', Max35Text, False)

	@property
	def IntrchngData(self):
		return self._IntrchngData

	@IntrchngData.setter
	def IntrchngData(self, value):
		self._IntrchngData = value if value is not None else base_types.UninitialisedField(self, 'IntrchngData', Max140Text, False)

	@IntrchngData.deleter
	def IntrchngData(self):
		del self._IntrchngData
		self._IntrchngData = base_types.UninitialisedField(self, 'IntrchngData', Max140Text, False)

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
	def MrchntOvrrd(self):
		return self._MrchntOvrrd

	@MrchntOvrrd.setter
	def MrchntOvrrd(self, value):
		self._MrchntOvrrd = value if value is not None else base_types.UninitialisedField(self, 'MrchntOvrrd', TrueFalseIndicator, False)

	@MrchntOvrrd.deleter
	def MrchntOvrrd(self):
		del self._MrchntOvrrd
		self._MrchntOvrrd = base_types.UninitialisedField(self, 'MrchntOvrrd', TrueFalseIndicator, False)

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
		self._OrgnlTx = value if value is not None else base_types.UninitialisedField(self, 'OrgnlTx', CardPaymentTransaction138, False)

	@OrgnlTx.deleter
	def OrgnlTx(self):
		del self._OrgnlTx
		self._OrgnlTx = base_types.UninitialisedField(self, 'OrgnlTx', CardPaymentTransaction138, False)

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
	def RcptTxId(self):
		return self._RcptTxId

	@RcptTxId.setter
	def RcptTxId(self, value):
		self._RcptTxId = value if value is not None else base_types.UninitialisedField(self, 'RcptTxId', Max140Text, False)

	@RcptTxId.deleter
	def RcptTxId(self):
		del self._RcptTxId
		self._RcptTxId = base_types.UninitialisedField(self, 'RcptTxId', Max140Text, False)

	@property
	def Rvsl(self):
		return self._Rvsl

	@Rvsl.setter
	def Rvsl(self, value):
		self._Rvsl = value if value is not None else base_types.UninitialisedField(self, 'Rvsl', TrueFalseIndicator, False)

	@Rvsl.deleter
	def Rvsl(self):
		del self._Rvsl
		self._Rvsl = base_types.UninitialisedField(self, 'Rvsl', TrueFalseIndicator, False)

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
	def TxSucss(self):
		return self._TxSucss

	@TxSucss.setter
	def TxSucss(self, value):
		self._TxSucss = value if value is not None else base_types.UninitialisedField(self, 'TxSucss', TrueFalseIndicator, False)

	@TxSucss.deleter
	def TxSucss(self):
		del self._TxSucss
		self._TxSucss = base_types.UninitialisedField(self, 'TxSucss', TrueFalseIndicator, False)

	@property
	def TxTp(self):
		return self._TxTp

	@TxTp.setter
	def TxTp(self, value):
		self._TxTp = value if value is not None else base_types.UninitialisedField(self, 'TxTp', CardPaymentServiceType12Code, False)

	@TxTp.deleter
	def TxTp(self):
		del self._TxTp
		self._TxTp = base_types.UninitialisedField(self, 'TxTp', CardPaymentServiceType12Code, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AcctFr', type=CardAccount16, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AcctTo', type=CardAccount16, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AddtlSvc', type=CardPaymentServiceType9Code, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='AddtlTxData', type=Max70Text, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='AuthstnRslt', type=AuthorisationResult18, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CardPrgrmmApld', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CardPrgrmmPropsd', type=Max35Text, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='CstmrCnsnt', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FailrRsn', type=FailureReason3Code, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='InitrTxId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IntrchngData', type=Max140Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IssrCITId', type=Max140Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LastTxFlg', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MrchntCITId', type=Max140Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MrchntCtgyCd', type=Min3Max4Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MrchntOvrrd', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MrchntRefData', type=Max70Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlTx', type=CardPaymentTransaction138, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RcncltnId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RcptTxId', type=Max140Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Rvsl', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SaleRefId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SvcAttr', type=CardPaymentServiceType15Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxCaptr', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxDtls', type=CardPaymentTransactionDetails53, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxId', type=TransactionIdentifier1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxSucss', type=TrueFalseIndicator, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxTp', type=CardPaymentServiceType12Code, min=0, max=1, mutex_group=None, array=False),
	))