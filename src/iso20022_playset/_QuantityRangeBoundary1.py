from . import base_types
from ._DecimalNumber import DecimalNumber
from ._YesNoIndicator import YesNoIndicator

class QuantityRangeBoundary1(base_types._BaseFieldType):

	__slots__ = ["_Bdry", "_Incl"]
	@property
	def Bdry(self):
		return self._Bdry

	@Bdry.setter
	def Bdry(self, value):
		self._Bdry = value if type(value) != base_types.auto else self.make_default("Bdry")

	@Bdry.deleter
	def Bdry(self):
		del self._Bdry
		self._Bdry = None

	@property
	def Incl(self):
		return self._Incl

	@Incl.setter
	def Incl(self, value):
		self._Incl = value if type(value) != base_types.auto else self.make_default("Incl")

	@Incl.deleter
	def Incl(self):
		del self._Incl
		self._Incl = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Bdry', type=DecimalNumber, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Incl', type=YesNoIndicator, min=1, max=1, mutex_group=None, array=False),
	))

