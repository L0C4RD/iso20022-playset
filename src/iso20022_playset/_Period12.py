# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._DateFormat45Choice import DateFormat45Choice

class Period12(base_types._BaseFieldType):

	__slots__ = ["_EndDt", "_StartDt"]
	@property
	def EndDt(self):
		return self._EndDt

	@EndDt.setter
	def EndDt(self, value):
		self._EndDt = value if type(value) != base_types.auto else self.make_default("EndDt")

	@EndDt.deleter
	def EndDt(self):
		del self._EndDt
		self._EndDt = None

	@property
	def StartDt(self):
		return self._StartDt

	@StartDt.setter
	def StartDt(self, value):
		self._StartDt = value if type(value) != base_types.auto else self.make_default("StartDt")

	@StartDt.deleter
	def StartDt(self):
		del self._StartDt
		self._StartDt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='EndDt', type=DateFormat45Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StartDt', type=DateFormat45Choice, min=1, max=1, mutex_group=None, array=False),
	))