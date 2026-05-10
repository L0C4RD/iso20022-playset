from . import base_types
from .SystemAndCurrency1 import SystemAndCurrency1
from .ISOYear import ISOYear
from .ISOMonth import ISOMonth

class CalendarSearchCriteria1(base_types._BaseFieldType):

	__slots__ = ["_Mnth", "_Svc", "_Yr"]
	@property
	def Mnth(self):
		return self._Mnth

	@Mnth.setter
	def Mnth(self, value):
		self._Mnth = value if type(value) != base_types.auto else self.make_default("Mnth")

	@Mnth.deleter
	def Mnth(self):
		del self._Mnth
		self._Mnth = None

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
	def Yr(self):
		return self._Yr

	@Yr.setter
	def Yr(self, value):
		self._Yr = value if type(value) != base_types.auto else self.make_default("Yr")

	@Yr.deleter
	def Yr(self):
		del self._Yr
		self._Yr = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Mnth', type=ISOMonth, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Svc', type=SystemAndCurrency1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Yr', type=ISOYear, min=0, max=1, mutex_group=None, array=False),
	))

