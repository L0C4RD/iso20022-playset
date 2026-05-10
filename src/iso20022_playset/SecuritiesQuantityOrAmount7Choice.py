from . import base_types
import RestrictedFINActiveCurrencyAndAmount
import SecuritiesOption88

class SecuritiesQuantityOrAmount7Choice(base_types._BaseFieldType):

	__slots__ = ["_SctiesQty", "_InstdAmt"]
	@property
	def SctiesQty(self):
		return self._SctiesQty

	@SctiesQty.setter
	def SctiesQty(self, value):
		self._SctiesQty = value if type(value) != auto else self.make_default("SctiesQty")

	@SctiesQty.deleter
	def SctiesQty(self):
		del self._SctiesQty
		self._SctiesQty = None

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

	_field_defs = frozenset((
		base_types.FieldEntry(name='SctiesQty', type=SecuritiesOption88, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='InstdAmt', type=RestrictedFINActiveCurrencyAndAmount, min=0, max=1, mutex_group=1, array=False),
	))

