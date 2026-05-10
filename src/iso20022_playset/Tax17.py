import base_types
import TaxType12Code
import Extended350Code
import TaxCalculationInformation4
import PercentageRate
import CountryCode
import ActiveOrHistoricCurrencyAnd13DecimalAmount

class Tax17(base_types._BaseFieldType):

	__slots__ = ["_Ctry", "_TaxClctnDtls", "_XtndedTp", "_Tp", "_Amt", "_Rate"]
	@property
	def Ctry(self):
		return self._Ctry

	@Ctry.setter
	def Ctry(self, value):
		self._Ctry = value if type(value) != auto else self.make_default("Ctry")

	@Ctry.deleter
	def Ctry(self):
		del self._Ctry
		self._Ctry = None

	@property
	def TaxClctnDtls(self):
		return self._TaxClctnDtls

	@TaxClctnDtls.setter
	def TaxClctnDtls(self, value):
		self._TaxClctnDtls = value if type(value) != auto else self.make_default("TaxClctnDtls")

	@TaxClctnDtls.deleter
	def TaxClctnDtls(self):
		del self._TaxClctnDtls
		self._TaxClctnDtls = None

	@property
	def XtndedTp(self):
		return self._XtndedTp

	@XtndedTp.setter
	def XtndedTp(self, value):
		self._XtndedTp = value if type(value) != auto else self.make_default("XtndedTp")

	@XtndedTp.deleter
	def XtndedTp(self):
		del self._XtndedTp
		self._XtndedTp = None

	@property
	def Tp(self):
		return self._Tp

	@Tp.setter
	def Tp(self, value):
		self._Tp = value if type(value) != auto else self.make_default("Tp")

	@Tp.deleter
	def Tp(self):
		del self._Tp
		self._Tp = None

	@property
	def Amt(self):
		return self._Amt

	@Amt.setter
	def Amt(self, value):
		self._Amt = value if type(value) != auto else self.make_default("Amt")

	@Amt.deleter
	def Amt(self):
		del self._Amt
		self._Amt = None

	@property
	def Rate(self):
		return self._Rate

	@Rate.setter
	def Rate(self, value):
		self._Rate = value if type(value) != auto else self.make_default("Rate")

	@Rate.deleter
	def Rate(self):
		del self._Rate
		self._Rate = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Ctry', type=CountryCode, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TaxClctnDtls', type=TaxCalculationInformation4, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='XtndedTp', type=Extended350Code, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Tp', type=TaxType12Code, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Amt', type=ActiveOrHistoricCurrencyAnd13DecimalAmount, min=0, max=7, mutex_group=None, array=True),
		base_types.FieldEntry(name='Rate', type=PercentageRate, min=0, max=1, mutex_group=None, array=False),
	))

