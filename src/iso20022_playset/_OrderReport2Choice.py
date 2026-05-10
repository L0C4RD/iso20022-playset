from . import base_types
from .NewOrderReport2 import NewOrderReport2
from .CancelOrderReport1 import CancelOrderReport1

class OrderReport2Choice(base_types._BaseFieldType):

	__slots__ = ["_New", "_Cxl"]
	@property
	def New(self):
		return self._New

	@New.setter
	def New(self, value):
		self._New = value if type(value) != base_types.auto else self.make_default("New")

	@New.deleter
	def New(self):
		del self._New
		self._New = None

	@property
	def Cxl(self):
		return self._Cxl

	@Cxl.setter
	def Cxl(self, value):
		self._Cxl = value if type(value) != base_types.auto else self.make_default("Cxl")

	@Cxl.deleter
	def Cxl(self):
		del self._Cxl
		self._Cxl = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='New', type=NewOrderReport2, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Cxl', type=CancelOrderReport1, min=0, max=1, mutex_group=1, array=False),
	))

