from . import base_types
from .IncomePreference1Code import IncomePreference1Code
from .DateAndDateTimeChoice import DateAndDateTimeChoice
from .DeliveryParameters3 import DeliveryParameters3
from .FinancialInstrument57 import FinancialInstrument57
from .ActiveCurrencyCode import ActiveCurrencyCode
from .InformativeTax1 import InformativeTax1
from .InvestmentAccount58 import InvestmentAccount58
from .ActiveCurrencyAndAmount import ActiveCurrencyAndAmount
from .Equalisation1 import Equalisation1
from .TotalFeesAndTaxes40 import TotalFeesAndTaxes40
from .Max350Text import Max350Text
from .UKTaxGroupUnit1Code import UKTaxGroupUnit1Code
from .ProfitAndLoss2Choice import ProfitAndLoss2Choice
from .DecimalNumber import DecimalNumber
from .ActiveOrHistoricCurrencyCode import ActiveOrHistoricCurrencyCode
from .PercentageRate import PercentageRate
from .UnitPrice22 import UnitPrice22
from .Max35Text import Max35Text
from .FundSettlementParameters11 import FundSettlementParameters11
from .HoldBackInformation2 import HoldBackInformation2
from .YesNoIndicator import YesNoIndicator

class SwitchRedemptionLegExecution4(base_types._BaseFieldType):

	__slots__ = ["_PhysDlvryDtls", "_Grp1Or2Units", "_SttlmAndCtdyDtls", "_FinInstrmDtls", "_PhysDlvryInd", "_InvstmtAcctDtls", "_IntrmPrftAmt", "_UnitsNb", "_GrssAmt", "_TxOvrhd", "_InftvPricDtls", "_ReqdNAVCcy", "_LegId", "_NetAmt", "_ReqdSttlmCcy", "_GtgOrHldBckDtls", "_HldgsRedRate", "_NonStdSttlmInf", "_Equlstn", "_LegExctnId", "_CumDvddInd", "_PricDtls", "_IncmPref", "_TradDtTm", "_InftvTaxDtls"]
	@property
	def PhysDlvryDtls(self):
		return self._PhysDlvryDtls

	@PhysDlvryDtls.setter
	def PhysDlvryDtls(self, value):
		self._PhysDlvryDtls = value if type(value) != base_types.auto else self.make_default("PhysDlvryDtls")

	@PhysDlvryDtls.deleter
	def PhysDlvryDtls(self):
		del self._PhysDlvryDtls
		self._PhysDlvryDtls = None

	@property
	def Grp1Or2Units(self):
		return self._Grp1Or2Units

	@Grp1Or2Units.setter
	def Grp1Or2Units(self, value):
		self._Grp1Or2Units = value if type(value) != base_types.auto else self.make_default("Grp1Or2Units")

	@Grp1Or2Units.deleter
	def Grp1Or2Units(self):
		del self._Grp1Or2Units
		self._Grp1Or2Units = None

	@property
	def SttlmAndCtdyDtls(self):
		return self._SttlmAndCtdyDtls

	@SttlmAndCtdyDtls.setter
	def SttlmAndCtdyDtls(self, value):
		self._SttlmAndCtdyDtls = value if type(value) != base_types.auto else self.make_default("SttlmAndCtdyDtls")

	@SttlmAndCtdyDtls.deleter
	def SttlmAndCtdyDtls(self):
		del self._SttlmAndCtdyDtls
		self._SttlmAndCtdyDtls = None

	@property
	def FinInstrmDtls(self):
		return self._FinInstrmDtls

	@FinInstrmDtls.setter
	def FinInstrmDtls(self, value):
		self._FinInstrmDtls = value if type(value) != base_types.auto else self.make_default("FinInstrmDtls")

	@FinInstrmDtls.deleter
	def FinInstrmDtls(self):
		del self._FinInstrmDtls
		self._FinInstrmDtls = None

	@property
	def PhysDlvryInd(self):
		return self._PhysDlvryInd

	@PhysDlvryInd.setter
	def PhysDlvryInd(self, value):
		self._PhysDlvryInd = value if type(value) != base_types.auto else self.make_default("PhysDlvryInd")

	@PhysDlvryInd.deleter
	def PhysDlvryInd(self):
		del self._PhysDlvryInd
		self._PhysDlvryInd = None

	@property
	def InvstmtAcctDtls(self):
		return self._InvstmtAcctDtls

	@InvstmtAcctDtls.setter
	def InvstmtAcctDtls(self, value):
		self._InvstmtAcctDtls = value if type(value) != base_types.auto else self.make_default("InvstmtAcctDtls")

	@InvstmtAcctDtls.deleter
	def InvstmtAcctDtls(self):
		del self._InvstmtAcctDtls
		self._InvstmtAcctDtls = None

	@property
	def IntrmPrftAmt(self):
		return self._IntrmPrftAmt

	@IntrmPrftAmt.setter
	def IntrmPrftAmt(self, value):
		self._IntrmPrftAmt = value if type(value) != base_types.auto else self.make_default("IntrmPrftAmt")

	@IntrmPrftAmt.deleter
	def IntrmPrftAmt(self):
		del self._IntrmPrftAmt
		self._IntrmPrftAmt = None

	@property
	def UnitsNb(self):
		return self._UnitsNb

	@UnitsNb.setter
	def UnitsNb(self, value):
		self._UnitsNb = value if type(value) != base_types.auto else self.make_default("UnitsNb")

	@UnitsNb.deleter
	def UnitsNb(self):
		del self._UnitsNb
		self._UnitsNb = None

	@property
	def GrssAmt(self):
		return self._GrssAmt

	@GrssAmt.setter
	def GrssAmt(self, value):
		self._GrssAmt = value if type(value) != base_types.auto else self.make_default("GrssAmt")

	@GrssAmt.deleter
	def GrssAmt(self):
		del self._GrssAmt
		self._GrssAmt = None

	@property
	def TxOvrhd(self):
		return self._TxOvrhd

	@TxOvrhd.setter
	def TxOvrhd(self, value):
		self._TxOvrhd = value if type(value) != base_types.auto else self.make_default("TxOvrhd")

	@TxOvrhd.deleter
	def TxOvrhd(self):
		del self._TxOvrhd
		self._TxOvrhd = None

	@property
	def InftvPricDtls(self):
		return self._InftvPricDtls

	@InftvPricDtls.setter
	def InftvPricDtls(self, value):
		self._InftvPricDtls = value if type(value) != base_types.auto else self.make_default("InftvPricDtls")

	@InftvPricDtls.deleter
	def InftvPricDtls(self):
		del self._InftvPricDtls
		self._InftvPricDtls = None

	@property
	def ReqdNAVCcy(self):
		return self._ReqdNAVCcy

	@ReqdNAVCcy.setter
	def ReqdNAVCcy(self, value):
		self._ReqdNAVCcy = value if type(value) != base_types.auto else self.make_default("ReqdNAVCcy")

	@ReqdNAVCcy.deleter
	def ReqdNAVCcy(self):
		del self._ReqdNAVCcy
		self._ReqdNAVCcy = None

	@property
	def LegId(self):
		return self._LegId

	@LegId.setter
	def LegId(self, value):
		self._LegId = value if type(value) != base_types.auto else self.make_default("LegId")

	@LegId.deleter
	def LegId(self):
		del self._LegId
		self._LegId = None

	@property
	def NetAmt(self):
		return self._NetAmt

	@NetAmt.setter
	def NetAmt(self, value):
		self._NetAmt = value if type(value) != base_types.auto else self.make_default("NetAmt")

	@NetAmt.deleter
	def NetAmt(self):
		del self._NetAmt
		self._NetAmt = None

	@property
	def ReqdSttlmCcy(self):
		return self._ReqdSttlmCcy

	@ReqdSttlmCcy.setter
	def ReqdSttlmCcy(self, value):
		self._ReqdSttlmCcy = value if type(value) != base_types.auto else self.make_default("ReqdSttlmCcy")

	@ReqdSttlmCcy.deleter
	def ReqdSttlmCcy(self):
		del self._ReqdSttlmCcy
		self._ReqdSttlmCcy = None

	@property
	def GtgOrHldBckDtls(self):
		return self._GtgOrHldBckDtls

	@GtgOrHldBckDtls.setter
	def GtgOrHldBckDtls(self, value):
		self._GtgOrHldBckDtls = value if type(value) != base_types.auto else self.make_default("GtgOrHldBckDtls")

	@GtgOrHldBckDtls.deleter
	def GtgOrHldBckDtls(self):
		del self._GtgOrHldBckDtls
		self._GtgOrHldBckDtls = None

	@property
	def HldgsRedRate(self):
		return self._HldgsRedRate

	@HldgsRedRate.setter
	def HldgsRedRate(self, value):
		self._HldgsRedRate = value if type(value) != base_types.auto else self.make_default("HldgsRedRate")

	@HldgsRedRate.deleter
	def HldgsRedRate(self):
		del self._HldgsRedRate
		self._HldgsRedRate = None

	@property
	def NonStdSttlmInf(self):
		return self._NonStdSttlmInf

	@NonStdSttlmInf.setter
	def NonStdSttlmInf(self, value):
		self._NonStdSttlmInf = value if type(value) != base_types.auto else self.make_default("NonStdSttlmInf")

	@NonStdSttlmInf.deleter
	def NonStdSttlmInf(self):
		del self._NonStdSttlmInf
		self._NonStdSttlmInf = None

	@property
	def Equlstn(self):
		return self._Equlstn

	@Equlstn.setter
	def Equlstn(self, value):
		self._Equlstn = value if type(value) != base_types.auto else self.make_default("Equlstn")

	@Equlstn.deleter
	def Equlstn(self):
		del self._Equlstn
		self._Equlstn = None

	@property
	def LegExctnId(self):
		return self._LegExctnId

	@LegExctnId.setter
	def LegExctnId(self, value):
		self._LegExctnId = value if type(value) != base_types.auto else self.make_default("LegExctnId")

	@LegExctnId.deleter
	def LegExctnId(self):
		del self._LegExctnId
		self._LegExctnId = None

	@property
	def CumDvddInd(self):
		return self._CumDvddInd

	@CumDvddInd.setter
	def CumDvddInd(self, value):
		self._CumDvddInd = value if type(value) != base_types.auto else self.make_default("CumDvddInd")

	@CumDvddInd.deleter
	def CumDvddInd(self):
		del self._CumDvddInd
		self._CumDvddInd = None

	@property
	def PricDtls(self):
		return self._PricDtls

	@PricDtls.setter
	def PricDtls(self, value):
		self._PricDtls = value if type(value) != base_types.auto else self.make_default("PricDtls")

	@PricDtls.deleter
	def PricDtls(self):
		del self._PricDtls
		self._PricDtls = None

	@property
	def IncmPref(self):
		return self._IncmPref

	@IncmPref.setter
	def IncmPref(self, value):
		self._IncmPref = value if type(value) != base_types.auto else self.make_default("IncmPref")

	@IncmPref.deleter
	def IncmPref(self):
		del self._IncmPref
		self._IncmPref = None

	@property
	def TradDtTm(self):
		return self._TradDtTm

	@TradDtTm.setter
	def TradDtTm(self, value):
		self._TradDtTm = value if type(value) != base_types.auto else self.make_default("TradDtTm")

	@TradDtTm.deleter
	def TradDtTm(self):
		del self._TradDtTm
		self._TradDtTm = None

	@property
	def InftvTaxDtls(self):
		return self._InftvTaxDtls

	@InftvTaxDtls.setter
	def InftvTaxDtls(self, value):
		self._InftvTaxDtls = value if type(value) != base_types.auto else self.make_default("InftvTaxDtls")

	@InftvTaxDtls.deleter
	def InftvTaxDtls(self):
		del self._InftvTaxDtls
		self._InftvTaxDtls = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='PhysDlvryDtls', type=DeliveryParameters3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Grp1Or2Units', type=UKTaxGroupUnit1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SttlmAndCtdyDtls', type=FundSettlementParameters11, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FinInstrmDtls', type=FinancialInstrument57, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PhysDlvryInd', type=YesNoIndicator, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InvstmtAcctDtls', type=InvestmentAccount58, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IntrmPrftAmt', type=ProfitAndLoss2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UnitsNb', type=DecimalNumber, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='GrssAmt', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxOvrhd', type=TotalFeesAndTaxes40, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InftvPricDtls', type=UnitPrice22, min=0, max=2, mutex_group=None, array=True),
		base_types.FieldEntry(name='ReqdNAVCcy', type=ActiveOrHistoricCurrencyCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LegId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NetAmt', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ReqdSttlmCcy', type=ActiveCurrencyCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='GtgOrHldBckDtls', type=HoldBackInformation2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='HldgsRedRate', type=PercentageRate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NonStdSttlmInf', type=Max350Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Equlstn', type=Equalisation1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LegExctnId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CumDvddInd', type=YesNoIndicator, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PricDtls', type=UnitPrice22, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IncmPref', type=IncomePreference1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TradDtTm', type=DateAndDateTimeChoice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InftvTaxDtls', type=InformativeTax1, min=0, max=1, mutex_group=None, array=False),
	))

