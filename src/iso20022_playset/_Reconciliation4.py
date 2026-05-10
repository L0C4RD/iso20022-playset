from . import base_types
from ._Max35Text import Max35Text
from ._ISODate import ISODate

class Reconciliation4(base_types._BaseFieldType):

	__slots__ = ["_Id", "_ChckptRef", "_Dt"]
	@property
	def Id(self):
		return self._Id

	@Id.setter
	def Id(self, value):
		self._Id = value if type(value) != base_types.auto else self.make_default("Id")

	@Id.deleter
	def Id(self):
		del self._Id
		self._Id = None

	@property
	def ChckptRef(self):
		return self._ChckptRef

	@ChckptRef.setter
	def ChckptRef(self, value):
		self._ChckptRef = value if type(value) != base_types.auto else self.make_default("ChckptRef")

	@ChckptRef.deleter
	def ChckptRef(self):
		del self._ChckptRef
		self._ChckptRef = None

	@property
	def Dt(self):
		return self._Dt

	@Dt.setter
	def Dt(self, value):
		self._Dt = value if type(value) != base_types.auto else self.make_default("Dt")

	@Dt.deleter
	def Dt(self):
		del self._Dt
		self._Dt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Id', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ChckptRef', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Dt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
	))

