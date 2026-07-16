# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ISODate
from . import Period2

class DateAndPeriod2Choice(base_types._BaseFieldType):

	__slots__ = ["_Dt", "_FrDt", "_Prd", "_ToDt"]
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
	def FrDt(self):
		return self._FrDt

	@FrDt.setter
	def FrDt(self, value):
		self._FrDt = value if value is not None else base_types.UninitialisedField(self, 'FrDt', ISODate, False)

	@FrDt.deleter
	def FrDt(self):
		del self._FrDt
		self._FrDt = base_types.UninitialisedField(self, 'FrDt', ISODate, False)

	@property
	def Prd(self):
		return self._Prd

	@Prd.setter
	def Prd(self, value):
		self._Prd = value if value is not None else base_types.UninitialisedField(self, 'Prd', Period2, False)

	@Prd.deleter
	def Prd(self):
		del self._Prd
		self._Prd = base_types.UninitialisedField(self, 'Prd', Period2, False)

	@property
	def ToDt(self):
		return self._ToDt

	@ToDt.setter
	def ToDt(self, value):
		self._ToDt = value if value is not None else base_types.UninitialisedField(self, 'ToDt', ISODate, False)

	@ToDt.deleter
	def ToDt(self):
		del self._ToDt
		self._ToDt = base_types.UninitialisedField(self, 'ToDt', ISODate, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Dt', type=ISODate, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='FrDt', type=ISODate, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Prd', type=Period2, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='ToDt', type=ISODate, min=0, max=1, mutex_group=1, array=False),
	))