from . import base_types
from ._Max30Text import Max30Text
from ._Max30DecimalNumber import Max30DecimalNumber
from ._DTI2021Identifier import DTI2021Identifier

class DigitalTokenAmount2(base_types._BaseFieldType):

	__slots__ = ["_Desc", "_Idr", "_Unit"]
	@property
	def Desc(self):
		return self._Desc

	@Desc.setter
	def Desc(self, value):
		self._Desc = value if type(value) != base_types.auto else self.make_default("Desc")

	@Desc.deleter
	def Desc(self):
		del self._Desc
		self._Desc = None

	@property
	def Idr(self):
		return self._Idr

	@Idr.setter
	def Idr(self, value):
		self._Idr = value if type(value) != base_types.auto else self.make_default("Idr")

	@Idr.deleter
	def Idr(self):
		del self._Idr
		self._Idr = None

	@property
	def Unit(self):
		return self._Unit

	@Unit.setter
	def Unit(self, value):
		self._Unit = value if type(value) != base_types.auto else self.make_default("Unit")

	@Unit.deleter
	def Unit(self):
		del self._Unit
		self._Unit = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Desc', type=Max30Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Idr', type=DTI2021Identifier, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Unit', type=Max30DecimalNumber, min=0, max=1, mutex_group=None, array=False),
	))

