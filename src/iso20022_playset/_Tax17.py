# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActiveOrHistoricCurrencyAnd13DecimalAmount
from . import CountryCode
from . import Extended350Code
from . import PercentageRate
from . import TaxCalculationInformation4
from . import TaxType12Code

class Tax17(base_types._BaseFieldType):

	__slots__ = ["_Amt", "_Ctry", "_Rate", "_TaxClctnDtls", "_Tp", "_XtndedTp"]
	@property
	def Amt(self):
		return self._Amt

	@Amt.setter
	def Amt(self, value):
		self._Amt = value if value is not None else base_types.UninitialisedField(self, 'Amt', ActiveOrHistoricCurrencyAnd13DecimalAmount, True)

	@Amt.deleter
	def Amt(self):
		del self._Amt
		self._Amt = base_types.UninitialisedField(self, 'Amt', ActiveOrHistoricCurrencyAnd13DecimalAmount, True)

	@property
	def Ctry(self):
		return self._Ctry

	@Ctry.setter
	def Ctry(self, value):
		self._Ctry = value if value is not None else base_types.UninitialisedField(self, 'Ctry', CountryCode, False)

	@Ctry.deleter
	def Ctry(self):
		del self._Ctry
		self._Ctry = base_types.UninitialisedField(self, 'Ctry', CountryCode, False)

	@property
	def Rate(self):
		return self._Rate

	@Rate.setter
	def Rate(self, value):
		self._Rate = value if value is not None else base_types.UninitialisedField(self, 'Rate', PercentageRate, False)

	@Rate.deleter
	def Rate(self):
		del self._Rate
		self._Rate = base_types.UninitialisedField(self, 'Rate', PercentageRate, False)

	@property
	def TaxClctnDtls(self):
		return self._TaxClctnDtls

	@TaxClctnDtls.setter
	def TaxClctnDtls(self, value):
		self._TaxClctnDtls = value if value is not None else base_types.UninitialisedField(self, 'TaxClctnDtls', TaxCalculationInformation4, False)

	@TaxClctnDtls.deleter
	def TaxClctnDtls(self):
		del self._TaxClctnDtls
		self._TaxClctnDtls = base_types.UninitialisedField(self, 'TaxClctnDtls', TaxCalculationInformation4, False)

	@property
	def Tp(self):
		return self._Tp

	@Tp.setter
	def Tp(self, value):
		self._Tp = value if value is not None else base_types.UninitialisedField(self, 'Tp', TaxType12Code, False)

	@Tp.deleter
	def Tp(self):
		del self._Tp
		self._Tp = base_types.UninitialisedField(self, 'Tp', TaxType12Code, False)

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
		base_types.FieldEntry(name='Amt', type=ActiveOrHistoricCurrencyAnd13DecimalAmount, min=0, max=7, mutex_group=None, array=True),
		base_types.FieldEntry(name='Ctry', type=CountryCode, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Rate', type=PercentageRate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TaxClctnDtls', type=TaxCalculationInformation4, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tp', type=TaxType12Code, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='XtndedTp', type=Extended350Code, min=0, max=1, mutex_group=1, array=False),
	))