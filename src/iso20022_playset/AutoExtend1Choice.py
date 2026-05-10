from . import base_types
import ISODate
import Number

class AutoExtend1Choice(base_types._BaseFieldType):

	__slots__ = ["_Yrs", "_Dt", "_Mnths", "_Days"]
	@property
	def Yrs(self):
		return self._Yrs

	@Yrs.setter
	def Yrs(self, value):
		self._Yrs = value if type(value) != auto else self.make_default("Yrs")

	@Yrs.deleter
	def Yrs(self):
		del self._Yrs
		self._Yrs = None

	@property
	def Dt(self):
		return self._Dt

	@Dt.setter
	def Dt(self, value):
		self._Dt = value if type(value) != auto else self.make_default("Dt")

	@Dt.deleter
	def Dt(self):
		del self._Dt
		self._Dt = None

	@property
	def Mnths(self):
		return self._Mnths

	@Mnths.setter
	def Mnths(self, value):
		self._Mnths = value if type(value) != auto else self.make_default("Mnths")

	@Mnths.deleter
	def Mnths(self):
		del self._Mnths
		self._Mnths = None

	@property
	def Days(self):
		return self._Days

	@Days.setter
	def Days(self, value):
		self._Days = value if type(value) != auto else self.make_default("Days")

	@Days.deleter
	def Days(self):
		del self._Days
		self._Days = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Yrs', type=Number, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Dt', type=ISODate, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Mnths', type=Number, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Days', type=Number, min=0, max=1, mutex_group=1, array=False),
	))

