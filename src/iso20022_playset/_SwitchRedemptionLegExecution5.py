# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActiveCurrencyAndAmount
from . import ActiveCurrencyCode
from . import ActiveOrHistoricCurrencyCode
from . import DateAndDateTime2Choice
from . import DeliveryParameters3
from . import DigitalPaymentSettlement3
from . import Equalisation1
from . import FinancialInstrument107
from . import FundSettlementParameters22
from . import HoldBackInformation5
from . import IncomePreference1Code
from . import InformativeTax2
from . import InvestmentAccount81
from . import Max350Text
from . import Max35Text
from . import PercentageRate
from . import ProfitAndLoss2Choice
from . import TotalFeesAndTaxes44
from . import UKTaxGroupUnit1Code
from . import Unit1Choice
from . import UnitPrice22
from . import YesNoIndicator

class SwitchRedemptionLegExecution5(base_types._BaseFieldType):

	__slots__ = ["_CumDvddInd", "_DgtlAsstSttlm", "_Equlstn", "_FinInstrmDtls", "_Grp1Or2Units", "_GrssAmt", "_GtgOrHldBckDtls", "_HldgsRedRate", "_IncmPref", "_InftvPricDtls", "_InftvTaxDtls", "_IntrmPrftAmt", "_InvstmtAcctDtls", "_LegExctnId", "_LegId", "_NetAmt", "_NonStdSttlmInf", "_PhysDlvryDtls", "_PhysDlvryInd", "_PricDtls", "_ReqdNAVCcy", "_ReqdSttlmCcy", "_SttlmAndCtdyDtls", "_TradDtTm", "_TxOvrhd", "_Units"]
	@property
	def CumDvddInd(self):
		return self._CumDvddInd

	@CumDvddInd.setter
	def CumDvddInd(self, value):
		self._CumDvddInd = value if value is not None else base_types.UninitialisedField(self, 'CumDvddInd', YesNoIndicator, False)

	@CumDvddInd.deleter
	def CumDvddInd(self):
		del self._CumDvddInd
		self._CumDvddInd = base_types.UninitialisedField(self, 'CumDvddInd', YesNoIndicator, False)

	@property
	def DgtlAsstSttlm(self):
		return self._DgtlAsstSttlm

	@DgtlAsstSttlm.setter
	def DgtlAsstSttlm(self, value):
		self._DgtlAsstSttlm = value if value is not None else base_types.UninitialisedField(self, 'DgtlAsstSttlm', DigitalPaymentSettlement3, False)

	@DgtlAsstSttlm.deleter
	def DgtlAsstSttlm(self):
		del self._DgtlAsstSttlm
		self._DgtlAsstSttlm = base_types.UninitialisedField(self, 'DgtlAsstSttlm', DigitalPaymentSettlement3, False)

	@property
	def Equlstn(self):
		return self._Equlstn

	@Equlstn.setter
	def Equlstn(self, value):
		self._Equlstn = value if value is not None else base_types.UninitialisedField(self, 'Equlstn', Equalisation1, False)

	@Equlstn.deleter
	def Equlstn(self):
		del self._Equlstn
		self._Equlstn = base_types.UninitialisedField(self, 'Equlstn', Equalisation1, False)

	@property
	def FinInstrmDtls(self):
		return self._FinInstrmDtls

	@FinInstrmDtls.setter
	def FinInstrmDtls(self, value):
		self._FinInstrmDtls = value if value is not None else base_types.UninitialisedField(self, 'FinInstrmDtls', FinancialInstrument107, False)

	@FinInstrmDtls.deleter
	def FinInstrmDtls(self):
		del self._FinInstrmDtls
		self._FinInstrmDtls = base_types.UninitialisedField(self, 'FinInstrmDtls', FinancialInstrument107, False)

	@property
	def Grp1Or2Units(self):
		return self._Grp1Or2Units

	@Grp1Or2Units.setter
	def Grp1Or2Units(self, value):
		self._Grp1Or2Units = value if value is not None else base_types.UninitialisedField(self, 'Grp1Or2Units', UKTaxGroupUnit1Code, False)

	@Grp1Or2Units.deleter
	def Grp1Or2Units(self):
		del self._Grp1Or2Units
		self._Grp1Or2Units = base_types.UninitialisedField(self, 'Grp1Or2Units', UKTaxGroupUnit1Code, False)

	@property
	def GrssAmt(self):
		return self._GrssAmt

	@GrssAmt.setter
	def GrssAmt(self, value):
		self._GrssAmt = value if value is not None else base_types.UninitialisedField(self, 'GrssAmt', ActiveCurrencyAndAmount, False)

	@GrssAmt.deleter
	def GrssAmt(self):
		del self._GrssAmt
		self._GrssAmt = base_types.UninitialisedField(self, 'GrssAmt', ActiveCurrencyAndAmount, False)

	@property
	def GtgOrHldBckDtls(self):
		return self._GtgOrHldBckDtls

	@GtgOrHldBckDtls.setter
	def GtgOrHldBckDtls(self, value):
		self._GtgOrHldBckDtls = value if value is not None else base_types.UninitialisedField(self, 'GtgOrHldBckDtls', HoldBackInformation5, False)

	@GtgOrHldBckDtls.deleter
	def GtgOrHldBckDtls(self):
		del self._GtgOrHldBckDtls
		self._GtgOrHldBckDtls = base_types.UninitialisedField(self, 'GtgOrHldBckDtls', HoldBackInformation5, False)

	@property
	def HldgsRedRate(self):
		return self._HldgsRedRate

	@HldgsRedRate.setter
	def HldgsRedRate(self, value):
		self._HldgsRedRate = value if value is not None else base_types.UninitialisedField(self, 'HldgsRedRate', PercentageRate, False)

	@HldgsRedRate.deleter
	def HldgsRedRate(self):
		del self._HldgsRedRate
		self._HldgsRedRate = base_types.UninitialisedField(self, 'HldgsRedRate', PercentageRate, False)

	@property
	def IncmPref(self):
		return self._IncmPref

	@IncmPref.setter
	def IncmPref(self, value):
		self._IncmPref = value if value is not None else base_types.UninitialisedField(self, 'IncmPref', IncomePreference1Code, False)

	@IncmPref.deleter
	def IncmPref(self):
		del self._IncmPref
		self._IncmPref = base_types.UninitialisedField(self, 'IncmPref', IncomePreference1Code, False)

	@property
	def InftvPricDtls(self):
		return self._InftvPricDtls

	@InftvPricDtls.setter
	def InftvPricDtls(self, value):
		self._InftvPricDtls = value if value is not None else base_types.UninitialisedField(self, 'InftvPricDtls', UnitPrice22, True)

	@InftvPricDtls.deleter
	def InftvPricDtls(self):
		del self._InftvPricDtls
		self._InftvPricDtls = base_types.UninitialisedField(self, 'InftvPricDtls', UnitPrice22, True)

	@property
	def InftvTaxDtls(self):
		return self._InftvTaxDtls

	@InftvTaxDtls.setter
	def InftvTaxDtls(self, value):
		self._InftvTaxDtls = value if value is not None else base_types.UninitialisedField(self, 'InftvTaxDtls', InformativeTax2, False)

	@InftvTaxDtls.deleter
	def InftvTaxDtls(self):
		del self._InftvTaxDtls
		self._InftvTaxDtls = base_types.UninitialisedField(self, 'InftvTaxDtls', InformativeTax2, False)

	@property
	def IntrmPrftAmt(self):
		return self._IntrmPrftAmt

	@IntrmPrftAmt.setter
	def IntrmPrftAmt(self, value):
		self._IntrmPrftAmt = value if value is not None else base_types.UninitialisedField(self, 'IntrmPrftAmt', ProfitAndLoss2Choice, False)

	@IntrmPrftAmt.deleter
	def IntrmPrftAmt(self):
		del self._IntrmPrftAmt
		self._IntrmPrftAmt = base_types.UninitialisedField(self, 'IntrmPrftAmt', ProfitAndLoss2Choice, False)

	@property
	def InvstmtAcctDtls(self):
		return self._InvstmtAcctDtls

	@InvstmtAcctDtls.setter
	def InvstmtAcctDtls(self, value):
		self._InvstmtAcctDtls = value if value is not None else base_types.UninitialisedField(self, 'InvstmtAcctDtls', InvestmentAccount81, False)

	@InvstmtAcctDtls.deleter
	def InvstmtAcctDtls(self):
		del self._InvstmtAcctDtls
		self._InvstmtAcctDtls = base_types.UninitialisedField(self, 'InvstmtAcctDtls', InvestmentAccount81, False)

	@property
	def LegExctnId(self):
		return self._LegExctnId

	@LegExctnId.setter
	def LegExctnId(self, value):
		self._LegExctnId = value if value is not None else base_types.UninitialisedField(self, 'LegExctnId', Max35Text, False)

	@LegExctnId.deleter
	def LegExctnId(self):
		del self._LegExctnId
		self._LegExctnId = base_types.UninitialisedField(self, 'LegExctnId', Max35Text, False)

	@property
	def LegId(self):
		return self._LegId

	@LegId.setter
	def LegId(self, value):
		self._LegId = value if value is not None else base_types.UninitialisedField(self, 'LegId', Max35Text, False)

	@LegId.deleter
	def LegId(self):
		del self._LegId
		self._LegId = base_types.UninitialisedField(self, 'LegId', Max35Text, False)

	@property
	def NetAmt(self):
		return self._NetAmt

	@NetAmt.setter
	def NetAmt(self, value):
		self._NetAmt = value if value is not None else base_types.UninitialisedField(self, 'NetAmt', ActiveCurrencyAndAmount, False)

	@NetAmt.deleter
	def NetAmt(self):
		del self._NetAmt
		self._NetAmt = base_types.UninitialisedField(self, 'NetAmt', ActiveCurrencyAndAmount, False)

	@property
	def NonStdSttlmInf(self):
		return self._NonStdSttlmInf

	@NonStdSttlmInf.setter
	def NonStdSttlmInf(self, value):
		self._NonStdSttlmInf = value if value is not None else base_types.UninitialisedField(self, 'NonStdSttlmInf', Max350Text, False)

	@NonStdSttlmInf.deleter
	def NonStdSttlmInf(self):
		del self._NonStdSttlmInf
		self._NonStdSttlmInf = base_types.UninitialisedField(self, 'NonStdSttlmInf', Max350Text, False)

	@property
	def PhysDlvryDtls(self):
		return self._PhysDlvryDtls

	@PhysDlvryDtls.setter
	def PhysDlvryDtls(self, value):
		self._PhysDlvryDtls = value if value is not None else base_types.UninitialisedField(self, 'PhysDlvryDtls', DeliveryParameters3, False)

	@PhysDlvryDtls.deleter
	def PhysDlvryDtls(self):
		del self._PhysDlvryDtls
		self._PhysDlvryDtls = base_types.UninitialisedField(self, 'PhysDlvryDtls', DeliveryParameters3, False)

	@property
	def PhysDlvryInd(self):
		return self._PhysDlvryInd

	@PhysDlvryInd.setter
	def PhysDlvryInd(self, value):
		self._PhysDlvryInd = value if value is not None else base_types.UninitialisedField(self, 'PhysDlvryInd', YesNoIndicator, False)

	@PhysDlvryInd.deleter
	def PhysDlvryInd(self):
		del self._PhysDlvryInd
		self._PhysDlvryInd = base_types.UninitialisedField(self, 'PhysDlvryInd', YesNoIndicator, False)

	@property
	def PricDtls(self):
		return self._PricDtls

	@PricDtls.setter
	def PricDtls(self, value):
		self._PricDtls = value if value is not None else base_types.UninitialisedField(self, 'PricDtls', UnitPrice22, False)

	@PricDtls.deleter
	def PricDtls(self):
		del self._PricDtls
		self._PricDtls = base_types.UninitialisedField(self, 'PricDtls', UnitPrice22, False)

	@property
	def ReqdNAVCcy(self):
		return self._ReqdNAVCcy

	@ReqdNAVCcy.setter
	def ReqdNAVCcy(self, value):
		self._ReqdNAVCcy = value if value is not None else base_types.UninitialisedField(self, 'ReqdNAVCcy', ActiveOrHistoricCurrencyCode, False)

	@ReqdNAVCcy.deleter
	def ReqdNAVCcy(self):
		del self._ReqdNAVCcy
		self._ReqdNAVCcy = base_types.UninitialisedField(self, 'ReqdNAVCcy', ActiveOrHistoricCurrencyCode, False)

	@property
	def ReqdSttlmCcy(self):
		return self._ReqdSttlmCcy

	@ReqdSttlmCcy.setter
	def ReqdSttlmCcy(self, value):
		self._ReqdSttlmCcy = value if value is not None else base_types.UninitialisedField(self, 'ReqdSttlmCcy', ActiveCurrencyCode, False)

	@ReqdSttlmCcy.deleter
	def ReqdSttlmCcy(self):
		del self._ReqdSttlmCcy
		self._ReqdSttlmCcy = base_types.UninitialisedField(self, 'ReqdSttlmCcy', ActiveCurrencyCode, False)

	@property
	def SttlmAndCtdyDtls(self):
		return self._SttlmAndCtdyDtls

	@SttlmAndCtdyDtls.setter
	def SttlmAndCtdyDtls(self, value):
		self._SttlmAndCtdyDtls = value if value is not None else base_types.UninitialisedField(self, 'SttlmAndCtdyDtls', FundSettlementParameters22, False)

	@SttlmAndCtdyDtls.deleter
	def SttlmAndCtdyDtls(self):
		del self._SttlmAndCtdyDtls
		self._SttlmAndCtdyDtls = base_types.UninitialisedField(self, 'SttlmAndCtdyDtls', FundSettlementParameters22, False)

	@property
	def TradDtTm(self):
		return self._TradDtTm

	@TradDtTm.setter
	def TradDtTm(self, value):
		self._TradDtTm = value if value is not None else base_types.UninitialisedField(self, 'TradDtTm', DateAndDateTime2Choice, False)

	@TradDtTm.deleter
	def TradDtTm(self):
		del self._TradDtTm
		self._TradDtTm = base_types.UninitialisedField(self, 'TradDtTm', DateAndDateTime2Choice, False)

	@property
	def TxOvrhd(self):
		return self._TxOvrhd

	@TxOvrhd.setter
	def TxOvrhd(self, value):
		self._TxOvrhd = value if value is not None else base_types.UninitialisedField(self, 'TxOvrhd', TotalFeesAndTaxes44, False)

	@TxOvrhd.deleter
	def TxOvrhd(self):
		del self._TxOvrhd
		self._TxOvrhd = base_types.UninitialisedField(self, 'TxOvrhd', TotalFeesAndTaxes44, False)

	@property
	def Units(self):
		return self._Units

	@Units.setter
	def Units(self, value):
		self._Units = value if value is not None else base_types.UninitialisedField(self, 'Units', Unit1Choice, False)

	@Units.deleter
	def Units(self):
		del self._Units
		self._Units = base_types.UninitialisedField(self, 'Units', Unit1Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='CumDvddInd', type=YesNoIndicator, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DgtlAsstSttlm', type=DigitalPaymentSettlement3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Equlstn', type=Equalisation1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FinInstrmDtls', type=FinancialInstrument107, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Grp1Or2Units', type=UKTaxGroupUnit1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='GrssAmt', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='GtgOrHldBckDtls', type=HoldBackInformation5, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='HldgsRedRate', type=PercentageRate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IncmPref', type=IncomePreference1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InftvPricDtls', type=UnitPrice22, min=0, max=2, mutex_group=None, array=True),
		base_types.FieldEntry(name='InftvTaxDtls', type=InformativeTax2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IntrmPrftAmt', type=ProfitAndLoss2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InvstmtAcctDtls', type=InvestmentAccount81, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LegExctnId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LegId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NetAmt', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NonStdSttlmInf', type=Max350Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PhysDlvryDtls', type=DeliveryParameters3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PhysDlvryInd', type=YesNoIndicator, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PricDtls', type=UnitPrice22, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ReqdNAVCcy', type=ActiveOrHistoricCurrencyCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ReqdSttlmCcy', type=ActiveCurrencyCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SttlmAndCtdyDtls', type=FundSettlementParameters22, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TradDtTm', type=DateAndDateTime2Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxOvrhd', type=TotalFeesAndTaxes44, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Units', type=Unit1Choice, min=1, max=1, mutex_group=None, array=False),
	))