# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ISODate
from . import SecuritiesTransactionPrice17Choice

class Schedule1(base_types._BaseFieldType):

	__slots__ = ["_Pric", "_UadjstdEndDt", "_UadjstdFctvDt"]
	@property
	def Pric(self):
		return self._Pric

	@Pric.setter
	def Pric(self, value):
		self._Pric = value if value is not None else base_types.UninitialisedField(self, 'Pric', SecuritiesTransactionPrice17Choice, False)

	@Pric.deleter
	def Pric(self):
		del self._Pric
		self._Pric = base_types.UninitialisedField(self, 'Pric', SecuritiesTransactionPrice17Choice, False)

	@property
	def UadjstdEndDt(self):
		return self._UadjstdEndDt

	@UadjstdEndDt.setter
	def UadjstdEndDt(self, value):
		self._UadjstdEndDt = value if value is not None else base_types.UninitialisedField(self, 'UadjstdEndDt', ISODate, False)

	@UadjstdEndDt.deleter
	def UadjstdEndDt(self):
		del self._UadjstdEndDt
		self._UadjstdEndDt = base_types.UninitialisedField(self, 'UadjstdEndDt', ISODate, False)

	@property
	def UadjstdFctvDt(self):
		return self._UadjstdFctvDt

	@UadjstdFctvDt.setter
	def UadjstdFctvDt(self, value):
		self._UadjstdFctvDt = value if value is not None else base_types.UninitialisedField(self, 'UadjstdFctvDt', ISODate, False)

	@UadjstdFctvDt.deleter
	def UadjstdFctvDt(self):
		del self._UadjstdFctvDt
		self._UadjstdFctvDt = base_types.UninitialisedField(self, 'UadjstdFctvDt', ISODate, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Pric', type=SecuritiesTransactionPrice17Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UadjstdEndDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UadjstdFctvDt', type=ISODate, min=1, max=1, mutex_group=None, array=False),
	))