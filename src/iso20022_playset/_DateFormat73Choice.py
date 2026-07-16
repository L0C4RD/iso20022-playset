# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import DateType8Code
from . import ISODate

class DateFormat73Choice(base_types._BaseFieldType):

	__slots__ = ["_Dt", "_NotSpcfdDt"]
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
	def NotSpcfdDt(self):
		return self._NotSpcfdDt

	@NotSpcfdDt.setter
	def NotSpcfdDt(self, value):
		self._NotSpcfdDt = value if value is not None else base_types.UninitialisedField(self, 'NotSpcfdDt', DateType8Code, False)

	@NotSpcfdDt.deleter
	def NotSpcfdDt(self):
		del self._NotSpcfdDt
		self._NotSpcfdDt = base_types.UninitialisedField(self, 'NotSpcfdDt', DateType8Code, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Dt', type=ISODate, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='NotSpcfdDt', type=DateType8Code, min=0, max=1, mutex_group=1, array=False),
	))