from . import base_types
from ._ContactIdentification1 import ContactIdentification1

class BankContactPerson1Choice(base_types._BaseFieldType):

	__slots__ = ["_SellrBkCtctPrsn", "_BuyrBkCtctPrsn"]
	@property
	def BuyrBkCtctPrsn(self):
		return self._BuyrBkCtctPrsn

	@BuyrBkCtctPrsn.setter
	def BuyrBkCtctPrsn(self, value):
		self._BuyrBkCtctPrsn = value if type(value) != base_types.auto else self.make_default("BuyrBkCtctPrsn")

	@BuyrBkCtctPrsn.deleter
	def BuyrBkCtctPrsn(self):
		del self._BuyrBkCtctPrsn
		self._BuyrBkCtctPrsn = None

	@property
	def SellrBkCtctPrsn(self):
		return self._SellrBkCtctPrsn

	@SellrBkCtctPrsn.setter
	def SellrBkCtctPrsn(self, value):
		self._SellrBkCtctPrsn = value if type(value) != base_types.auto else self.make_default("SellrBkCtctPrsn")

	@SellrBkCtctPrsn.deleter
	def SellrBkCtctPrsn(self):
		del self._SellrBkCtctPrsn
		self._SellrBkCtctPrsn = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='BuyrBkCtctPrsn', type=ContactIdentification1, min=1, max=None, mutex_group=1, array=True),
		base_types.FieldEntry(name='SellrBkCtctPrsn', type=ContactIdentification1, min=1, max=None, mutex_group=1, array=True),
	))

