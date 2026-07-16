# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ISOTime

class TimePeriod1(base_types._BaseFieldType):

	__slots__ = ["_FrTm", "_ToTm"]
	@property
	def FrTm(self):
		return self._FrTm

	@FrTm.setter
	def FrTm(self, value):
		self._FrTm = value if value is not None else base_types.UninitialisedField(self, 'FrTm', ISOTime, False)

	@FrTm.deleter
	def FrTm(self):
		del self._FrTm
		self._FrTm = base_types.UninitialisedField(self, 'FrTm', ISOTime, False)

	@property
	def ToTm(self):
		return self._ToTm

	@ToTm.setter
	def ToTm(self, value):
		self._ToTm = value if value is not None else base_types.UninitialisedField(self, 'ToTm', ISOTime, False)

	@ToTm.deleter
	def ToTm(self):
		del self._ToTm
		self._ToTm = base_types.UninitialisedField(self, 'ToTm', ISOTime, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='FrTm', type=ISOTime, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ToTm', type=ISOTime, min=1, max=1, mutex_group=None, array=False),
	))