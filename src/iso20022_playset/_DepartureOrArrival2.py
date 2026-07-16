# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ISODate
from . import ISOTime
from . import Max35NumericText
from . import Max35Text

class DepartureOrArrival2(base_types._BaseFieldType):

	__slots__ = ["_CrrierCd", "_Dt", "_RouteNb", "_Tm"]
	@property
	def CrrierCd(self):
		return self._CrrierCd

	@CrrierCd.setter
	def CrrierCd(self, value):
		self._CrrierCd = value if value is not None else base_types.UninitialisedField(self, 'CrrierCd', Max35Text, False)

	@CrrierCd.deleter
	def CrrierCd(self):
		del self._CrrierCd
		self._CrrierCd = base_types.UninitialisedField(self, 'CrrierCd', Max35Text, False)

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
	def RouteNb(self):
		return self._RouteNb

	@RouteNb.setter
	def RouteNb(self, value):
		self._RouteNb = value if value is not None else base_types.UninitialisedField(self, 'RouteNb', Max35NumericText, False)

	@RouteNb.deleter
	def RouteNb(self):
		del self._RouteNb
		self._RouteNb = base_types.UninitialisedField(self, 'RouteNb', Max35NumericText, False)

	@property
	def Tm(self):
		return self._Tm

	@Tm.setter
	def Tm(self, value):
		self._Tm = value if value is not None else base_types.UninitialisedField(self, 'Tm', ISOTime, False)

	@Tm.deleter
	def Tm(self):
		del self._Tm
		self._Tm = base_types.UninitialisedField(self, 'Tm', ISOTime, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='CrrierCd', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Dt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RouteNb', type=Max35NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tm', type=ISOTime, min=0, max=1, mutex_group=None, array=False),
	))