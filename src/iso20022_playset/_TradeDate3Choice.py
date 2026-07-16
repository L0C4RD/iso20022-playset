# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import DateType1Code
from . import ISODate

class TradeDate3Choice(base_types._BaseFieldType):

	__slots__ = ["_Dt", "_DtCd"]
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
	def DtCd(self):
		return self._DtCd

	@DtCd.setter
	def DtCd(self, value):
		self._DtCd = value if value is not None else base_types.UninitialisedField(self, 'DtCd', DateType1Code, False)

	@DtCd.deleter
	def DtCd(self):
		del self._DtCd
		self._DtCd = base_types.UninitialisedField(self, 'DtCd', DateType1Code, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Dt', type=ISODate, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='DtCd', type=DateType1Code, min=0, max=1, mutex_group=1, array=False),
	))