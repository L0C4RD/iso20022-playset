from . import base_types
from .Price7 import Price7
from .ProprietaryPrice2 import ProprietaryPrice2

class TransactionPrice4Choice(base_types._BaseFieldType):

	__slots__ = ["_Prtry", "_DealPric"]
	@property
	def Prtry(self):
		return self._Prtry

	@Prtry.setter
	def Prtry(self, value):
		self._Prtry = value if type(value) != base_types.auto else self.make_default("Prtry")

	@Prtry.deleter
	def Prtry(self):
		del self._Prtry
		self._Prtry = None

	@property
	def DealPric(self):
		return self._DealPric

	@DealPric.setter
	def DealPric(self, value):
		self._DealPric = value if type(value) != base_types.auto else self.make_default("DealPric")

	@DealPric.deleter
	def DealPric(self):
		del self._DealPric
		self._DealPric = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Prtry', type=ProprietaryPrice2, min=1, max=None, mutex_group=1, array=True),
		base_types.FieldEntry(name='DealPric', type=Price7, min=0, max=1, mutex_group=1, array=False),
	))

