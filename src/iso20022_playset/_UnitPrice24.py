from . import base_types
from ._ActiveOrHistoricCurrencyAnd13DecimalAmount import ActiveOrHistoricCurrencyAnd13DecimalAmount
from ._Charge33 import Charge33
from ._EUDividendStatusType3Choice import EUDividendStatusType3Choice
from ._Number import Number
from ._PercentageRate import PercentageRate
from ._PriceMethod1Code import PriceMethod1Code
from ._PriceType6Choice import PriceType6Choice
from ._PriceValue1 import PriceValue1
from ._Tax43 import Tax43
from ._TaxableIncomePerShareCalculated3Choice import TaxableIncomePerShareCalculated3Choice
from ._YesNoIndicator import YesNoIndicator

class UnitPrice24(base_types._BaseFieldType):

	__slots__ = ["_ChrgDtls", "_ClctnBsis", "_CumDvddInd", "_EUDvddSts", "_EstmtdPricInd", "_ForExctnInd", "_NbOfDaysAcrd", "_PricMtd", "_PricTp", "_TaxLbltyDtls", "_TaxRfndDtls", "_TaxblIncmPerDvdd", "_TaxblIncmPerShr", "_TaxblIncmPerShrClctd", "_ValInAltrntvCcy", "_ValInInvstmtCcy"]
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
	def PricTp(self):
		return self._PricTp

	@PricTp.setter
	def PricTp(self, value):
		self._PricTp = value if type(value) != base_types.auto else self.make_default("PricTp")

	@PricTp.deleter
	def PricTp(self):
		del self._PricTp
		self._PricTp = None

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
	def TaxblIncmPerShr(self):
		return self._TaxblIncmPerShr

	@TaxblIncmPerShr.setter
	def TaxblIncmPerShr(self, value):
		self._TaxblIncmPerShr = value if type(value) != base_types.auto else self.make_default("TaxblIncmPerShr")

	@TaxblIncmPerShr.deleter
	def TaxblIncmPerShr(self):
		del self._TaxblIncmPerShr
		self._TaxblIncmPerShr = None

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
	def ValInInvstmtCcy(self):
		return self._ValInInvstmtCcy

	@ValInInvstmtCcy.setter
	def ValInInvstmtCcy(self, value):
		self._ValInInvstmtCcy = value if type(value) != base_types.auto else self.make_default("ValInInvstmtCcy")

	@ValInInvstmtCcy.deleter
	def ValInInvstmtCcy(self):
		del self._ValInInvstmtCcy
		self._ValInInvstmtCcy = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='ChrgDtls', type=Charge33, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='ClctnBsis', type=PercentageRate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CumDvddInd', type=YesNoIndicator, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='EUDvddSts', type=EUDividendStatusType3Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='EstmtdPricInd', type=YesNoIndicator, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ForExctnInd', type=YesNoIndicator, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NbOfDaysAcrd', type=Number, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PricMtd', type=PriceMethod1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PricTp', type=PriceType6Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TaxLbltyDtls', type=Tax43, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='TaxRfndDtls', type=Tax43, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='TaxblIncmPerDvdd', type=ActiveOrHistoricCurrencyAnd13DecimalAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TaxblIncmPerShr', type=ActiveOrHistoricCurrencyAnd13DecimalAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TaxblIncmPerShrClctd', type=TaxableIncomePerShareCalculated3Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ValInAltrntvCcy', type=PriceValue1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='ValInInvstmtCcy', type=PriceValue1, min=1, max=None, mutex_group=None, array=True),
	))

