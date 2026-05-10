import base_types
import CancelOrderReport1
import NewOrderReport2

class OrderReport2Choice(base_types._BaseFieldType):

	__slots__ = ["_Cxl", "_New"]
	@property
	def Cxl(self):
		return self._Cxl

	@Cxl.setter
	def Cxl(self, value):
		self._Cxl = value if type(value) != auto else self.make_default("Cxl")

	@Cxl.deleter
	def Cxl(self):
		del self._Cxl
		self._Cxl = None

	@property
	def New(self):
		return self._New

	@New.setter
	def New(self, value):
		self._New = value if type(value) != auto else self.make_default("New")

	@New.deleter
	def New(self):
		del self._New
		self._New = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Cxl', type=CancelOrderReport1, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='New', type=NewOrderReport2, min=0, max=1, mutex_group=1, array=False),
	))

