from . import base_types
from ._Operation1Code import Operation1Code
from ._Term1 import Term1

class AmountOrPercentageRange1(base_types._BaseFieldType):

	__slots__ = ["_Opr", "_Term"]
	@property
	def Opr(self):
		return self._Opr

	@Opr.setter
	def Opr(self, value):
		self._Opr = value if type(value) != base_types.auto else self.make_default("Opr")

	@Opr.deleter
	def Opr(self):
		del self._Opr
		self._Opr = None

	@property
	def Term(self):
		return self._Term

	@Term.setter
	def Term(self, value):
		self._Term = value if type(value) != base_types.auto else self.make_default("Term")

	@Term.deleter
	def Term(self):
		del self._Term
		self._Term = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Opr', type=Operation1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Term', type=Term1, min=0, max=10, mutex_group=None, array=True),
	))

