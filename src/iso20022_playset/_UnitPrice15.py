# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActiveOrHistoricCurrencyAnd13DecimalAmount
from . import Charge15
from . import EUDividendStatus1Code
from . import Extended350Code
from . import Number
from . import PercentageRate
from . import PriceMethod1Code
from . import PriceValue1
from . import Tax17
from . import TaxableIncomePerShareCalculated2Code
from . import TypeOfPrice9Code
from . import YesNoIndicator

class UnitPrice15(base_types._BaseFieldType):

	__slots__ = ["_ChrgDtls", "_ClctnBsis", "_CumDvddInd", "_EUDvddSts", "_EstmtdPricInd", "_ForExctnInd", "_NbOfDaysAcrd", "_PricMtd", "_TaxLbltyDtls", "_TaxRfndDtls", "_TaxblIncmPerDvdd", "_TaxblIncmPerShr", "_TaxblIncmPerShrClctd", "_Tp", "_ValInAltrntvCcy", "_ValInInvstmtCcy", "_XtndedEUDvddSts", "_XtndedTaxblIncmPerShrClctd", "_XtndedTp"]
	@property
	def ChrgDtls(self):
		return self._ChrgDtls

	@ChrgDtls.setter
	def ChrgDtls(self, value):
		self._ChrgDtls = value if value is not None else base_types.UninitialisedField(self, 'ChrgDtls', Charge15, True)

	@ChrgDtls.deleter
	def ChrgDtls(self):
		del self._ChrgDtls
		self._ChrgDtls = base_types.UninitialisedField(self, 'ChrgDtls', Charge15, True)

	@property
	def ClctnBsis(self):
		return self._ClctnBsis

	@ClctnBsis.setter
	def ClctnBsis(self, value):
		self._ClctnBsis = value if value is not None else base_types.UninitialisedField(self, 'ClctnBsis', PercentageRate, False)

	@ClctnBsis.deleter
	def ClctnBsis(self):
		del self._ClctnBsis
		self._ClctnBsis = base_types.UninitialisedField(self, 'ClctnBsis', PercentageRate, False)

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
	def EUDvddSts(self):
		return self._EUDvddSts

	@EUDvddSts.setter
	def EUDvddSts(self, value):
		self._EUDvddSts = value if value is not None else base_types.UninitialisedField(self, 'EUDvddSts', EUDividendStatus1Code, False)

	@EUDvddSts.deleter
	def EUDvddSts(self):
		del self._EUDvddSts
		self._EUDvddSts = base_types.UninitialisedField(self, 'EUDvddSts', EUDividendStatus1Code, False)

	@property
	def EstmtdPricInd(self):
		return self._EstmtdPricInd

	@EstmtdPricInd.setter
	def EstmtdPricInd(self, value):
		self._EstmtdPricInd = value if value is not None else base_types.UninitialisedField(self, 'EstmtdPricInd', YesNoIndicator, False)

	@EstmtdPricInd.deleter
	def EstmtdPricInd(self):
		del self._EstmtdPricInd
		self._EstmtdPricInd = base_types.UninitialisedField(self, 'EstmtdPricInd', YesNoIndicator, False)

	@property
	def ForExctnInd(self):
		return self._ForExctnInd

	@ForExctnInd.setter
	def ForExctnInd(self, value):
		self._ForExctnInd = value if value is not None else base_types.UninitialisedField(self, 'ForExctnInd', YesNoIndicator, False)

	@ForExctnInd.deleter
	def ForExctnInd(self):
		del self._ForExctnInd
		self._ForExctnInd = base_types.UninitialisedField(self, 'ForExctnInd', YesNoIndicator, False)

	@property
	def NbOfDaysAcrd(self):
		return self._NbOfDaysAcrd

	@NbOfDaysAcrd.setter
	def NbOfDaysAcrd(self, value):
		self._NbOfDaysAcrd = value if value is not None else base_types.UninitialisedField(self, 'NbOfDaysAcrd', Number, False)

	@NbOfDaysAcrd.deleter
	def NbOfDaysAcrd(self):
		del self._NbOfDaysAcrd
		self._NbOfDaysAcrd = base_types.UninitialisedField(self, 'NbOfDaysAcrd', Number, False)

	@property
	def PricMtd(self):
		return self._PricMtd

	@PricMtd.setter
	def PricMtd(self, value):
		self._PricMtd = value if value is not None else base_types.UninitialisedField(self, 'PricMtd', PriceMethod1Code, False)

	@PricMtd.deleter
	def PricMtd(self):
		del self._PricMtd
		self._PricMtd = base_types.UninitialisedField(self, 'PricMtd', PriceMethod1Code, False)

	@property
	def TaxLbltyDtls(self):
		return self._TaxLbltyDtls

	@TaxLbltyDtls.setter
	def TaxLbltyDtls(self, value):
		self._TaxLbltyDtls = value if value is not None else base_types.UninitialisedField(self, 'TaxLbltyDtls', Tax17, True)

	@TaxLbltyDtls.deleter
	def TaxLbltyDtls(self):
		del self._TaxLbltyDtls
		self._TaxLbltyDtls = base_types.UninitialisedField(self, 'TaxLbltyDtls', Tax17, True)

	@property
	def TaxRfndDtls(self):
		return self._TaxRfndDtls

	@TaxRfndDtls.setter
	def TaxRfndDtls(self, value):
		self._TaxRfndDtls = value if value is not None else base_types.UninitialisedField(self, 'TaxRfndDtls', Tax17, True)

	@TaxRfndDtls.deleter
	def TaxRfndDtls(self):
		del self._TaxRfndDtls
		self._TaxRfndDtls = base_types.UninitialisedField(self, 'TaxRfndDtls', Tax17, True)

	@property
	def TaxblIncmPerDvdd(self):
		return self._TaxblIncmPerDvdd

	@TaxblIncmPerDvdd.setter
	def TaxblIncmPerDvdd(self, value):
		self._TaxblIncmPerDvdd = value if value is not None else base_types.UninitialisedField(self, 'TaxblIncmPerDvdd', ActiveOrHistoricCurrencyAnd13DecimalAmount, False)

	@TaxblIncmPerDvdd.deleter
	def TaxblIncmPerDvdd(self):
		del self._TaxblIncmPerDvdd
		self._TaxblIncmPerDvdd = base_types.UninitialisedField(self, 'TaxblIncmPerDvdd', ActiveOrHistoricCurrencyAnd13DecimalAmount, False)

	@property
	def TaxblIncmPerShr(self):
		return self._TaxblIncmPerShr

	@TaxblIncmPerShr.setter
	def TaxblIncmPerShr(self, value):
		self._TaxblIncmPerShr = value if value is not None else base_types.UninitialisedField(self, 'TaxblIncmPerShr', ActiveOrHistoricCurrencyAnd13DecimalAmount, False)

	@TaxblIncmPerShr.deleter
	def TaxblIncmPerShr(self):
		del self._TaxblIncmPerShr
		self._TaxblIncmPerShr = base_types.UninitialisedField(self, 'TaxblIncmPerShr', ActiveOrHistoricCurrencyAnd13DecimalAmount, False)

	@property
	def TaxblIncmPerShrClctd(self):
		return self._TaxblIncmPerShrClctd

	@TaxblIncmPerShrClctd.setter
	def TaxblIncmPerShrClctd(self, value):
		self._TaxblIncmPerShrClctd = value if value is not None else base_types.UninitialisedField(self, 'TaxblIncmPerShrClctd', TaxableIncomePerShareCalculated2Code, False)

	@TaxblIncmPerShrClctd.deleter
	def TaxblIncmPerShrClctd(self):
		del self._TaxblIncmPerShrClctd
		self._TaxblIncmPerShrClctd = base_types.UninitialisedField(self, 'TaxblIncmPerShrClctd', TaxableIncomePerShareCalculated2Code, False)

	@property
	def Tp(self):
		return self._Tp

	@Tp.setter
	def Tp(self, value):
		self._Tp = value if value is not None else base_types.UninitialisedField(self, 'Tp', TypeOfPrice9Code, False)

	@Tp.deleter
	def Tp(self):
		del self._Tp
		self._Tp = base_types.UninitialisedField(self, 'Tp', TypeOfPrice9Code, False)

	@property
	def ValInAltrntvCcy(self):
		return self._ValInAltrntvCcy

	@ValInAltrntvCcy.setter
	def ValInAltrntvCcy(self, value):
		self._ValInAltrntvCcy = value if value is not None else base_types.UninitialisedField(self, 'ValInAltrntvCcy', PriceValue1, True)

	@ValInAltrntvCcy.deleter
	def ValInAltrntvCcy(self):
		del self._ValInAltrntvCcy
		self._ValInAltrntvCcy = base_types.UninitialisedField(self, 'ValInAltrntvCcy', PriceValue1, True)

	@property
	def ValInInvstmtCcy(self):
		return self._ValInInvstmtCcy

	@ValInInvstmtCcy.setter
	def ValInInvstmtCcy(self, value):
		self._ValInInvstmtCcy = value if value is not None else base_types.UninitialisedField(self, 'ValInInvstmtCcy', PriceValue1, True)

	@ValInInvstmtCcy.deleter
	def ValInInvstmtCcy(self):
		del self._ValInInvstmtCcy
		self._ValInInvstmtCcy = base_types.UninitialisedField(self, 'ValInInvstmtCcy', PriceValue1, True)

	@property
	def XtndedEUDvddSts(self):
		return self._XtndedEUDvddSts

	@XtndedEUDvddSts.setter
	def XtndedEUDvddSts(self, value):
		self._XtndedEUDvddSts = value if value is not None else base_types.UninitialisedField(self, 'XtndedEUDvddSts', Extended350Code, False)

	@XtndedEUDvddSts.deleter
	def XtndedEUDvddSts(self):
		del self._XtndedEUDvddSts
		self._XtndedEUDvddSts = base_types.UninitialisedField(self, 'XtndedEUDvddSts', Extended350Code, False)

	@property
	def XtndedTaxblIncmPerShrClctd(self):
		return self._XtndedTaxblIncmPerShrClctd

	@XtndedTaxblIncmPerShrClctd.setter
	def XtndedTaxblIncmPerShrClctd(self, value):
		self._XtndedTaxblIncmPerShrClctd = value if value is not None else base_types.UninitialisedField(self, 'XtndedTaxblIncmPerShrClctd', Extended350Code, False)

	@XtndedTaxblIncmPerShrClctd.deleter
	def XtndedTaxblIncmPerShrClctd(self):
		del self._XtndedTaxblIncmPerShrClctd
		self._XtndedTaxblIncmPerShrClctd = base_types.UninitialisedField(self, 'XtndedTaxblIncmPerShrClctd', Extended350Code, False)

	@property
	def XtndedTp(self):
		return self._XtndedTp

	@XtndedTp.setter
	def XtndedTp(self, value):
		self._XtndedTp = value if value is not None else base_types.UninitialisedField(self, 'XtndedTp', Extended350Code, False)

	@XtndedTp.deleter
	def XtndedTp(self):
		del self._XtndedTp
		self._XtndedTp = base_types.UninitialisedField(self, 'XtndedTp', Extended350Code, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='ChrgDtls', type=Charge15, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='ClctnBsis', type=PercentageRate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CumDvddInd', type=YesNoIndicator, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='EUDvddSts', type=EUDividendStatus1Code, min=0, max=1, mutex_group=3, array=False),
		base_types.FieldEntry(name='EstmtdPricInd', type=YesNoIndicator, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ForExctnInd', type=YesNoIndicator, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NbOfDaysAcrd', type=Number, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PricMtd', type=PriceMethod1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TaxLbltyDtls', type=Tax17, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='TaxRfndDtls', type=Tax17, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='TaxblIncmPerDvdd', type=ActiveOrHistoricCurrencyAnd13DecimalAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TaxblIncmPerShr', type=ActiveOrHistoricCurrencyAnd13DecimalAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TaxblIncmPerShrClctd', type=TaxableIncomePerShareCalculated2Code, min=0, max=1, mutex_group=2, array=False),
		base_types.FieldEntry(name='Tp', type=TypeOfPrice9Code, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='ValInAltrntvCcy', type=PriceValue1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='ValInInvstmtCcy', type=PriceValue1, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='XtndedEUDvddSts', type=Extended350Code, min=0, max=1, mutex_group=3, array=False),
		base_types.FieldEntry(name='XtndedTaxblIncmPerShrClctd', type=Extended350Code, min=0, max=1, mutex_group=2, array=False),
		base_types.FieldEntry(name='XtndedTp', type=Extended350Code, min=0, max=1, mutex_group=1, array=False),
	))