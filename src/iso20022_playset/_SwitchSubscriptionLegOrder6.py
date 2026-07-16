# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActiveCurrencyCode
from . import ActiveOrHistoricCurrencyCode
from . import Equalisation1
from . import FeeAndTax1
from . import FinancialInstrument57
from . import FinancialInstrumentQuantity26Choice
from . import FundSettlementParameters11
from . import IncomePreference1Code
from . import InvestmentAccount58
from . import Max350Text
from . import Max35Text
from . import NameAndAddress4
from . import YesNoIndicator

class SwitchSubscriptionLegOrder6(base_types._BaseFieldType):

	__slots__ = ["_Equlstn", "_FinInstrmDtls", "_FinInstrmQtyChc", "_IncmPref", "_InvstmtAcctDtls", "_LegId", "_NonStdSttlmInf", "_PhysDlvryDtls", "_PhysDlvryInd", "_ReqdNAVCcy", "_ReqdSttlmCcy", "_SttlmAndCtdyDtls", "_TxOvrhd"]
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
		self._FinInstrmDtls = value if value is not None else base_types.UninitialisedField(self, 'FinInstrmDtls', FinancialInstrument57, False)

	@FinInstrmDtls.deleter
	def FinInstrmDtls(self):
		del self._FinInstrmDtls
		self._FinInstrmDtls = base_types.UninitialisedField(self, 'FinInstrmDtls', FinancialInstrument57, False)

	@property
	def FinInstrmQtyChc(self):
		return self._FinInstrmQtyChc

	@FinInstrmQtyChc.setter
	def FinInstrmQtyChc(self, value):
		self._FinInstrmQtyChc = value if value is not None else base_types.UninitialisedField(self, 'FinInstrmQtyChc', FinancialInstrumentQuantity26Choice, False)

	@FinInstrmQtyChc.deleter
	def FinInstrmQtyChc(self):
		del self._FinInstrmQtyChc
		self._FinInstrmQtyChc = base_types.UninitialisedField(self, 'FinInstrmQtyChc', FinancialInstrumentQuantity26Choice, False)

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
	def InvstmtAcctDtls(self):
		return self._InvstmtAcctDtls

	@InvstmtAcctDtls.setter
	def InvstmtAcctDtls(self, value):
		self._InvstmtAcctDtls = value if value is not None else base_types.UninitialisedField(self, 'InvstmtAcctDtls', InvestmentAccount58, False)

	@InvstmtAcctDtls.deleter
	def InvstmtAcctDtls(self):
		del self._InvstmtAcctDtls
		self._InvstmtAcctDtls = base_types.UninitialisedField(self, 'InvstmtAcctDtls', InvestmentAccount58, False)

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
		self._PhysDlvryDtls = value if value is not None else base_types.UninitialisedField(self, 'PhysDlvryDtls', NameAndAddress4, False)

	@PhysDlvryDtls.deleter
	def PhysDlvryDtls(self):
		del self._PhysDlvryDtls
		self._PhysDlvryDtls = base_types.UninitialisedField(self, 'PhysDlvryDtls', NameAndAddress4, False)

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
		self._SttlmAndCtdyDtls = value if value is not None else base_types.UninitialisedField(self, 'SttlmAndCtdyDtls', FundSettlementParameters11, False)

	@SttlmAndCtdyDtls.deleter
	def SttlmAndCtdyDtls(self):
		del self._SttlmAndCtdyDtls
		self._SttlmAndCtdyDtls = base_types.UninitialisedField(self, 'SttlmAndCtdyDtls', FundSettlementParameters11, False)

	@property
	def TxOvrhd(self):
		return self._TxOvrhd

	@TxOvrhd.setter
	def TxOvrhd(self, value):
		self._TxOvrhd = value if value is not None else base_types.UninitialisedField(self, 'TxOvrhd', FeeAndTax1, False)

	@TxOvrhd.deleter
	def TxOvrhd(self):
		del self._TxOvrhd
		self._TxOvrhd = base_types.UninitialisedField(self, 'TxOvrhd', FeeAndTax1, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Equlstn', type=Equalisation1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FinInstrmDtls', type=FinancialInstrument57, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FinInstrmQtyChc', type=FinancialInstrumentQuantity26Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IncmPref', type=IncomePreference1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InvstmtAcctDtls', type=InvestmentAccount58, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LegId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NonStdSttlmInf', type=Max350Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PhysDlvryDtls', type=NameAndAddress4, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PhysDlvryInd', type=YesNoIndicator, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ReqdNAVCcy', type=ActiveOrHistoricCurrencyCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ReqdSttlmCcy', type=ActiveCurrencyCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SttlmAndCtdyDtls', type=FundSettlementParameters11, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxOvrhd', type=FeeAndTax1, min=0, max=1, mutex_group=None, array=False),
	))