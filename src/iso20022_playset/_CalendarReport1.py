from . import base_types
from ._CalendarOrBusinessError1Choice import CalendarOrBusinessError1Choice
from ._SystemAndCurrency1 import SystemAndCurrency1

class CalendarReport1(base_types._BaseFieldType):

	__slots__ = ["_CalOrErr", "_Svc"]
	@property
	def CalOrErr(self):
		return self._CalOrErr

	@CalOrErr.setter
	def CalOrErr(self, value):
		self._CalOrErr = value if type(value) != base_types.auto else self.make_default("CalOrErr")

	@CalOrErr.deleter
	def CalOrErr(self):
		del self._CalOrErr
		self._CalOrErr = None

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

	_field_defs = frozenset((
		base_types.FieldEntry(name='CalOrErr', type=CalendarOrBusinessError1Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Svc', type=SystemAndCurrency1, min=0, max=1, mutex_group=None, array=False),
	))

