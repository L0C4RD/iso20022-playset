from . import base_types
import ATMService25
import Max35Text

class ATMContext26(base_types._BaseFieldType):

	__slots__ = ["_SsnRef", "_Svc"]
	@property
	def SsnRef(self):
		return self._SsnRef

	@SsnRef.setter
	def SsnRef(self, value):
		self._SsnRef = value if type(value) != auto else self.make_default("SsnRef")

	@SsnRef.deleter
	def SsnRef(self):
		del self._SsnRef
		self._SsnRef = None

	@property
	def Svc(self):
		return self._Svc

	@Svc.setter
	def Svc(self, value):
		self._Svc = value if type(value) != auto else self.make_default("Svc")

	@Svc.deleter
	def Svc(self):
		del self._Svc
		self._Svc = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='SsnRef', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Svc', type=ATMService25, min=1, max=1, mutex_group=None, array=False),
	))

