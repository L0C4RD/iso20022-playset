import base_types
import AmountRangeBoundary1

class FromToAmountRange1(base_types._BaseFieldType):

	__slots__ = ["_FrAmt", "_ToAmt"]
	@property
	def FrAmt(self):
		return self._FrAmt

	@FrAmt.setter
	def FrAmt(self, value):
		self._FrAmt = value if type(value) != auto else self.make_default("FrAmt")

	@FrAmt.deleter
	def FrAmt(self):
		del self._FrAmt
		self._FrAmt = None

	@property
	def ToAmt(self):
		return self._ToAmt

	@ToAmt.setter
	def ToAmt(self, value):
		self._ToAmt = value if type(value) != auto else self.make_default("ToAmt")

	@ToAmt.deleter
	def ToAmt(self):
		del self._ToAmt
		self._ToAmt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='FrAmt', type=AmountRangeBoundary1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ToAmt', type=AmountRangeBoundary1, min=1, max=1, mutex_group=None, array=False),
	))

