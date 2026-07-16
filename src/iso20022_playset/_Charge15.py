# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActiveCurrencyAnd13DecimalAmount
from . import CalculationBasis2Code
from . import ChargeType9Code
from . import Extended350Code
from . import PercentageRate

class Charge15(base_types._BaseFieldType):

	__slots__ = ["_Amt", "_ClctnBsis", "_Rate", "_Tp", "_XtndedClctnBsis", "_XtndedTp"]
	@property
	def Amt(self):
		return self._Amt

	@Amt.setter
	def Amt(self, value):
		self._Amt = value if value is not None else base_types.UninitialisedField(self, 'Amt', ActiveCurrencyAnd13DecimalAmount, False)

	@Amt.deleter
	def Amt(self):
		del self._Amt
		self._Amt = base_types.UninitialisedField(self, 'Amt', ActiveCurrencyAnd13DecimalAmount, False)

	@property
	def ClctnBsis(self):
		return self._ClctnBsis

	@ClctnBsis.setter
	def ClctnBsis(self, value):
		self._ClctnBsis = value if value is not None else base_types.UninitialisedField(self, 'ClctnBsis', CalculationBasis2Code, False)

	@ClctnBsis.deleter
	def ClctnBsis(self):
		del self._ClctnBsis
		self._ClctnBsis = base_types.UninitialisedField(self, 'ClctnBsis', CalculationBasis2Code, False)

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
	def Tp(self):
		return self._Tp

	@Tp.setter
	def Tp(self, value):
		self._Tp = value if value is not None else base_types.UninitialisedField(self, 'Tp', ChargeType9Code, False)

	@Tp.deleter
	def Tp(self):
		del self._Tp
		self._Tp = base_types.UninitialisedField(self, 'Tp', ChargeType9Code, False)

	@property
	def XtndedClctnBsis(self):
		return self._XtndedClctnBsis

	@XtndedClctnBsis.setter
	def XtndedClctnBsis(self, value):
		self._XtndedClctnBsis = value if value is not None else base_types.UninitialisedField(self, 'XtndedClctnBsis', Extended350Code, False)

	@XtndedClctnBsis.deleter
	def XtndedClctnBsis(self):
		del self._XtndedClctnBsis
		self._XtndedClctnBsis = base_types.UninitialisedField(self, 'XtndedClctnBsis', Extended350Code, False)

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
		base_types.FieldEntry(name='Amt', type=ActiveCurrencyAnd13DecimalAmount, min=0, max=1, mutex_group=2, array=False),
		base_types.FieldEntry(name='ClctnBsis', type=CalculationBasis2Code, min=0, max=1, mutex_group=3, array=False),
		base_types.FieldEntry(name='Rate', type=PercentageRate, min=0, max=1, mutex_group=2, array=False),
		base_types.FieldEntry(name='Tp', type=ChargeType9Code, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='XtndedClctnBsis', type=Extended350Code, min=0, max=1, mutex_group=3, array=False),
		base_types.FieldEntry(name='XtndedTp', type=Extended350Code, min=0, max=1, mutex_group=1, array=False),
	))