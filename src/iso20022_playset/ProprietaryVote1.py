from . import base_types
from .GenericIdentification30 import GenericIdentification30
from .QuantityOrCode1Choice import QuantityOrCode1Choice

class ProprietaryVote1(base_types._BaseFieldType):

	__slots__ = ["_Cd", "_Qty"]
	@property
	def Cd(self):
		return self._Cd

	@Cd.setter
	def Cd(self, value):
		self._Cd = value if type(value) != auto else self.make_default("Cd")

	@Cd.deleter
	def Cd(self):
		del self._Cd
		self._Cd = None

	@property
	def Qty(self):
		return self._Qty

	@Qty.setter
	def Qty(self, value):
		self._Qty = value if type(value) != auto else self.make_default("Qty")

	@Qty.deleter
	def Qty(self):
		del self._Qty
		self._Qty = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Cd', type=GenericIdentification30, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Qty', type=QuantityOrCode1Choice, min=1, max=1, mutex_group=None, array=False),
	))

