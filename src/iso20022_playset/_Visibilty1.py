# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import DateAndDateTime2Choice
from . import TrueFalseIndicator

class Visibilty1(base_types._BaseFieldType):

	__slots__ = ["_EndDt", "_LtdVsblty", "_StartDt"]
	@property
	def EndDt(self):
		return self._EndDt

	@EndDt.setter
	def EndDt(self, value):
		self._EndDt = value if value is not None else base_types.UninitialisedField(self, 'EndDt', DateAndDateTime2Choice, False)

	@EndDt.deleter
	def EndDt(self):
		del self._EndDt
		self._EndDt = base_types.UninitialisedField(self, 'EndDt', DateAndDateTime2Choice, False)

	@property
	def LtdVsblty(self):
		return self._LtdVsblty

	@LtdVsblty.setter
	def LtdVsblty(self, value):
		self._LtdVsblty = value if value is not None else base_types.UninitialisedField(self, 'LtdVsblty', TrueFalseIndicator, False)

	@LtdVsblty.deleter
	def LtdVsblty(self):
		del self._LtdVsblty
		self._LtdVsblty = base_types.UninitialisedField(self, 'LtdVsblty', TrueFalseIndicator, False)

	@property
	def StartDt(self):
		return self._StartDt

	@StartDt.setter
	def StartDt(self, value):
		self._StartDt = value if value is not None else base_types.UninitialisedField(self, 'StartDt', DateAndDateTime2Choice, False)

	@StartDt.deleter
	def StartDt(self):
		del self._StartDt
		self._StartDt = base_types.UninitialisedField(self, 'StartDt', DateAndDateTime2Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='EndDt', type=DateAndDateTime2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LtdVsblty', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StartDt', type=DateAndDateTime2Choice, min=0, max=1, mutex_group=None, array=False),
	))