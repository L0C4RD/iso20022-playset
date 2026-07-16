# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import DateCode21Choice
from . import ISOTime

class DateCodeAndTimeFormat3(base_types._BaseFieldType):

	__slots__ = ["_DtCd", "_Tm"]
	@property
	def DtCd(self):
		return self._DtCd

	@DtCd.setter
	def DtCd(self, value):
		self._DtCd = value if value is not None else base_types.UninitialisedField(self, 'DtCd', DateCode21Choice, False)

	@DtCd.deleter
	def DtCd(self):
		del self._DtCd
		self._DtCd = base_types.UninitialisedField(self, 'DtCd', DateCode21Choice, False)

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
		base_types.FieldEntry(name='DtCd', type=DateCode21Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tm', type=ISOTime, min=1, max=1, mutex_group=None, array=False),
	))