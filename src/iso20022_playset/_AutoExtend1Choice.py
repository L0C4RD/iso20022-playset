# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ISODate
from . import Number

class AutoExtend1Choice(base_types._BaseFieldType):

	__slots__ = ["_Days", "_Dt", "_Mnths", "_Yrs"]
	@property
	def Days(self):
		return self._Days

	@Days.setter
	def Days(self, value):
		self._Days = value if value is not None else base_types.UninitialisedField(self, 'Days', Number, False)

	@Days.deleter
	def Days(self):
		del self._Days
		self._Days = base_types.UninitialisedField(self, 'Days', Number, False)

	@property
	def Dt(self):
		return self._Dt

	@Dt.setter
	def Dt(self, value):
		self._Dt = value if value is not None else base_types.UninitialisedField(self, 'Dt', ISODate, False)

	@Dt.deleter
	def Dt(self):
		del self._Dt
		self._Dt = base_types.UninitialisedField(self, 'Dt', ISODate, False)

	@property
	def Mnths(self):
		return self._Mnths

	@Mnths.setter
	def Mnths(self, value):
		self._Mnths = value if value is not None else base_types.UninitialisedField(self, 'Mnths', Number, False)

	@Mnths.deleter
	def Mnths(self):
		del self._Mnths
		self._Mnths = base_types.UninitialisedField(self, 'Mnths', Number, False)

	@property
	def Yrs(self):
		return self._Yrs

	@Yrs.setter
	def Yrs(self, value):
		self._Yrs = value if value is not None else base_types.UninitialisedField(self, 'Yrs', Number, False)

	@Yrs.deleter
	def Yrs(self):
		del self._Yrs
		self._Yrs = base_types.UninitialisedField(self, 'Yrs', Number, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Days', type=Number, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Dt', type=ISODate, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Mnths', type=Number, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Yrs', type=Number, min=0, max=1, mutex_group=1, array=False),
	))