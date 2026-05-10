from . import base_types
from .NotReported1Code import NotReported1Code
from .Max52Text import Max52Text

class UPIQueryCriteria1(base_types._BaseFieldType):

	__slots__ = ["_NotRptd", "_Idr"]
	@property
	def NotRptd(self):
		return self._NotRptd

	@NotRptd.setter
	def NotRptd(self, value):
		self._NotRptd = value if type(value) != base_types.auto else self.make_default("NotRptd")

	@NotRptd.deleter
	def NotRptd(self):
		del self._NotRptd
		self._NotRptd = None

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

	_field_defs = frozenset((
		base_types.FieldEntry(name='NotRptd', type=NotReported1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Idr', type=Max52Text, min=0, max=None, mutex_group=None, array=True),
	))

