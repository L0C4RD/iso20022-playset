# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ISODate

class DatePeriod5(base_types._BaseFieldType):

	__slots__ = ["_CurValDt", "_ReqdValDt"]
	@property
	def CurValDt(self):
		return self._CurValDt

	@CurValDt.setter
	def CurValDt(self, value):
		self._CurValDt = value if value is not None else base_types.UninitialisedField(self, 'CurValDt', ISODate, False)

	@CurValDt.deleter
	def CurValDt(self):
		del self._CurValDt
		self._CurValDt = base_types.UninitialisedField(self, 'CurValDt', ISODate, False)

	@property
	def ReqdValDt(self):
		return self._ReqdValDt

	@ReqdValDt.setter
	def ReqdValDt(self, value):
		self._ReqdValDt = value if value is not None else base_types.UninitialisedField(self, 'ReqdValDt', ISODate, False)

	@ReqdValDt.deleter
	def ReqdValDt(self):
		del self._ReqdValDt
		self._ReqdValDt = base_types.UninitialisedField(self, 'ReqdValDt', ISODate, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='CurValDt', type=ISODate, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ReqdValDt', type=ISODate, min=1, max=1, mutex_group=None, array=False),
	))