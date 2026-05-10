import base_types
import EquivalentAmount2
import ActiveOrHistoricCurrencyAndAmount

class AmountType3Choice(base_types._BaseFieldType):

	__slots__ = ["_InstdAmt", "_EqvtAmt"]
	@property
	def InstdAmt(self):
		return self._InstdAmt

	@InstdAmt.setter
	def InstdAmt(self, value):
		self._InstdAmt = value if type(value) != auto else self.make_default("InstdAmt")

	@InstdAmt.deleter
	def InstdAmt(self):
		del self._InstdAmt
		self._InstdAmt = None

	@property
	def EqvtAmt(self):
		return self._EqvtAmt

	@EqvtAmt.setter
	def EqvtAmt(self, value):
		self._EqvtAmt = value if type(value) != auto else self.make_default("EqvtAmt")

	@EqvtAmt.deleter
	def EqvtAmt(self):
		del self._EqvtAmt
		self._EqvtAmt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='InstdAmt', type=ActiveOrHistoricCurrencyAndAmount, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='EqvtAmt', type=EquivalentAmount2, min=0, max=1, mutex_group=1, array=False),
	))

