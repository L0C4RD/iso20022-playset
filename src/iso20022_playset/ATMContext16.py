from . import base_types
from .ATMService20 import ATMService20
from .Max35Text import Max35Text

class ATMContext16(base_types._BaseFieldType):

	__slots__ = ["_Svc", "_SsnRef"]
	@property
	def Svc(self):
		return self._Svc

	@Svc.setter
	def Svc(self, value):
		self._Svc = value if type(value) != base_types.auto else self.make_default("Svc")

	@Svc.deleter
	def Svc(self):
		del self._Svc
		self._Svc = None

	@property
	def SsnRef(self):
		return self._SsnRef

	@SsnRef.setter
	def SsnRef(self, value):
		self._SsnRef = value if type(value) != base_types.auto else self.make_default("SsnRef")

	@SsnRef.deleter
	def SsnRef(self):
		del self._SsnRef
		self._SsnRef = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Svc', type=ATMService20, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SsnRef', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
	))

