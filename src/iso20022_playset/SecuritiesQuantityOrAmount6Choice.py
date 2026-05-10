from . import base_types
from .SecuritiesOption79 import SecuritiesOption79
from .ActiveCurrencyAndAmount import ActiveCurrencyAndAmount

class SecuritiesQuantityOrAmount6Choice(base_types._BaseFieldType):

	__slots__ = ["_InstdAmt", "_SctiesQty"]
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
	def SctiesQty(self):
		return self._SctiesQty

	@SctiesQty.setter
	def SctiesQty(self, value):
		self._SctiesQty = value if type(value) != auto else self.make_default("SctiesQty")

	@SctiesQty.deleter
	def SctiesQty(self):
		del self._SctiesQty
		self._SctiesQty = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='InstdAmt', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='SctiesQty', type=SecuritiesOption79, min=0, max=1, mutex_group=1, array=False),
	))

