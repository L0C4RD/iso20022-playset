from . import base_types
from ._LoanContract4 import LoanContract4
from ._TradeContract4 import TradeContract4

class UnderlyingContract4Choice(base_types._BaseFieldType):

	__slots__ = ["_Trad", "_Ln"]
	@property
	def Ln(self):
		return self._Ln

	@Ln.setter
	def Ln(self, value):
		self._Ln = value if type(value) != base_types.auto else self.make_default("Ln")

	@Ln.deleter
	def Ln(self):
		del self._Ln
		self._Ln = None

	@property
	def Trad(self):
		return self._Trad

	@Trad.setter
	def Trad(self, value):
		self._Trad = value if type(value) != base_types.auto else self.make_default("Trad")

	@Trad.deleter
	def Trad(self):
		del self._Trad
		self._Trad = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Ln', type=LoanContract4, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Trad', type=TradeContract4, min=0, max=1, mutex_group=1, array=False),
	))

