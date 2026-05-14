# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._ISODateTime import ISODateTime

class DateTimePeriod2(base_types._BaseFieldType):

	__slots__ = ["_FrDtTm", "_ToDtTm"]
	@property
	def FrDtTm(self):
		return self._FrDtTm

	@FrDtTm.setter
	def FrDtTm(self, value):
		self._FrDtTm = value if type(value) != base_types.auto else self.make_default("FrDtTm")

	@FrDtTm.deleter
	def FrDtTm(self):
		del self._FrDtTm
		self._FrDtTm = None

	@property
	def ToDtTm(self):
		return self._ToDtTm

	@ToDtTm.setter
	def ToDtTm(self, value):
		self._ToDtTm = value if type(value) != base_types.auto else self.make_default("ToDtTm")

	@ToDtTm.deleter
	def ToDtTm(self):
		del self._ToDtTm
		self._ToDtTm = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='FrDtTm', type=ISODateTime, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ToDtTm', type=ISODateTime, min=0, max=1, mutex_group=None, array=False),
	))