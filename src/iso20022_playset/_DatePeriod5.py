# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._ISODate import ISODate

class DatePeriod5(base_types._BaseFieldType):

	__slots__ = ["_CurValDt", "_ReqdValDt"]
	@property
	def CurValDt(self):
		return self._CurValDt

	@CurValDt.setter
	def CurValDt(self, value):
		self._CurValDt = value if type(value) != base_types.auto else self.make_default("CurValDt")

	@CurValDt.deleter
	def CurValDt(self):
		del self._CurValDt
		self._CurValDt = None

	@property
	def ReqdValDt(self):
		return self._ReqdValDt

	@ReqdValDt.setter
	def ReqdValDt(self, value):
		self._ReqdValDt = value if type(value) != base_types.auto else self.make_default("ReqdValDt")

	@ReqdValDt.deleter
	def ReqdValDt(self):
		del self._ReqdValDt
		self._ReqdValDt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='CurValDt', type=ISODate, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ReqdValDt', type=ISODate, min=1, max=1, mutex_group=None, array=False),
	))