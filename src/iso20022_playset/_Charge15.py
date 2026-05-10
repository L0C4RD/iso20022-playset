from . import base_types
from ._PercentageRate import PercentageRate
from ._ActiveCurrencyAnd13DecimalAmount import ActiveCurrencyAnd13DecimalAmount
from ._ChargeType9Code import ChargeType9Code
from ._CalculationBasis2Code import CalculationBasis2Code
from ._Extended350Code import Extended350Code

class Charge15(base_types._BaseFieldType):

	__slots__ = ["_Amt", "_ClctnBsis", "_Rate", "_XtndedTp", "_Tp", "_XtndedClctnBsis"]
	@property
	def Amt(self):
		return self._Amt

	@Amt.setter
	def Amt(self, value):
		self._Amt = value if type(value) != base_types.auto else self.make_default("Amt")

	@Amt.deleter
	def Amt(self):
		del self._Amt
		self._Amt = None

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
	def Rate(self):
		return self._Rate

	@Rate.setter
	def Rate(self, value):
		self._Rate = value if type(value) != base_types.auto else self.make_default("Rate")

	@Rate.deleter
	def Rate(self):
		del self._Rate
		self._Rate = None

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
	def XtndedClctnBsis(self):
		return self._XtndedClctnBsis

	@XtndedClctnBsis.setter
	def XtndedClctnBsis(self, value):
		self._XtndedClctnBsis = value if type(value) != base_types.auto else self.make_default("XtndedClctnBsis")

	@XtndedClctnBsis.deleter
	def XtndedClctnBsis(self):
		del self._XtndedClctnBsis
		self._XtndedClctnBsis = None

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

	_field_defs = frozenset((
		base_types.FieldEntry(name='Amt', type=ActiveCurrencyAnd13DecimalAmount, min=0, max=1, mutex_group=2, array=False),
		base_types.FieldEntry(name='ClctnBsis', type=CalculationBasis2Code, min=0, max=1, mutex_group=3, array=False),
		base_types.FieldEntry(name='Rate', type=PercentageRate, min=0, max=1, mutex_group=2, array=False),
		base_types.FieldEntry(name='Tp', type=ChargeType9Code, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='XtndedClctnBsis', type=Extended350Code, min=0, max=1, mutex_group=3, array=False),
		base_types.FieldEntry(name='XtndedTp', type=Extended350Code, min=0, max=1, mutex_group=1, array=False),
	))

