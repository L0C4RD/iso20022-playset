# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._ActiveCurrencyCode import ActiveCurrencyCode
from ._ActiveOrHistoricCurrencyCode import ActiveOrHistoricCurrencyCode
from ._DeliveryParameters3 import DeliveryParameters3
from ._DigitalPaymentSettlement3 import DigitalPaymentSettlement3
from ._Equalisation1 import Equalisation1
from ._FeeAndTax2 import FeeAndTax2
from ._FinancialInstrument107 import FinancialInstrument107
from ._FinancialInstrumentQuantity50Choice import FinancialInstrumentQuantity50Choice
from ._FundSettlementParameters28 import FundSettlementParameters28
from ._IncomePreference1Code import IncomePreference1Code
from ._InvestmentAccount81 import InvestmentAccount81
from ._Max350Text import Max350Text
from ._Max35Text import Max35Text
from ._UKTaxGroupUnit1Code import UKTaxGroupUnit1Code
from ._YesNoIndicator import YesNoIndicator

class SwitchRedemptionLegOrder7(base_types._BaseFieldType):

	__slots__ = ["_DgtlAsstSttlm", "_Equlstn", "_FinInstrmDtls", "_FinInstrmQtyChc", "_Grp1Or2Units", "_IncmPref", "_InvstmtAcctDtls", "_LegId", "_NonStdSttlmInf", "_PhysDlvryDtls", "_PhysDlvryInd", "_ReqdNAVCcy", "_ReqdSttlmCcy", "_SttlmAndCtdyDtls", "_TxOvrhd"]
	@property
	def DgtlAsstSttlm(self):
		return self._DgtlAsstSttlm

	@DgtlAsstSttlm.setter
	def DgtlAsstSttlm(self, value):
		self._DgtlAsstSttlm = value if type(value) != base_types.auto else self.make_default("DgtlAsstSttlm")

	@DgtlAsstSttlm.deleter
	def DgtlAsstSttlm(self):
		del self._DgtlAsstSttlm
		self._DgtlAsstSttlm = None

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
	def FinInstrmQtyChc(self):
		return self._FinInstrmQtyChc

	@FinInstrmQtyChc.setter
	def FinInstrmQtyChc(self, value):
		self._FinInstrmQtyChc = value if type(value) != base_types.auto else self.make_default("FinInstrmQtyChc")

	@FinInstrmQtyChc.deleter
	def FinInstrmQtyChc(self):
		del self._FinInstrmQtyChc
		self._FinInstrmQtyChc = None

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
	def TxOvrhd(self):
		return self._TxOvrhd

	@TxOvrhd.setter
	def TxOvrhd(self, value):
		self._TxOvrhd = value if type(value) != base_types.auto else self.make_default("TxOvrhd")

	@TxOvrhd.deleter
	def TxOvrhd(self):
		del self._TxOvrhd
		self._TxOvrhd = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='DgtlAsstSttlm', type=DigitalPaymentSettlement3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Equlstn', type=Equalisation1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FinInstrmDtls', type=FinancialInstrument107, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FinInstrmQtyChc', type=FinancialInstrumentQuantity50Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Grp1Or2Units', type=UKTaxGroupUnit1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IncmPref', type=IncomePreference1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InvstmtAcctDtls', type=InvestmentAccount81, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LegId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NonStdSttlmInf', type=Max350Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PhysDlvryDtls', type=DeliveryParameters3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PhysDlvryInd', type=YesNoIndicator, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ReqdNAVCcy', type=ActiveOrHistoricCurrencyCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ReqdSttlmCcy', type=ActiveCurrencyCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SttlmAndCtdyDtls', type=FundSettlementParameters28, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxOvrhd', type=FeeAndTax2, min=0, max=1, mutex_group=None, array=False),
	))