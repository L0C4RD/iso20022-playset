import base_types
import ISOYear
import ISOMonth
import SystemAndCurrency1

class CalendarSearchCriteria1(base_types._BaseFieldType):

	__slots__ = ["_Yr", "_Svc", "_Mnth"]
	@property
	def Yr(self):
		return self._Yr

	@Yr.setter
	def Yr(self, value):
		self._Yr = value if type(value) != auto else self.make_default("Yr")

	@Yr.deleter
	def Yr(self):
		del self._Yr
		self._Yr = None

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
	def Mnth(self):
		return self._Mnth

	@Mnth.setter
	def Mnth(self, value):
		self._Mnth = value if type(value) != auto else self.make_default("Mnth")

	@Mnth.deleter
	def Mnth(self):
		del self._Mnth
		self._Mnth = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Yr', type=ISOYear, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Svc', type=SystemAndCurrency1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Mnth', type=ISOMonth, min=0, max=1, mutex_group=None, array=False),
	))

