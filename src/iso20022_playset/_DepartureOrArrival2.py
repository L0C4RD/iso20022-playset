from . import base_types
from .Max35Text import Max35Text
from .Max35NumericText import Max35NumericText
from .ISODate import ISODate
from .ISOTime import ISOTime

class DepartureOrArrival2(base_types._BaseFieldType):

	__slots__ = ["_Tm", "_RouteNb", "_CrrierCd", "_Dt"]
	@property
	def Tm(self):
		return self._Tm

	@Tm.setter
	def Tm(self, value):
		self._Tm = value if type(value) != base_types.auto else self.make_default("Tm")

	@Tm.deleter
	def Tm(self):
		del self._Tm
		self._Tm = None

	@property
	def RouteNb(self):
		return self._RouteNb

	@RouteNb.setter
	def RouteNb(self, value):
		self._RouteNb = value if type(value) != base_types.auto else self.make_default("RouteNb")

	@RouteNb.deleter
	def RouteNb(self):
		del self._RouteNb
		self._RouteNb = None

	@property
	def CrrierCd(self):
		return self._CrrierCd

	@CrrierCd.setter
	def CrrierCd(self, value):
		self._CrrierCd = value if type(value) != base_types.auto else self.make_default("CrrierCd")

	@CrrierCd.deleter
	def CrrierCd(self):
		del self._CrrierCd
		self._CrrierCd = None

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
		base_types.FieldEntry(name='Tm', type=ISOTime, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RouteNb', type=Max35NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CrrierCd', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Dt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
	))

