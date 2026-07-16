# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import DateAndDateTime2Choice
from . import DateCode19Choice
from . import DateCodeAndTimeFormat3

class DateFormat44Choice(base_types._BaseFieldType):

	__slots__ = ["_Dt", "_DtCd", "_DtCdAndTm"]
	@property
	def Dt(self):
		return self._Dt

	@Dt.setter
	def Dt(self, value):
		self._Dt = value if value is not None else base_types.UninitialisedField(self, 'Dt', DateAndDateTime2Choice, False)

	@Dt.deleter
	def Dt(self):
		del self._Dt
		self._Dt = base_types.UninitialisedField(self, 'Dt', DateAndDateTime2Choice, False)

	@property
	def DtCd(self):
		return self._DtCd

	@DtCd.setter
	def DtCd(self, value):
		self._DtCd = value if value is not None else base_types.UninitialisedField(self, 'DtCd', DateCode19Choice, False)

	@DtCd.deleter
	def DtCd(self):
		del self._DtCd
		self._DtCd = base_types.UninitialisedField(self, 'DtCd', DateCode19Choice, False)

	@property
	def DtCdAndTm(self):
		return self._DtCdAndTm

	@DtCdAndTm.setter
	def DtCdAndTm(self, value):
		self._DtCdAndTm = value if value is not None else base_types.UninitialisedField(self, 'DtCdAndTm', DateCodeAndTimeFormat3, False)

	@DtCdAndTm.deleter
	def DtCdAndTm(self):
		del self._DtCdAndTm
		self._DtCdAndTm = base_types.UninitialisedField(self, 'DtCdAndTm', DateCodeAndTimeFormat3, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Dt', type=DateAndDateTime2Choice, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='DtCd', type=DateCode19Choice, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='DtCdAndTm', type=DateCodeAndTimeFormat3, min=0, max=1, mutex_group=1, array=False),
	))