# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActiveCurrencyAnd13DecimalAmount
from . import ActiveCurrencyAndAmount
from . import AdditionalInformation15
from . import BonusWithdrawal2
from . import DateAndAmount2
from . import ISODate
from . import InnovativeFinance1
from . import Max35Text
from . import OtherAmount3
from . import PreviousYear4
from . import SubscriptionInformation2
from . import TaxEfficientProductType2Choice
from . import TaxReference2
from . import YesNoIndicator

class TaxEfficientProduct7(base_types._BaseFieldType):

	__slots__ = ["_AddtlInf", "_BnsOrWdrwl", "_CshCmpntInd", "_CurInvstmtAmt", "_CurYr", "_CurYrSbcptDtls", "_DtFrstQlfygAddtn", "_DtOfFrstSbcpt", "_EstmtdVal", "_InnvtvFinc", "_InvstmtsToFllwVal", "_InvstrTaxRef", "_LwstInvstdAmtCurYr", "_OthrAmt", "_PrvsYrSbcptAmt", "_PrvsYrs", "_PrvsYrsSbcptAmt", "_TaxClctnBase", "_TaxEffcntPdctTp", "_TrfrAltrnId", "_TtlSbcptAmt", "_UusdTaxDdctn", "_WdrwlForResdtlPurchsPrgrs"]
	@property
	def AddtlInf(self):
		return self._AddtlInf

	@AddtlInf.setter
	def AddtlInf(self, value):
		self._AddtlInf = value if value is not None else base_types.UninitialisedField(self, 'AddtlInf', AdditionalInformation15, True)

	@AddtlInf.deleter
	def AddtlInf(self):
		del self._AddtlInf
		self._AddtlInf = base_types.UninitialisedField(self, 'AddtlInf', AdditionalInformation15, True)

	@property
	def BnsOrWdrwl(self):
		return self._BnsOrWdrwl

	@BnsOrWdrwl.setter
	def BnsOrWdrwl(self, value):
		self._BnsOrWdrwl = value if value is not None else base_types.UninitialisedField(self, 'BnsOrWdrwl', BonusWithdrawal2, True)

	@BnsOrWdrwl.deleter
	def BnsOrWdrwl(self):
		del self._BnsOrWdrwl
		self._BnsOrWdrwl = base_types.UninitialisedField(self, 'BnsOrWdrwl', BonusWithdrawal2, True)

	@property
	def CshCmpntInd(self):
		return self._CshCmpntInd

	@CshCmpntInd.setter
	def CshCmpntInd(self, value):
		self._CshCmpntInd = value if value is not None else base_types.UninitialisedField(self, 'CshCmpntInd', YesNoIndicator, False)

	@CshCmpntInd.deleter
	def CshCmpntInd(self):
		del self._CshCmpntInd
		self._CshCmpntInd = base_types.UninitialisedField(self, 'CshCmpntInd', YesNoIndicator, False)

	@property
	def CurInvstmtAmt(self):
		return self._CurInvstmtAmt

	@CurInvstmtAmt.setter
	def CurInvstmtAmt(self, value):
		self._CurInvstmtAmt = value if value is not None else base_types.UninitialisedField(self, 'CurInvstmtAmt', ActiveCurrencyAnd13DecimalAmount, False)

	@CurInvstmtAmt.deleter
	def CurInvstmtAmt(self):
		del self._CurInvstmtAmt
		self._CurInvstmtAmt = base_types.UninitialisedField(self, 'CurInvstmtAmt', ActiveCurrencyAnd13DecimalAmount, False)

	@property
	def CurYr(self):
		return self._CurYr

	@CurYr.setter
	def CurYr(self, value):
		self._CurYr = value if value is not None else base_types.UninitialisedField(self, 'CurYr', YesNoIndicator, False)

	@CurYr.deleter
	def CurYr(self):
		del self._CurYr
		self._CurYr = base_types.UninitialisedField(self, 'CurYr', YesNoIndicator, False)

	@property
	def CurYrSbcptDtls(self):
		return self._CurYrSbcptDtls

	@CurYrSbcptDtls.setter
	def CurYrSbcptDtls(self, value):
		self._CurYrSbcptDtls = value if value is not None else base_types.UninitialisedField(self, 'CurYrSbcptDtls', SubscriptionInformation2, False)

	@CurYrSbcptDtls.deleter
	def CurYrSbcptDtls(self):
		del self._CurYrSbcptDtls
		self._CurYrSbcptDtls = base_types.UninitialisedField(self, 'CurYrSbcptDtls', SubscriptionInformation2, False)

	@property
	def DtFrstQlfygAddtn(self):
		return self._DtFrstQlfygAddtn

	@DtFrstQlfygAddtn.setter
	def DtFrstQlfygAddtn(self, value):
		self._DtFrstQlfygAddtn = value if value is not None else base_types.UninitialisedField(self, 'DtFrstQlfygAddtn', ISODate, False)

	@DtFrstQlfygAddtn.deleter
	def DtFrstQlfygAddtn(self):
		del self._DtFrstQlfygAddtn
		self._DtFrstQlfygAddtn = base_types.UninitialisedField(self, 'DtFrstQlfygAddtn', ISODate, False)

	@property
	def DtOfFrstSbcpt(self):
		return self._DtOfFrstSbcpt

	@DtOfFrstSbcpt.setter
	def DtOfFrstSbcpt(self, value):
		self._DtOfFrstSbcpt = value if value is not None else base_types.UninitialisedField(self, 'DtOfFrstSbcpt', ISODate, False)

	@DtOfFrstSbcpt.deleter
	def DtOfFrstSbcpt(self):
		del self._DtOfFrstSbcpt
		self._DtOfFrstSbcpt = base_types.UninitialisedField(self, 'DtOfFrstSbcpt', ISODate, False)

	@property
	def EstmtdVal(self):
		return self._EstmtdVal

	@EstmtdVal.setter
	def EstmtdVal(self, value):
		self._EstmtdVal = value if value is not None else base_types.UninitialisedField(self, 'EstmtdVal', DateAndAmount2, False)

	@EstmtdVal.deleter
	def EstmtdVal(self):
		del self._EstmtdVal
		self._EstmtdVal = base_types.UninitialisedField(self, 'EstmtdVal', DateAndAmount2, False)

	@property
	def InnvtvFinc(self):
		return self._InnvtvFinc

	@InnvtvFinc.setter
	def InnvtvFinc(self, value):
		self._InnvtvFinc = value if value is not None else base_types.UninitialisedField(self, 'InnvtvFinc', InnovativeFinance1, True)

	@InnvtvFinc.deleter
	def InnvtvFinc(self):
		del self._InnvtvFinc
		self._InnvtvFinc = base_types.UninitialisedField(self, 'InnvtvFinc', InnovativeFinance1, True)

	@property
	def InvstmtsToFllwVal(self):
		return self._InvstmtsToFllwVal

	@InvstmtsToFllwVal.setter
	def InvstmtsToFllwVal(self, value):
		self._InvstmtsToFllwVal = value if value is not None else base_types.UninitialisedField(self, 'InvstmtsToFllwVal', DateAndAmount2, True)

	@InvstmtsToFllwVal.deleter
	def InvstmtsToFllwVal(self):
		del self._InvstmtsToFllwVal
		self._InvstmtsToFllwVal = base_types.UninitialisedField(self, 'InvstmtsToFllwVal', DateAndAmount2, True)

	@property
	def InvstrTaxRef(self):
		return self._InvstrTaxRef

	@InvstrTaxRef.setter
	def InvstrTaxRef(self, value):
		self._InvstrTaxRef = value if value is not None else base_types.UninitialisedField(self, 'InvstrTaxRef', TaxReference2, False)

	@InvstrTaxRef.deleter
	def InvstrTaxRef(self):
		del self._InvstrTaxRef
		self._InvstrTaxRef = base_types.UninitialisedField(self, 'InvstrTaxRef', TaxReference2, False)

	@property
	def LwstInvstdAmtCurYr(self):
		return self._LwstInvstdAmtCurYr

	@LwstInvstdAmtCurYr.setter
	def LwstInvstdAmtCurYr(self, value):
		self._LwstInvstdAmtCurYr = value if value is not None else base_types.UninitialisedField(self, 'LwstInvstdAmtCurYr', ActiveCurrencyAnd13DecimalAmount, False)

	@LwstInvstdAmtCurYr.deleter
	def LwstInvstdAmtCurYr(self):
		del self._LwstInvstdAmtCurYr
		self._LwstInvstdAmtCurYr = base_types.UninitialisedField(self, 'LwstInvstdAmtCurYr', ActiveCurrencyAnd13DecimalAmount, False)

	@property
	def OthrAmt(self):
		return self._OthrAmt

	@OthrAmt.setter
	def OthrAmt(self, value):
		self._OthrAmt = value if value is not None else base_types.UninitialisedField(self, 'OthrAmt', OtherAmount3, True)

	@OthrAmt.deleter
	def OthrAmt(self):
		del self._OthrAmt
		self._OthrAmt = base_types.UninitialisedField(self, 'OthrAmt', OtherAmount3, True)

	@property
	def PrvsYrSbcptAmt(self):
		return self._PrvsYrSbcptAmt

	@PrvsYrSbcptAmt.setter
	def PrvsYrSbcptAmt(self, value):
		self._PrvsYrSbcptAmt = value if value is not None else base_types.UninitialisedField(self, 'PrvsYrSbcptAmt', ActiveCurrencyAnd13DecimalAmount, False)

	@PrvsYrSbcptAmt.deleter
	def PrvsYrSbcptAmt(self):
		del self._PrvsYrSbcptAmt
		self._PrvsYrSbcptAmt = base_types.UninitialisedField(self, 'PrvsYrSbcptAmt', ActiveCurrencyAnd13DecimalAmount, False)

	@property
	def PrvsYrs(self):
		return self._PrvsYrs

	@PrvsYrs.setter
	def PrvsYrs(self, value):
		self._PrvsYrs = value if value is not None else base_types.UninitialisedField(self, 'PrvsYrs', PreviousYear4, False)

	@PrvsYrs.deleter
	def PrvsYrs(self):
		del self._PrvsYrs
		self._PrvsYrs = base_types.UninitialisedField(self, 'PrvsYrs', PreviousYear4, False)

	@property
	def PrvsYrsSbcptAmt(self):
		return self._PrvsYrsSbcptAmt

	@PrvsYrsSbcptAmt.setter
	def PrvsYrsSbcptAmt(self, value):
		self._PrvsYrsSbcptAmt = value if value is not None else base_types.UninitialisedField(self, 'PrvsYrsSbcptAmt', ActiveCurrencyAnd13DecimalAmount, False)

	@PrvsYrsSbcptAmt.deleter
	def PrvsYrsSbcptAmt(self):
		del self._PrvsYrsSbcptAmt
		self._PrvsYrsSbcptAmt = base_types.UninitialisedField(self, 'PrvsYrsSbcptAmt', ActiveCurrencyAnd13DecimalAmount, False)

	@property
	def TaxClctnBase(self):
		return self._TaxClctnBase

	@TaxClctnBase.setter
	def TaxClctnBase(self, value):
		self._TaxClctnBase = value if value is not None else base_types.UninitialisedField(self, 'TaxClctnBase', ActiveCurrencyAnd13DecimalAmount, False)

	@TaxClctnBase.deleter
	def TaxClctnBase(self):
		del self._TaxClctnBase
		self._TaxClctnBase = base_types.UninitialisedField(self, 'TaxClctnBase', ActiveCurrencyAnd13DecimalAmount, False)

	@property
	def TaxEffcntPdctTp(self):
		return self._TaxEffcntPdctTp

	@TaxEffcntPdctTp.setter
	def TaxEffcntPdctTp(self, value):
		self._TaxEffcntPdctTp = value if value is not None else base_types.UninitialisedField(self, 'TaxEffcntPdctTp', TaxEfficientProductType2Choice, False)

	@TaxEffcntPdctTp.deleter
	def TaxEffcntPdctTp(self):
		del self._TaxEffcntPdctTp
		self._TaxEffcntPdctTp = base_types.UninitialisedField(self, 'TaxEffcntPdctTp', TaxEfficientProductType2Choice, False)

	@property
	def TrfrAltrnId(self):
		return self._TrfrAltrnId

	@TrfrAltrnId.setter
	def TrfrAltrnId(self, value):
		self._TrfrAltrnId = value if value is not None else base_types.UninitialisedField(self, 'TrfrAltrnId', Max35Text, False)

	@TrfrAltrnId.deleter
	def TrfrAltrnId(self):
		del self._TrfrAltrnId
		self._TrfrAltrnId = base_types.UninitialisedField(self, 'TrfrAltrnId', Max35Text, False)

	@property
	def TtlSbcptAmt(self):
		return self._TtlSbcptAmt

	@TtlSbcptAmt.setter
	def TtlSbcptAmt(self, value):
		self._TtlSbcptAmt = value if value is not None else base_types.UninitialisedField(self, 'TtlSbcptAmt', ActiveCurrencyAndAmount, False)

	@TtlSbcptAmt.deleter
	def TtlSbcptAmt(self):
		del self._TtlSbcptAmt
		self._TtlSbcptAmt = base_types.UninitialisedField(self, 'TtlSbcptAmt', ActiveCurrencyAndAmount, False)

	@property
	def UusdTaxDdctn(self):
		return self._UusdTaxDdctn

	@UusdTaxDdctn.setter
	def UusdTaxDdctn(self, value):
		self._UusdTaxDdctn = value if value is not None else base_types.UninitialisedField(self, 'UusdTaxDdctn', ActiveCurrencyAnd13DecimalAmount, False)

	@UusdTaxDdctn.deleter
	def UusdTaxDdctn(self):
		del self._UusdTaxDdctn
		self._UusdTaxDdctn = base_types.UninitialisedField(self, 'UusdTaxDdctn', ActiveCurrencyAnd13DecimalAmount, False)

	@property
	def WdrwlForResdtlPurchsPrgrs(self):
		return self._WdrwlForResdtlPurchsPrgrs

	@WdrwlForResdtlPurchsPrgrs.setter
	def WdrwlForResdtlPurchsPrgrs(self, value):
		self._WdrwlForResdtlPurchsPrgrs = value if value is not None else base_types.UninitialisedField(self, 'WdrwlForResdtlPurchsPrgrs', YesNoIndicator, False)

	@WdrwlForResdtlPurchsPrgrs.deleter
	def WdrwlForResdtlPurchsPrgrs(self):
		del self._WdrwlForResdtlPurchsPrgrs
		self._WdrwlForResdtlPurchsPrgrs = base_types.UninitialisedField(self, 'WdrwlForResdtlPurchsPrgrs', YesNoIndicator, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AddtlInf', type=AdditionalInformation15, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='BnsOrWdrwl', type=BonusWithdrawal2, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='CshCmpntInd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CurInvstmtAmt', type=ActiveCurrencyAnd13DecimalAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CurYr', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CurYrSbcptDtls', type=SubscriptionInformation2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DtFrstQlfygAddtn', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DtOfFrstSbcpt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='EstmtdVal', type=DateAndAmount2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InnvtvFinc', type=InnovativeFinance1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='InvstmtsToFllwVal', type=DateAndAmount2, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='InvstrTaxRef', type=TaxReference2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LwstInvstdAmtCurYr', type=ActiveCurrencyAnd13DecimalAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OthrAmt', type=OtherAmount3, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='PrvsYrSbcptAmt', type=ActiveCurrencyAnd13DecimalAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrvsYrs', type=PreviousYear4, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrvsYrsSbcptAmt', type=ActiveCurrencyAnd13DecimalAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TaxClctnBase', type=ActiveCurrencyAnd13DecimalAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TaxEffcntPdctTp', type=TaxEfficientProductType2Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TrfrAltrnId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlSbcptAmt', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UusdTaxDdctn', type=ActiveCurrencyAnd13DecimalAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='WdrwlForResdtlPurchsPrgrs', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
	))