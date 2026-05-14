# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._ISODate import ISODate

class DatePeriod2(base_types._BaseFieldType):

	__slots__ = ["_FrDt", "_ToDt"]
	@property
	def FrDt(self):
		return self._FrDt

	@FrDt.setter
	def FrDt(self, value):
		self._FrDt = value if type(value) != base_types.auto else self.make_default("FrDt")

	@FrDt.deleter
	def FrDt(self):
		del self._FrDt
		self._FrDt = None

	@property
	def ToDt(self):
		return self._ToDt

	@ToDt.setter
	def ToDt(self, value):
		self._ToDt = value if type(value) != base_types.auto else self.make_default("ToDt")

	@ToDt.deleter
	def ToDt(self):
		del self._ToDt
		self._ToDt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='FrDt', type=ISODate, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ToDt', type=ISODate, min=1, max=1, mutex_group=None, array=False),
	))