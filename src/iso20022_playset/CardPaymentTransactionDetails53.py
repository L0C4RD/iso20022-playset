from . import base_types
import ISODate
import Max10Text
import TypeOfAmount8Code
import Max35Text
import ActiveCurrencyCode
import CurrencyConversion30
import PositiveNumber
import ImpliedCurrencyAndAmount
import ExternallyDefinedData5
import CardAccountType3Code
import Product6
import Max10000Binary
import Instalment5
import AggregationTransaction3
import RecurringTransaction6
import DetailedAmount15
import Max35NumericText
import OnLineReason2Code

class CardPaymentTransactionDetails53(base_types._BaseFieldType):

	__slots__ = ["_AcctTp", "_CmltvAmt", "_DtldAmt", "_Ccy", "_TtlAmt", "_InvcAmt", "_ReqdAmt", "_VldtyDt", "_UattnddLvlCtgy", "_PdctCdSetId", "_AmtQlfr", "_Rcrng", "_AggtnTx", "_AddtlInf", "_CcyConvsRslt", "_CmpltnSeqNb", "_SaleItm", "_AuthrsdAmt", "_ReSubmissnCntr", "_TtlAuthrsdAmt", "_OnLineRsn", "_DlvryLctn", "_Instlmt", "_ICCRltdData", "_CmpltnSeqCntr"]
	@property
	def AcctTp(self):
		return self._AcctTp

	@AcctTp.setter
	def AcctTp(self, value):
		self._AcctTp = value if type(value) != auto else self.make_default("AcctTp")

	@AcctTp.deleter
	def AcctTp(self):
		del self._AcctTp
		self._AcctTp = None

	@property
	def CmltvAmt(self):
		return self._CmltvAmt

	@CmltvAmt.setter
	def CmltvAmt(self, value):
		self._CmltvAmt = value if type(value) != auto else self.make_default("CmltvAmt")

	@CmltvAmt.deleter
	def CmltvAmt(self):
		del self._CmltvAmt
		self._CmltvAmt = None

	@property
	def DtldAmt(self):
		return self._DtldAmt

	@DtldAmt.setter
	def DtldAmt(self, value):
		self._DtldAmt = value if type(value) != auto else self.make_default("DtldAmt")

	@DtldAmt.deleter
	def DtldAmt(self):
		del self._DtldAmt
		self._DtldAmt = None

	@property
	def Ccy(self):
		return self._Ccy

	@Ccy.setter
	def Ccy(self, value):
		self._Ccy = value if type(value) != auto else self.make_default("Ccy")

	@Ccy.deleter
	def Ccy(self):
		del self._Ccy
		self._Ccy = None

	@property
	def TtlAmt(self):
		return self._TtlAmt

	@TtlAmt.setter
	def TtlAmt(self, value):
		self._TtlAmt = value if type(value) != auto else self.make_default("TtlAmt")

	@TtlAmt.deleter
	def TtlAmt(self):
		del self._TtlAmt
		self._TtlAmt = None

	@property
	def InvcAmt(self):
		return self._InvcAmt

	@InvcAmt.setter
	def InvcAmt(self, value):
		self._InvcAmt = value if type(value) != auto else self.make_default("InvcAmt")

	@InvcAmt.deleter
	def InvcAmt(self):
		del self._InvcAmt
		self._InvcAmt = None

	@property
	def ReqdAmt(self):
		return self._ReqdAmt

	@ReqdAmt.setter
	def ReqdAmt(self, value):
		self._ReqdAmt = value if type(value) != auto else self.make_default("ReqdAmt")

	@ReqdAmt.deleter
	def ReqdAmt(self):
		del self._ReqdAmt
		self._ReqdAmt = None

	@property
	def VldtyDt(self):
		return self._VldtyDt

	@VldtyDt.setter
	def VldtyDt(self, value):
		self._VldtyDt = value if type(value) != auto else self.make_default("VldtyDt")

	@VldtyDt.deleter
	def VldtyDt(self):
		del self._VldtyDt
		self._VldtyDt = None

	@property
	def UattnddLvlCtgy(self):
		return self._UattnddLvlCtgy

	@UattnddLvlCtgy.setter
	def UattnddLvlCtgy(self, value):
		self._UattnddLvlCtgy = value if type(value) != auto else self.make_default("UattnddLvlCtgy")

	@UattnddLvlCtgy.deleter
	def UattnddLvlCtgy(self):
		del self._UattnddLvlCtgy
		self._UattnddLvlCtgy = None

	@property
	def PdctCdSetId(self):
		return self._PdctCdSetId

	@PdctCdSetId.setter
	def PdctCdSetId(self, value):
		self._PdctCdSetId = value if type(value) != auto else self.make_default("PdctCdSetId")

	@PdctCdSetId.deleter
	def PdctCdSetId(self):
		del self._PdctCdSetId
		self._PdctCdSetId = None

	@property
	def AmtQlfr(self):
		return self._AmtQlfr

	@AmtQlfr.setter
	def AmtQlfr(self, value):
		self._AmtQlfr = value if type(value) != auto else self.make_default("AmtQlfr")

	@AmtQlfr.deleter
	def AmtQlfr(self):
		del self._AmtQlfr
		self._AmtQlfr = None

	@property
	def Rcrng(self):
		return self._Rcrng

	@Rcrng.setter
	def Rcrng(self, value):
		self._Rcrng = value if type(value) != auto else self.make_default("Rcrng")

	@Rcrng.deleter
	def Rcrng(self):
		del self._Rcrng
		self._Rcrng = None

	@property
	def AggtnTx(self):
		return self._AggtnTx

	@AggtnTx.setter
	def AggtnTx(self, value):
		self._AggtnTx = value if type(value) != auto else self.make_default("AggtnTx")

	@AggtnTx.deleter
	def AggtnTx(self):
		del self._AggtnTx
		self._AggtnTx = None

	@property
	def AddtlInf(self):
		return self._AddtlInf

	@AddtlInf.setter
	def AddtlInf(self, value):
		self._AddtlInf = value if type(value) != auto else self.make_default("AddtlInf")

	@AddtlInf.deleter
	def AddtlInf(self):
		del self._AddtlInf
		self._AddtlInf = None

	@property
	def CcyConvsRslt(self):
		return self._CcyConvsRslt

	@CcyConvsRslt.setter
	def CcyConvsRslt(self, value):
		self._CcyConvsRslt = value if type(value) != auto else self.make_default("CcyConvsRslt")

	@CcyConvsRslt.deleter
	def CcyConvsRslt(self):
		del self._CcyConvsRslt
		self._CcyConvsRslt = None

	@property
	def CmpltnSeqNb(self):
		return self._CmpltnSeqNb

	@CmpltnSeqNb.setter
	def CmpltnSeqNb(self, value):
		self._CmpltnSeqNb = value if type(value) != auto else self.make_default("CmpltnSeqNb")

	@CmpltnSeqNb.deleter
	def CmpltnSeqNb(self):
		del self._CmpltnSeqNb
		self._CmpltnSeqNb = None

	@property
	def SaleItm(self):
		return self._SaleItm

	@SaleItm.setter
	def SaleItm(self, value):
		self._SaleItm = value if type(value) != auto else self.make_default("SaleItm")

	@SaleItm.deleter
	def SaleItm(self):
		del self._SaleItm
		self._SaleItm = None

	@property
	def AuthrsdAmt(self):
		return self._AuthrsdAmt

	@AuthrsdAmt.setter
	def AuthrsdAmt(self, value):
		self._AuthrsdAmt = value if type(value) != auto else self.make_default("AuthrsdAmt")

	@AuthrsdAmt.deleter
	def AuthrsdAmt(self):
		del self._AuthrsdAmt
		self._AuthrsdAmt = None

	@property
	def ReSubmissnCntr(self):
		return self._ReSubmissnCntr

	@ReSubmissnCntr.setter
	def ReSubmissnCntr(self, value):
		self._ReSubmissnCntr = value if type(value) != auto else self.make_default("ReSubmissnCntr")

	@ReSubmissnCntr.deleter
	def ReSubmissnCntr(self):
		del self._ReSubmissnCntr
		self._ReSubmissnCntr = None

	@property
	def TtlAuthrsdAmt(self):
		return self._TtlAuthrsdAmt

	@TtlAuthrsdAmt.setter
	def TtlAuthrsdAmt(self, value):
		self._TtlAuthrsdAmt = value if type(value) != auto else self.make_default("TtlAuthrsdAmt")

	@TtlAuthrsdAmt.deleter
	def TtlAuthrsdAmt(self):
		del self._TtlAuthrsdAmt
		self._TtlAuthrsdAmt = None

	@property
	def OnLineRsn(self):
		return self._OnLineRsn

	@OnLineRsn.setter
	def OnLineRsn(self, value):
		self._OnLineRsn = value if type(value) != auto else self.make_default("OnLineRsn")

	@OnLineRsn.deleter
	def OnLineRsn(self):
		del self._OnLineRsn
		self._OnLineRsn = None

	@property
	def DlvryLctn(self):
		return self._DlvryLctn

	@DlvryLctn.setter
	def DlvryLctn(self, value):
		self._DlvryLctn = value if type(value) != auto else self.make_default("DlvryLctn")

	@DlvryLctn.deleter
	def DlvryLctn(self):
		del self._DlvryLctn
		self._DlvryLctn = None

	@property
	def Instlmt(self):
		return self._Instlmt

	@Instlmt.setter
	def Instlmt(self, value):
		self._Instlmt = value if type(value) != auto else self.make_default("Instlmt")

	@Instlmt.deleter
	def Instlmt(self):
		del self._Instlmt
		self._Instlmt = None

	@property
	def ICCRltdData(self):
		return self._ICCRltdData

	@ICCRltdData.setter
	def ICCRltdData(self, value):
		self._ICCRltdData = value if type(value) != auto else self.make_default("ICCRltdData")

	@ICCRltdData.deleter
	def ICCRltdData(self):
		del self._ICCRltdData
		self._ICCRltdData = None

	@property
	def CmpltnSeqCntr(self):
		return self._CmpltnSeqCntr

	@CmpltnSeqCntr.setter
	def CmpltnSeqCntr(self, value):
		self._CmpltnSeqCntr = value if type(value) != auto else self.make_default("CmpltnSeqCntr")

	@CmpltnSeqCntr.deleter
	def CmpltnSeqCntr(self):
		del self._CmpltnSeqCntr
		self._CmpltnSeqCntr = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AcctTp', type=CardAccountType3Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CmltvAmt', type=ImpliedCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DtldAmt', type=DetailedAmount15, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Ccy', type=ActiveCurrencyCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlAmt', type=ImpliedCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InvcAmt', type=ImpliedCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ReqdAmt', type=ImpliedCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='VldtyDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UattnddLvlCtgy', type=Max35NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PdctCdSetId', type=Max10Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AmtQlfr', type=TypeOfAmount8Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Rcrng', type=RecurringTransaction6, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AggtnTx', type=AggregationTransaction3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AddtlInf', type=ExternallyDefinedData5, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='CcyConvsRslt', type=CurrencyConversion30, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CmpltnSeqNb', type=PositiveNumber, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SaleItm', type=Product6, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='AuthrsdAmt', type=ImpliedCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ReSubmissnCntr', type=PositiveNumber, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlAuthrsdAmt', type=ImpliedCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OnLineRsn', type=OnLineReason2Code, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='DlvryLctn', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Instlmt', type=Instalment5, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='ICCRltdData', type=Max10000Binary, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CmpltnSeqCntr', type=PositiveNumber, min=0, max=1, mutex_group=None, array=False),
	))

