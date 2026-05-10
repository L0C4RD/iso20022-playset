from . import base_types
from ._ActiveCurrencyAndAmount import ActiveCurrencyAndAmount
from ._PreviousYear4 import PreviousYear4
from ._OtherAmount3 import OtherAmount3
from ._InnovativeFinance1 import InnovativeFinance1
from ._BonusWithdrawal2 import BonusWithdrawal2
from ._TaxReference2 import TaxReference2
from ._SubscriptionInformation2 import SubscriptionInformation2
from ._YesNoIndicator import YesNoIndicator
from ._TaxEfficientProductType2Choice import TaxEfficientProductType2Choice
from ._Max35Text import Max35Text
from ._DateAndAmount2 import DateAndAmount2
from ._ISODate import ISODate
from ._ActiveCurrencyAnd13DecimalAmount import ActiveCurrencyAnd13DecimalAmount
from ._AdditionalInformation15 import AdditionalInformation15

class TaxEfficientProduct7(base_types._BaseFieldType):

	__slots__ = ["_PrvsYrSbcptAmt", "_TtlSbcptAmt", "_DtFrstQlfygAddtn", "_CurYrSbcptDtls", "_CurInvstmtAmt", "_TrfrAltrnId", "_InvstrTaxRef", "_TaxEffcntPdctTp", "_InvstmtsToFllwVal", "_PrvsYrsSbcptAmt", "_DtOfFrstSbcpt", "_LwstInvstdAmtCurYr", "_BnsOrWdrwl", "_PrvsYrs", "_TaxClctnBase", "_UusdTaxDdctn", "_WdrwlForResdtlPurchsPrgrs", "_CshCmpntInd", "_AddtlInf", "_CurYr", "_InnvtvFinc", "_OthrAmt", "_EstmtdVal"]
	@property
	def PrvsYrSbcptAmt(self):
		return self._PrvsYrSbcptAmt

	@PrvsYrSbcptAmt.setter
	def PrvsYrSbcptAmt(self, value):
		self._PrvsYrSbcptAmt = value if type(value) != base_types.auto else self.make_default("PrvsYrSbcptAmt")

	@PrvsYrSbcptAmt.deleter
	def PrvsYrSbcptAmt(self):
		del self._PrvsYrSbcptAmt
		self._PrvsYrSbcptAmt = None

	@property
	def TtlSbcptAmt(self):
		return self._TtlSbcptAmt

	@TtlSbcptAmt.setter
	def TtlSbcptAmt(self, value):
		self._TtlSbcptAmt = value if type(value) != base_types.auto else self.make_default("TtlSbcptAmt")

	@TtlSbcptAmt.deleter
	def TtlSbcptAmt(self):
		del self._TtlSbcptAmt
		self._TtlSbcptAmt = None

	@property
	def DtFrstQlfygAddtn(self):
		return self._DtFrstQlfygAddtn

	@DtFrstQlfygAddtn.setter
	def DtFrstQlfygAddtn(self, value):
		self._DtFrstQlfygAddtn = value if type(value) != base_types.auto else self.make_default("DtFrstQlfygAddtn")

	@DtFrstQlfygAddtn.deleter
	def DtFrstQlfygAddtn(self):
		del self._DtFrstQlfygAddtn
		self._DtFrstQlfygAddtn = None

	@property
	def CurYrSbcptDtls(self):
		return self._CurYrSbcptDtls

	@CurYrSbcptDtls.setter
	def CurYrSbcptDtls(self, value):
		self._CurYrSbcptDtls = value if type(value) != base_types.auto else self.make_default("CurYrSbcptDtls")

	@CurYrSbcptDtls.deleter
	def CurYrSbcptDtls(self):
		del self._CurYrSbcptDtls
		self._CurYrSbcptDtls = None

	@property
	def CurInvstmtAmt(self):
		return self._CurInvstmtAmt

	@CurInvstmtAmt.setter
	def CurInvstmtAmt(self, value):
		self._CurInvstmtAmt = value if type(value) != base_types.auto else self.make_default("CurInvstmtAmt")

	@CurInvstmtAmt.deleter
	def CurInvstmtAmt(self):
		del self._CurInvstmtAmt
		self._CurInvstmtAmt = None

	@property
	def TrfrAltrnId(self):
		return self._TrfrAltrnId

	@TrfrAltrnId.setter
	def TrfrAltrnId(self, value):
		self._TrfrAltrnId = value if type(value) != base_types.auto else self.make_default("TrfrAltrnId")

	@TrfrAltrnId.deleter
	def TrfrAltrnId(self):
		del self._TrfrAltrnId
		self._TrfrAltrnId = None

	@property
	def InvstrTaxRef(self):
		return self._InvstrTaxRef

	@InvstrTaxRef.setter
	def InvstrTaxRef(self, value):
		self._InvstrTaxRef = value if type(value) != base_types.auto else self.make_default("InvstrTaxRef")

	@InvstrTaxRef.deleter
	def InvstrTaxRef(self):
		del self._InvstrTaxRef
		self._InvstrTaxRef = None

	@property
	def TaxEffcntPdctTp(self):
		return self._TaxEffcntPdctTp

	@TaxEffcntPdctTp.setter
	def TaxEffcntPdctTp(self, value):
		self._TaxEffcntPdctTp = value if type(value) != base_types.auto else self.make_default("TaxEffcntPdctTp")

	@TaxEffcntPdctTp.deleter
	def TaxEffcntPdctTp(self):
		del self._TaxEffcntPdctTp
		self._TaxEffcntPdctTp = None

	@property
	def InvstmtsToFllwVal(self):
		return self._InvstmtsToFllwVal

	@InvstmtsToFllwVal.setter
	def InvstmtsToFllwVal(self, value):
		self._InvstmtsToFllwVal = value if type(value) != base_types.auto else self.make_default("InvstmtsToFllwVal")

	@InvstmtsToFllwVal.deleter
	def InvstmtsToFllwVal(self):
		del self._InvstmtsToFllwVal
		self._InvstmtsToFllwVal = None

	@property
	def PrvsYrsSbcptAmt(self):
		return self._PrvsYrsSbcptAmt

	@PrvsYrsSbcptAmt.setter
	def PrvsYrsSbcptAmt(self, value):
		self._PrvsYrsSbcptAmt = value if type(value) != base_types.auto else self.make_default("PrvsYrsSbcptAmt")

	@PrvsYrsSbcptAmt.deleter
	def PrvsYrsSbcptAmt(self):
		del self._PrvsYrsSbcptAmt
		self._PrvsYrsSbcptAmt = None

	@property
	def DtOfFrstSbcpt(self):
		return self._DtOfFrstSbcpt

	@DtOfFrstSbcpt.setter
	def DtOfFrstSbcpt(self, value):
		self._DtOfFrstSbcpt = value if type(value) != base_types.auto else self.make_default("DtOfFrstSbcpt")

	@DtOfFrstSbcpt.deleter
	def DtOfFrstSbcpt(self):
		del self._DtOfFrstSbcpt
		self._DtOfFrstSbcpt = None

	@property
	def LwstInvstdAmtCurYr(self):
		return self._LwstInvstdAmtCurYr

	@LwstInvstdAmtCurYr.setter
	def LwstInvstdAmtCurYr(self, value):
		self._LwstInvstdAmtCurYr = value if type(value) != base_types.auto else self.make_default("LwstInvstdAmtCurYr")

	@LwstInvstdAmtCurYr.deleter
	def LwstInvstdAmtCurYr(self):
		del self._LwstInvstdAmtCurYr
		self._LwstInvstdAmtCurYr = None

	@property
	def BnsOrWdrwl(self):
		return self._BnsOrWdrwl

	@BnsOrWdrwl.setter
	def BnsOrWdrwl(self, value):
		self._BnsOrWdrwl = value if type(value) != base_types.auto else self.make_default("BnsOrWdrwl")

	@BnsOrWdrwl.deleter
	def BnsOrWdrwl(self):
		del self._BnsOrWdrwl
		self._BnsOrWdrwl = None

	@property
	def PrvsYrs(self):
		return self._PrvsYrs

	@PrvsYrs.setter
	def PrvsYrs(self, value):
		self._PrvsYrs = value if type(value) != base_types.auto else self.make_default("PrvsYrs")

	@PrvsYrs.deleter
	def PrvsYrs(self):
		del self._PrvsYrs
		self._PrvsYrs = None

	@property
	def TaxClctnBase(self):
		return self._TaxClctnBase

	@TaxClctnBase.setter
	def TaxClctnBase(self, value):
		self._TaxClctnBase = value if type(value) != base_types.auto else self.make_default("TaxClctnBase")

	@TaxClctnBase.deleter
	def TaxClctnBase(self):
		del self._TaxClctnBase
		self._TaxClctnBase = None

	@property
	def UusdTaxDdctn(self):
		return self._UusdTaxDdctn

	@UusdTaxDdctn.setter
	def UusdTaxDdctn(self, value):
		self._UusdTaxDdctn = value if type(value) != base_types.auto else self.make_default("UusdTaxDdctn")

	@UusdTaxDdctn.deleter
	def UusdTaxDdctn(self):
		del self._UusdTaxDdctn
		self._UusdTaxDdctn = None

	@property
	def WdrwlForResdtlPurchsPrgrs(self):
		return self._WdrwlForResdtlPurchsPrgrs

	@WdrwlForResdtlPurchsPrgrs.setter
	def WdrwlForResdtlPurchsPrgrs(self, value):
		self._WdrwlForResdtlPurchsPrgrs = value if type(value) != base_types.auto else self.make_default("WdrwlForResdtlPurchsPrgrs")

	@WdrwlForResdtlPurchsPrgrs.deleter
	def WdrwlForResdtlPurchsPrgrs(self):
		del self._WdrwlForResdtlPurchsPrgrs
		self._WdrwlForResdtlPurchsPrgrs = None

	@property
	def CshCmpntInd(self):
		return self._CshCmpntInd

	@CshCmpntInd.setter
	def CshCmpntInd(self, value):
		self._CshCmpntInd = value if type(value) != base_types.auto else self.make_default("CshCmpntInd")

	@CshCmpntInd.deleter
	def CshCmpntInd(self):
		del self._CshCmpntInd
		self._CshCmpntInd = None

	@property
	def AddtlInf(self):
		return self._AddtlInf

	@AddtlInf.setter
	def AddtlInf(self, value):
		self._AddtlInf = value if type(value) != base_types.auto else self.make_default("AddtlInf")

	@AddtlInf.deleter
	def AddtlInf(self):
		del self._AddtlInf
		self._AddtlInf = None

	@property
	def CurYr(self):
		return self._CurYr

	@CurYr.setter
	def CurYr(self, value):
		self._CurYr = value if type(value) != base_types.auto else self.make_default("CurYr")

	@CurYr.deleter
	def CurYr(self):
		del self._CurYr
		self._CurYr = None

	@property
	def InnvtvFinc(self):
		return self._InnvtvFinc

	@InnvtvFinc.setter
	def InnvtvFinc(self, value):
		self._InnvtvFinc = value if type(value) != base_types.auto else self.make_default("InnvtvFinc")

	@InnvtvFinc.deleter
	def InnvtvFinc(self):
		del self._InnvtvFinc
		self._InnvtvFinc = None

	@property
	def OthrAmt(self):
		return self._OthrAmt

	@OthrAmt.setter
	def OthrAmt(self, value):
		self._OthrAmt = value if type(value) != base_types.auto else self.make_default("OthrAmt")

	@OthrAmt.deleter
	def OthrAmt(self):
		del self._OthrAmt
		self._OthrAmt = None

	@property
	def EstmtdVal(self):
		return self._EstmtdVal

	@EstmtdVal.setter
	def EstmtdVal(self, value):
		self._EstmtdVal = value if type(value) != base_types.auto else self.make_default("EstmtdVal")

	@EstmtdVal.deleter
	def EstmtdVal(self):
		del self._EstmtdVal
		self._EstmtdVal = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='PrvsYrSbcptAmt', type=ActiveCurrencyAnd13DecimalAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlSbcptAmt', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DtFrstQlfygAddtn', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CurYrSbcptDtls', type=SubscriptionInformation2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CurInvstmtAmt', type=ActiveCurrencyAnd13DecimalAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TrfrAltrnId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InvstrTaxRef', type=TaxReference2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TaxEffcntPdctTp', type=TaxEfficientProductType2Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InvstmtsToFllwVal', type=DateAndAmount2, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='PrvsYrsSbcptAmt', type=ActiveCurrencyAnd13DecimalAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DtOfFrstSbcpt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LwstInvstdAmtCurYr', type=ActiveCurrencyAnd13DecimalAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BnsOrWdrwl', type=BonusWithdrawal2, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='PrvsYrs', type=PreviousYear4, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TaxClctnBase', type=ActiveCurrencyAnd13DecimalAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UusdTaxDdctn', type=ActiveCurrencyAnd13DecimalAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='WdrwlForResdtlPurchsPrgrs', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CshCmpntInd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AddtlInf', type=AdditionalInformation15, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='CurYr', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InnvtvFinc', type=InnovativeFinance1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='OthrAmt', type=OtherAmount3, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='EstmtdVal', type=DateAndAmount2, min=0, max=1, mutex_group=None, array=False),
	))

