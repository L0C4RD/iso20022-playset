# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ISODateTime

class DateTimePeriodDetails(base_types._BaseFieldType):

	__slots__ = ["_FrDtTm", "_ToDtTm"]
	@property
	def FrDtTm(self):
		return self._FrDtTm

	@FrDtTm.setter
	def FrDtTm(self, value):
		self._FrDtTm = value if value is not None else base_types.UninitialisedField(self, 'FrDtTm', ISODateTime, False)

	@FrDtTm.deleter
	def FrDtTm(self):
		del self._FrDtTm
		self._FrDtTm = base_types.UninitialisedField(self, 'FrDtTm', ISODateTime, False)

	@property
	def ToDtTm(self):
		return self._ToDtTm

	@ToDtTm.setter
	def ToDtTm(self, value):
		self._ToDtTm = value if value is not None else base_types.UninitialisedField(self, 'ToDtTm', ISODateTime, False)

	@ToDtTm.deleter
	def ToDtTm(self):
		del self._ToDtTm
		self._ToDtTm = base_types.UninitialisedField(self, 'ToDtTm', ISODateTime, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='FrDtTm', type=ISODateTime, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ToDtTm', type=ISODateTime, min=1, max=1, mutex_group=None, array=False),
	))