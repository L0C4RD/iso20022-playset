# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._DatePeriod3 import DatePeriod3
from ._QueryType3Code import QueryType3Code
from ._TimePeriod2 import TimePeriod2

class ReportingPeriod4(base_types._BaseFieldType):

	__slots__ = ["_FrToDt", "_FrToTm", "_Tp"]
	@property
	def FrToDt(self):
		return self._FrToDt

	@FrToDt.setter
	def FrToDt(self, value):
		self._FrToDt = value if type(value) != base_types.auto else self.make_default("FrToDt")

	@FrToDt.deleter
	def FrToDt(self):
		del self._FrToDt
		self._FrToDt = None

	@property
	def FrToTm(self):
		return self._FrToTm

	@FrToTm.setter
	def FrToTm(self, value):
		self._FrToTm = value if type(value) != base_types.auto else self.make_default("FrToTm")

	@FrToTm.deleter
	def FrToTm(self):
		del self._FrToTm
		self._FrToTm = None

	@property
	def Tp(self):
		return self._Tp

	@Tp.setter
	def Tp(self, value):
		self._Tp = value if type(value) != base_types.auto else self.make_default("Tp")

	@Tp.deleter
	def Tp(self):
		del self._Tp
		self._Tp = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='FrToDt', type=DatePeriod3, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FrToTm', type=TimePeriod2, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tp', type=QueryType3Code, min=1, max=1, mutex_group=None, array=False),
	))