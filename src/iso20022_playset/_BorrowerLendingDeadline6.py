from . import base_types
from ._PartyIdentification136Choice import PartyIdentification136Choice
from ._DateFormat49Choice import DateFormat49Choice

class BorrowerLendingDeadline6(base_types._BaseFieldType):

	__slots__ = ["_StockLndgDdln", "_Brrwr"]
	@property
	def Brrwr(self):
		return self._Brrwr

	@Brrwr.setter
	def Brrwr(self, value):
		self._Brrwr = value if type(value) != base_types.auto else self.make_default("Brrwr")

	@Brrwr.deleter
	def Brrwr(self):
		del self._Brrwr
		self._Brrwr = None

	@property
	def StockLndgDdln(self):
		return self._StockLndgDdln

	@StockLndgDdln.setter
	def StockLndgDdln(self, value):
		self._StockLndgDdln = value if type(value) != base_types.auto else self.make_default("StockLndgDdln")

	@StockLndgDdln.deleter
	def StockLndgDdln(self):
		del self._StockLndgDdln
		self._StockLndgDdln = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Brrwr', type=PartyIdentification136Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StockLndgDdln', type=DateFormat49Choice, min=1, max=1, mutex_group=None, array=False),
	))

