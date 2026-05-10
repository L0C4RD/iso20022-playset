from . import base_types
import BalanceQuantity14Choice

class OpeningBalance6Choice(base_types._BaseFieldType):

	__slots__ = ["_Intrmy", "_Frst"]
	@property
	def Intrmy(self):
		return self._Intrmy

	@Intrmy.setter
	def Intrmy(self, value):
		self._Intrmy = value if type(value) != auto else self.make_default("Intrmy")

	@Intrmy.deleter
	def Intrmy(self):
		del self._Intrmy
		self._Intrmy = None

	@property
	def Frst(self):
		return self._Frst

	@Frst.setter
	def Frst(self, value):
		self._Frst = value if type(value) != auto else self.make_default("Frst")

	@Frst.deleter
	def Frst(self):
		del self._Frst
		self._Frst = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Intrmy', type=BalanceQuantity14Choice, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Frst', type=BalanceQuantity14Choice, min=0, max=1, mutex_group=1, array=False),
	))

