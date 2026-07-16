# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActiveCurrencyCode
from . import AggregationTransaction3
from . import CardAccountType3Code
from . import CurrencyConversion30
from . import DetailedAmount15
from . import ExternallyDefinedData5
from . import ISODate
from . import ImpliedCurrencyAndAmount
from . import Instalment5
from . import Max10000Binary
from . import Max10Text
from . import Max35NumericText
from . import Max35Text
from . import OnLineReason2Code
from . import PositiveNumber
from . import Product6
from . import RecurringTransaction6
from . import TypeOfAmount8Code

class CardPaymentTransactionDetails53(base_types._BaseFieldType):

	__slots__ = ["_AcctTp", "_AddtlInf", "_AggtnTx", "_AmtQlfr", "_AuthrsdAmt", "_Ccy", "_CcyConvsRslt", "_CmltvAmt", "_CmpltnSeqCntr", "_CmpltnSeqNb", "_DlvryLctn", "_DtldAmt", "_ICCRltdData", "_Instlmt", "_InvcAmt", "_OnLineRsn", "_PdctCdSetId", "_Rcrng", "_ReSubmissnCntr", "_ReqdAmt", "_SaleItm", "_TtlAmt", "_TtlAuthrsdAmt", "_UattnddLvlCtgy", "_VldtyDt"]
	@property
	def AcctTp(self):
		return self._AcctTp

	@AcctTp.setter
	def AcctTp(self, value):
		self._AcctTp = value if value is not None else base_types.UninitialisedField(self, 'AcctTp', CardAccountType3Code, False)

	@AcctTp.deleter
	def AcctTp(self):
		del self._AcctTp
		self._AcctTp = base_types.UninitialisedField(self, 'AcctTp', CardAccountType3Code, False)

	@property
	def AddtlInf(self):
		return self._AddtlInf

	@AddtlInf.setter
	def AddtlInf(self, value):
		self._AddtlInf = value if value is not None else base_types.UninitialisedField(self, 'AddtlInf', ExternallyDefinedData5, True)

	@AddtlInf.deleter
	def AddtlInf(self):
		del self._AddtlInf
		self._AddtlInf = base_types.UninitialisedField(self, 'AddtlInf', ExternallyDefinedData5, True)

	@property
	def AggtnTx(self):
		return self._AggtnTx

	@AggtnTx.setter
	def AggtnTx(self, value):
		self._AggtnTx = value if value is not None else base_types.UninitialisedField(self, 'AggtnTx', AggregationTransaction3, False)

	@AggtnTx.deleter
	def AggtnTx(self):
		del self._AggtnTx
		self._AggtnTx = base_types.UninitialisedField(self, 'AggtnTx', AggregationTransaction3, False)

	@property
	def AmtQlfr(self):
		return self._AmtQlfr

	@AmtQlfr.setter
	def AmtQlfr(self, value):
		self._AmtQlfr = value if value is not None else base_types.UninitialisedField(self, 'AmtQlfr', TypeOfAmount8Code, False)

	@AmtQlfr.deleter
	def AmtQlfr(self):
		del self._AmtQlfr
		self._AmtQlfr = base_types.UninitialisedField(self, 'AmtQlfr', TypeOfAmount8Code, False)

	@property
	def AuthrsdAmt(self):
		return self._AuthrsdAmt

	@AuthrsdAmt.setter
	def AuthrsdAmt(self, value):
		self._AuthrsdAmt = value if value is not None else base_types.UninitialisedField(self, 'AuthrsdAmt', ImpliedCurrencyAndAmount, False)

	@AuthrsdAmt.deleter
	def AuthrsdAmt(self):
		del self._AuthrsdAmt
		self._AuthrsdAmt = base_types.UninitialisedField(self, 'AuthrsdAmt', ImpliedCurrencyAndAmount, False)

	@property
	def Ccy(self):
		return self._Ccy

	@Ccy.setter
	def Ccy(self, value):
		self._Ccy = value if value is not None else base_types.UninitialisedField(self, 'Ccy', ActiveCurrencyCode, False)

	@Ccy.deleter
	def Ccy(self):
		del self._Ccy
		self._Ccy = base_types.UninitialisedField(self, 'Ccy', ActiveCurrencyCode, False)

	@property
	def CcyConvsRslt(self):
		return self._CcyConvsRslt

	@CcyConvsRslt.setter
	def CcyConvsRslt(self, value):
		self._CcyConvsRslt = value if value is not None else base_types.UninitialisedField(self, 'CcyConvsRslt', CurrencyConversion30, False)

	@CcyConvsRslt.deleter
	def CcyConvsRslt(self):
		del self._CcyConvsRslt
		self._CcyConvsRslt = base_types.UninitialisedField(self, 'CcyConvsRslt', CurrencyConversion30, False)

	@property
	def CmltvAmt(self):
		return self._CmltvAmt

	@CmltvAmt.setter
	def CmltvAmt(self, value):
		self._CmltvAmt = value if value is not None else base_types.UninitialisedField(self, 'CmltvAmt', ImpliedCurrencyAndAmount, False)

	@CmltvAmt.deleter
	def CmltvAmt(self):
		del self._CmltvAmt
		self._CmltvAmt = base_types.UninitialisedField(self, 'CmltvAmt', ImpliedCurrencyAndAmount, False)

	@property
	def CmpltnSeqCntr(self):
		return self._CmpltnSeqCntr

	@CmpltnSeqCntr.setter
	def CmpltnSeqCntr(self, value):
		self._CmpltnSeqCntr = value if value is not None else base_types.UninitialisedField(self, 'CmpltnSeqCntr', PositiveNumber, False)

	@CmpltnSeqCntr.deleter
	def CmpltnSeqCntr(self):
		del self._CmpltnSeqCntr
		self._CmpltnSeqCntr = base_types.UninitialisedField(self, 'CmpltnSeqCntr', PositiveNumber, False)

	@property
	def CmpltnSeqNb(self):
		return self._CmpltnSeqNb

	@CmpltnSeqNb.setter
	def CmpltnSeqNb(self, value):
		self._CmpltnSeqNb = value if value is not None else base_types.UninitialisedField(self, 'CmpltnSeqNb', PositiveNumber, False)

	@CmpltnSeqNb.deleter
	def CmpltnSeqNb(self):
		del self._CmpltnSeqNb
		self._CmpltnSeqNb = base_types.UninitialisedField(self, 'CmpltnSeqNb', PositiveNumber, False)

	@property
	def DlvryLctn(self):
		return self._DlvryLctn

	@DlvryLctn.setter
	def DlvryLctn(self, value):
		self._DlvryLctn = value if value is not None else base_types.UninitialisedField(self, 'DlvryLctn', Max35Text, False)

	@DlvryLctn.deleter
	def DlvryLctn(self):
		del self._DlvryLctn
		self._DlvryLctn = base_types.UninitialisedField(self, 'DlvryLctn', Max35Text, False)

	@property
	def DtldAmt(self):
		return self._DtldAmt

	@DtldAmt.setter
	def DtldAmt(self, value):
		self._DtldAmt = value if value is not None else base_types.UninitialisedField(self, 'DtldAmt', DetailedAmount15, False)

	@DtldAmt.deleter
	def DtldAmt(self):
		del self._DtldAmt
		self._DtldAmt = base_types.UninitialisedField(self, 'DtldAmt', DetailedAmount15, False)

	@property
	def ICCRltdData(self):
		return self._ICCRltdData

	@ICCRltdData.setter
	def ICCRltdData(self, value):
		self._ICCRltdData = value if value is not None else base_types.UninitialisedField(self, 'ICCRltdData', Max10000Binary, False)

	@ICCRltdData.deleter
	def ICCRltdData(self):
		del self._ICCRltdData
		self._ICCRltdData = base_types.UninitialisedField(self, 'ICCRltdData', Max10000Binary, False)

	@property
	def Instlmt(self):
		return self._Instlmt

	@Instlmt.setter
	def Instlmt(self, value):
		self._Instlmt = value if value is not None else base_types.UninitialisedField(self, 'Instlmt', Instalment5, True)

	@Instlmt.deleter
	def Instlmt(self):
		del self._Instlmt
		self._Instlmt = base_types.UninitialisedField(self, 'Instlmt', Instalment5, True)

	@property
	def InvcAmt(self):
		return self._InvcAmt

	@InvcAmt.setter
	def InvcAmt(self, value):
		self._InvcAmt = value if value is not None else base_types.UninitialisedField(self, 'InvcAmt', ImpliedCurrencyAndAmount, False)

	@InvcAmt.deleter
	def InvcAmt(self):
		del self._InvcAmt
		self._InvcAmt = base_types.UninitialisedField(self, 'InvcAmt', ImpliedCurrencyAndAmount, False)

	@property
	def OnLineRsn(self):
		return self._OnLineRsn

	@OnLineRsn.setter
	def OnLineRsn(self, value):
		self._OnLineRsn = value if value is not None else base_types.UninitialisedField(self, 'OnLineRsn', OnLineReason2Code, True)

	@OnLineRsn.deleter
	def OnLineRsn(self):
		del self._OnLineRsn
		self._OnLineRsn = base_types.UninitialisedField(self, 'OnLineRsn', OnLineReason2Code, True)

	@property
	def PdctCdSetId(self):
		return self._PdctCdSetId

	@PdctCdSetId.setter
	def PdctCdSetId(self, value):
		self._PdctCdSetId = value if value is not None else base_types.UninitialisedField(self, 'PdctCdSetId', Max10Text, False)

	@PdctCdSetId.deleter
	def PdctCdSetId(self):
		del self._PdctCdSetId
		self._PdctCdSetId = base_types.UninitialisedField(self, 'PdctCdSetId', Max10Text, False)

	@property
	def Rcrng(self):
		return self._Rcrng

	@Rcrng.setter
	def Rcrng(self, value):
		self._Rcrng = value if value is not None else base_types.UninitialisedField(self, 'Rcrng', RecurringTransaction6, False)

	@Rcrng.deleter
	def Rcrng(self):
		del self._Rcrng
		self._Rcrng = base_types.UninitialisedField(self, 'Rcrng', RecurringTransaction6, False)

	@property
	def ReSubmissnCntr(self):
		return self._ReSubmissnCntr

	@ReSubmissnCntr.setter
	def ReSubmissnCntr(self, value):
		self._ReSubmissnCntr = value if value is not None else base_types.UninitialisedField(self, 'ReSubmissnCntr', PositiveNumber, False)

	@ReSubmissnCntr.deleter
	def ReSubmissnCntr(self):
		del self._ReSubmissnCntr
		self._ReSubmissnCntr = base_types.UninitialisedField(self, 'ReSubmissnCntr', PositiveNumber, False)

	@property
	def ReqdAmt(self):
		return self._ReqdAmt

	@ReqdAmt.setter
	def ReqdAmt(self, value):
		self._ReqdAmt = value if value is not None else base_types.UninitialisedField(self, 'ReqdAmt', ImpliedCurrencyAndAmount, False)

	@ReqdAmt.deleter
	def ReqdAmt(self):
		del self._ReqdAmt
		self._ReqdAmt = base_types.UninitialisedField(self, 'ReqdAmt', ImpliedCurrencyAndAmount, False)

	@property
	def SaleItm(self):
		return self._SaleItm

	@SaleItm.setter
	def SaleItm(self, value):
		self._SaleItm = value if value is not None else base_types.UninitialisedField(self, 'SaleItm', Product6, True)

	@SaleItm.deleter
	def SaleItm(self):
		del self._SaleItm
		self._SaleItm = base_types.UninitialisedField(self, 'SaleItm', Product6, True)

	@property
	def TtlAmt(self):
		return self._TtlAmt

	@TtlAmt.setter
	def TtlAmt(self, value):
		self._TtlAmt = value if value is not None else base_types.UninitialisedField(self, 'TtlAmt', ImpliedCurrencyAndAmount, False)

	@TtlAmt.deleter
	def TtlAmt(self):
		del self._TtlAmt
		self._TtlAmt = base_types.UninitialisedField(self, 'TtlAmt', ImpliedCurrencyAndAmount, False)

	@property
	def TtlAuthrsdAmt(self):
		return self._TtlAuthrsdAmt

	@TtlAuthrsdAmt.setter
	def TtlAuthrsdAmt(self, value):
		self._TtlAuthrsdAmt = value if value is not None else base_types.UninitialisedField(self, 'TtlAuthrsdAmt', ImpliedCurrencyAndAmount, False)

	@TtlAuthrsdAmt.deleter
	def TtlAuthrsdAmt(self):
		del self._TtlAuthrsdAmt
		self._TtlAuthrsdAmt = base_types.UninitialisedField(self, 'TtlAuthrsdAmt', ImpliedCurrencyAndAmount, False)

	@property
	def UattnddLvlCtgy(self):
		return self._UattnddLvlCtgy

	@UattnddLvlCtgy.setter
	def UattnddLvlCtgy(self, value):
		self._UattnddLvlCtgy = value if value is not None else base_types.UninitialisedField(self, 'UattnddLvlCtgy', Max35NumericText, False)

	@UattnddLvlCtgy.deleter
	def UattnddLvlCtgy(self):
		del self._UattnddLvlCtgy
		self._UattnddLvlCtgy = base_types.UninitialisedField(self, 'UattnddLvlCtgy', Max35NumericText, False)

	@property
	def VldtyDt(self):
		return self._VldtyDt

	@VldtyDt.setter
	def VldtyDt(self, value):
		self._VldtyDt = value if value is not None else base_types.UninitialisedField(self, 'VldtyDt', ISODate, False)

	@VldtyDt.deleter
	def VldtyDt(self):
		del self._VldtyDt
		self._VldtyDt = base_types.UninitialisedField(self, 'VldtyDt', ISODate, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AcctTp', type=CardAccountType3Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AddtlInf', type=ExternallyDefinedData5, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='AggtnTx', type=AggregationTransaction3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AmtQlfr', type=TypeOfAmount8Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AuthrsdAmt', type=ImpliedCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Ccy', type=ActiveCurrencyCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CcyConvsRslt', type=CurrencyConversion30, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CmltvAmt', type=ImpliedCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CmpltnSeqCntr', type=PositiveNumber, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CmpltnSeqNb', type=PositiveNumber, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DlvryLctn', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DtldAmt', type=DetailedAmount15, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ICCRltdData', type=Max10000Binary, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Instlmt', type=Instalment5, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='InvcAmt', type=ImpliedCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OnLineRsn', type=OnLineReason2Code, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='PdctCdSetId', type=Max10Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Rcrng', type=RecurringTransaction6, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ReSubmissnCntr', type=PositiveNumber, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ReqdAmt', type=ImpliedCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SaleItm', type=Product6, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='TtlAmt', type=ImpliedCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlAuthrsdAmt', type=ImpliedCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UattnddLvlCtgy', type=Max35NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='VldtyDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
	))