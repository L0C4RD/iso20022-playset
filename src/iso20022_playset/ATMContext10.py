from . import base_types
import Max35Text
import ATMService11

class ATMContext10(base_types._BaseFieldType):

	__slots__ = ["_Svc", "_SsnRef"]
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

	_field_defs = frozenset((
		base_types.FieldEntry(name='Svc', type=ATMService11, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SsnRef', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
	))

