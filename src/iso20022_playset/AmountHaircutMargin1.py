import base_types
import PercentageRate
import AmountAndDirection53

class AmountHaircutMargin1(base_types._BaseFieldType):

	__slots__ = ["_Amt", "_HrcutOrMrgn"]
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
	def HrcutOrMrgn(self):
		return self._HrcutOrMrgn

	@HrcutOrMrgn.setter
	def HrcutOrMrgn(self, value):
		self._HrcutOrMrgn = value if type(value) != auto else self.make_default("HrcutOrMrgn")

	@HrcutOrMrgn.deleter
	def HrcutOrMrgn(self):
		del self._HrcutOrMrgn
		self._HrcutOrMrgn = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Amt', type=AmountAndDirection53, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='HrcutOrMrgn', type=PercentageRate, min=0, max=1, mutex_group=None, array=False),
	))

