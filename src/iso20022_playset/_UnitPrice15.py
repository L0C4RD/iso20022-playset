from . import base_types
from ._Number import Number
from ._TypeOfPrice9Code import TypeOfPrice9Code
from ._EUDividendStatus1Code import EUDividendStatus1Code
from ._ActiveOrHistoricCurrencyAnd13DecimalAmount import ActiveOrHistoricCurrencyAnd13DecimalAmount
from ._PriceMethod1Code import PriceMethod1Code
from ._Charge15 import Charge15
from ._PercentageRate import PercentageRate
from ._Tax17 import Tax17
from ._TaxableIncomePerShareCalculated2Code import TaxableIncomePerShareCalculated2Code
from ._PriceValue1 import PriceValue1
from ._Extended350Code import Extended350Code
from ._YesNoIndicator import YesNoIndicator

class UnitPrice15(base_types._BaseFieldType):

	__slots__ = ["_XtndedEUDvddSts", "_ValInAltrntvCcy", "_XtndedTp", "_EUDvddSts", "_CumDvddInd", "_ChrgDtls", "_TaxLbltyDtls", "_EstmtdPricInd", "_TaxRfndDtls", "_ClctnBsis", "_XtndedTaxblIncmPerShrClctd", "_PricMtd", "_ValInInvstmtCcy", "_Tp", "_TaxblIncmPerDvdd", "_NbOfDaysAcrd", "_TaxblIncmPerShrClctd", "_ForExctnInd", "_TaxblIncmPerShr"]
	@property
	def XtndedEUDvddSts(self):
		return self._XtndedEUDvddSts

	@XtndedEUDvddSts.setter
	def XtndedEUDvddSts(self, value):
		self._XtndedEUDvddSts = value if type(value) != base_types.auto else self.make_default("XtndedEUDvddSts")

	@XtndedEUDvddSts.deleter
	def XtndedEUDvddSts(self):
		del self._XtndedEUDvddSts
		self._XtndedEUDvddSts = None

	@property
	def ValInAltrntvCcy(self):
		return self._ValInAltrntvCcy

	@ValInAltrntvCcy.setter
	def ValInAltrntvCcy(self, value):
		self._ValInAltrntvCcy = value if type(value) != base_types.auto else self.make_default("ValInAltrntvCcy")

	@ValInAltrntvCcy.deleter
	def ValInAltrntvCcy(self):
		del self._ValInAltrntvCcy
		self._ValInAltrntvCcy = None

	@property
	def XtndedTp(self):
		return self._XtndedTp

	@XtndedTp.setter
	def XtndedTp(self, value):
		self._XtndedTp = value if type(value) != base_types.auto else self.make_default("XtndedTp")

	@XtndedTp.deleter
	def XtndedTp(self):
		del self._XtndedTp
		self._XtndedTp = None

	@property
	def EUDvddSts(self):
		return self._EUDvddSts

	@EUDvddSts.setter
	def EUDvddSts(self, value):
		self._EUDvddSts = value if type(value) != base_types.auto else self.make_default("EUDvddSts")

	@EUDvddSts.deleter
	def EUDvddSts(self):
		del self._EUDvddSts
		self._EUDvddSts = None

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
	def ChrgDtls(self):
		return self._ChrgDtls

	@ChrgDtls.setter
	def ChrgDtls(self, value):
		self._ChrgDtls = value if type(value) != base_types.auto else self.make_default("ChrgDtls")

	@ChrgDtls.deleter
	def ChrgDtls(self):
		del self._ChrgDtls
		self._ChrgDtls = None

	@property
	def TaxLbltyDtls(self):
		return self._TaxLbltyDtls

	@TaxLbltyDtls.setter
	def TaxLbltyDtls(self, value):
		self._TaxLbltyDtls = value if type(value) != base_types.auto else self.make_default("TaxLbltyDtls")

	@TaxLbltyDtls.deleter
	def TaxLbltyDtls(self):
		del self._TaxLbltyDtls
		self._TaxLbltyDtls = None

	@property
	def EstmtdPricInd(self):
		return self._EstmtdPricInd

	@EstmtdPricInd.setter
	def EstmtdPricInd(self, value):
		self._EstmtdPricInd = value if type(value) != base_types.auto else self.make_default("EstmtdPricInd")

	@EstmtdPricInd.deleter
	def EstmtdPricInd(self):
		del self._EstmtdPricInd
		self._EstmtdPricInd = None

	@property
	def TaxRfndDtls(self):
		return self._TaxRfndDtls

	@TaxRfndDtls.setter
	def TaxRfndDtls(self, value):
		self._TaxRfndDtls = value if type(value) != base_types.auto else self.make_default("TaxRfndDtls")

	@TaxRfndDtls.deleter
	def TaxRfndDtls(self):
		del self._TaxRfndDtls
		self._TaxRfndDtls = None

	@property
	def ClctnBsis(self):
		return self._ClctnBsis

	@ClctnBsis.setter
	def ClctnBsis(self, value):
		self._ClctnBsis = value if type(value) != base_types.auto else self.make_default("ClctnBsis")

	@ClctnBsis.deleter
	def ClctnBsis(self):
		del self._ClctnBsis
		self._ClctnBsis = None

	@property
	def XtndedTaxblIncmPerShrClctd(self):
		return self._XtndedTaxblIncmPerShrClctd

	@XtndedTaxblIncmPerShrClctd.setter
	def XtndedTaxblIncmPerShrClctd(self, value):
		self._XtndedTaxblIncmPerShrClctd = value if type(value) != base_types.auto else self.make_default("XtndedTaxblIncmPerShrClctd")

	@XtndedTaxblIncmPerShrClctd.deleter
	def XtndedTaxblIncmPerShrClctd(self):
		del self._XtndedTaxblIncmPerShrClctd
		self._XtndedTaxblIncmPerShrClctd = None

	@property
	def PricMtd(self):
		return self._PricMtd

	@PricMtd.setter
	def PricMtd(self, value):
		self._PricMtd = value if type(value) != base_types.auto else self.make_default("PricMtd")

	@PricMtd.deleter
	def PricMtd(self):
		del self._PricMtd
		self._PricMtd = None

	@property
	def ValInInvstmtCcy(self):
		return self._ValInInvstmtCcy

	@ValInInvstmtCcy.setter
	def ValInInvstmtCcy(self, value):
		self._ValInInvstmtCcy = value if type(value) != base_types.auto else self.make_default("ValInInvstmtCcy")

	@ValInInvstmtCcy.deleter
	def ValInInvstmtCcy(self):
		del self._ValInInvstmtCcy
		self._ValInInvstmtCcy = None

	@property
	def Tp(self):
		return self._Tp

	@Tp.setter
	def Tp(self, value):
		self._Tp = value if type(value) != base_types.auto else self.make_default("Tp")

	@Tp.deleter
	def Tp(self):
		del self._Tp
		self._Tp = None

	@property
	def TaxblIncmPerDvdd(self):
		return self._TaxblIncmPerDvdd

	@TaxblIncmPerDvdd.setter
	def TaxblIncmPerDvdd(self, value):
		self._TaxblIncmPerDvdd = value if type(value) != base_types.auto else self.make_default("TaxblIncmPerDvdd")

	@TaxblIncmPerDvdd.deleter
	def TaxblIncmPerDvdd(self):
		del self._TaxblIncmPerDvdd
		self._TaxblIncmPerDvdd = None

	@property
	def NbOfDaysAcrd(self):
		return self._NbOfDaysAcrd

	@NbOfDaysAcrd.setter
	def NbOfDaysAcrd(self, value):
		self._NbOfDaysAcrd = value if type(value) != base_types.auto else self.make_default("NbOfDaysAcrd")

	@NbOfDaysAcrd.deleter
	def NbOfDaysAcrd(self):
		del self._NbOfDaysAcrd
		self._NbOfDaysAcrd = None

	@property
	def TaxblIncmPerShrClctd(self):
		return self._TaxblIncmPerShrClctd

	@TaxblIncmPerShrClctd.setter
	def TaxblIncmPerShrClctd(self, value):
		self._TaxblIncmPerShrClctd = value if type(value) != base_types.auto else self.make_default("TaxblIncmPerShrClctd")

	@TaxblIncmPerShrClctd.deleter
	def TaxblIncmPerShrClctd(self):
		del self._TaxblIncmPerShrClctd
		self._TaxblIncmPerShrClctd = None

	@property
	def ForExctnInd(self):
		return self._ForExctnInd

	@ForExctnInd.setter
	def ForExctnInd(self, value):
		self._ForExctnInd = value if type(value) != base_types.auto else self.make_default("ForExctnInd")

	@ForExctnInd.deleter
	def ForExctnInd(self):
		del self._ForExctnInd
		self._ForExctnInd = None

	@property
	def TaxblIncmPerShr(self):
		return self._TaxblIncmPerShr

	@TaxblIncmPerShr.setter
	def TaxblIncmPerShr(self, value):
		self._TaxblIncmPerShr = value if type(value) != base_types.auto else self.make_default("TaxblIncmPerShr")

	@TaxblIncmPerShr.deleter
	def TaxblIncmPerShr(self):
		del self._TaxblIncmPerShr
		self._TaxblIncmPerShr = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='XtndedEUDvddSts', type=Extended350Code, min=0, max=1, mutex_group=3, array=False),
		base_types.FieldEntry(name='ValInAltrntvCcy', type=PriceValue1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='XtndedTp', type=Extended350Code, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='EUDvddSts', type=EUDividendStatus1Code, min=0, max=1, mutex_group=3, array=False),
		base_types.FieldEntry(name='CumDvddInd', type=YesNoIndicator, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ChrgDtls', type=Charge15, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='TaxLbltyDtls', type=Tax17, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='EstmtdPricInd', type=YesNoIndicator, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TaxRfndDtls', type=Tax17, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='ClctnBsis', type=PercentageRate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='XtndedTaxblIncmPerShrClctd', type=Extended350Code, min=0, max=1, mutex_group=2, array=False),
		base_types.FieldEntry(name='PricMtd', type=PriceMethod1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ValInInvstmtCcy', type=PriceValue1, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Tp', type=TypeOfPrice9Code, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='TaxblIncmPerDvdd', type=ActiveOrHistoricCurrencyAnd13DecimalAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NbOfDaysAcrd', type=Number, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TaxblIncmPerShrClctd', type=TaxableIncomePerShareCalculated2Code, min=0, max=1, mutex_group=2, array=False),
		base_types.FieldEntry(name='ForExctnInd', type=YesNoIndicator, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TaxblIncmPerShr', type=ActiveOrHistoricCurrencyAnd13DecimalAmount, min=0, max=1, mutex_group=None, array=False),
	))

