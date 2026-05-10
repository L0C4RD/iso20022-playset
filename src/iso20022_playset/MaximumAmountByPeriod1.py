import base_types
import Max3NumericText
import ActiveCurrencyAndAmount

class MaximumAmountByPeriod1(base_types._BaseFieldType):

	__slots__ = ["_MaxAmt", "_NbOfDays"]
	@property
	def MaxAmt(self):
		return self._MaxAmt

	@MaxAmt.setter
	def MaxAmt(self, value):
		self._MaxAmt = value if type(value) != auto else self.make_default("MaxAmt")

	@MaxAmt.deleter
	def MaxAmt(self):
		del self._MaxAmt
		self._MaxAmt = None

	@property
	def NbOfDays(self):
		return self._NbOfDays

	@NbOfDays.setter
	def NbOfDays(self, value):
		self._NbOfDays = value if type(value) != auto else self.make_default("NbOfDays")

	@NbOfDays.deleter
	def NbOfDays(self):
		del self._NbOfDays
		self._NbOfDays = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='MaxAmt', type=ActiveCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NbOfDays', type=Max3NumericText, min=1, max=1, mutex_group=None, array=False),
	))

