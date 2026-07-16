# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import DateFormat73Choice

class Period18(base_types._BaseFieldType):

	__slots__ = ["_EndDt", "_StartDt"]
	@property
	def EndDt(self):
		return self._EndDt

	@EndDt.setter
	def EndDt(self, value):
		self._EndDt = value if value is not None else base_types.UninitialisedField(self, 'EndDt', DateFormat73Choice, False)

	@EndDt.deleter
	def EndDt(self):
		del self._EndDt
		self._EndDt = base_types.UninitialisedField(self, 'EndDt', DateFormat73Choice, False)

	@property
	def StartDt(self):
		return self._StartDt

	@StartDt.setter
	def StartDt(self, value):
		self._StartDt = value if value is not None else base_types.UninitialisedField(self, 'StartDt', DateFormat73Choice, False)

	@StartDt.deleter
	def StartDt(self):
		del self._StartDt
		self._StartDt = base_types.UninitialisedField(self, 'StartDt', DateFormat73Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='EndDt', type=DateFormat73Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StartDt', type=DateFormat73Choice, min=1, max=1, mutex_group=None, array=False),
	))