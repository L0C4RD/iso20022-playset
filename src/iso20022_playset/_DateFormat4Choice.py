# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._DateAndDateTimeChoice import DateAndDateTimeChoice
from ._DateType6Code import DateType6Code
from ._GenericIdentification13 import GenericIdentification13

class DateFormat4Choice(base_types._BaseFieldType):

	__slots__ = ["_Dt", "_NotSpcfdDt", "_Prtry"]
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

	@property
	def NotSpcfdDt(self):
		return self._NotSpcfdDt

	@NotSpcfdDt.setter
	def NotSpcfdDt(self, value):
		self._NotSpcfdDt = value if type(value) != base_types.auto else self.make_default("NotSpcfdDt")

	@NotSpcfdDt.deleter
	def NotSpcfdDt(self):
		del self._NotSpcfdDt
		self._NotSpcfdDt = None

	@property
	def Prtry(self):
		return self._Prtry

	@Prtry.setter
	def Prtry(self, value):
		self._Prtry = value if type(value) != base_types.auto else self.make_default("Prtry")

	@Prtry.deleter
	def Prtry(self):
		del self._Prtry
		self._Prtry = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Dt', type=DateAndDateTimeChoice, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='NotSpcfdDt', type=DateType6Code, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Prtry', type=GenericIdentification13, min=0, max=1, mutex_group=1, array=False),
	))