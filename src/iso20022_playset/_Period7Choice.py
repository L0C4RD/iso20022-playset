# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import DateTimePeriod1
from . import Period2

class Period7Choice(base_types._BaseFieldType):

	__slots__ = ["_FrDtTmToDtTm", "_FrDtToDt"]
	@property
	def FrDtTmToDtTm(self):
		return self._FrDtTmToDtTm

	@FrDtTmToDtTm.setter
	def FrDtTmToDtTm(self, value):
		self._FrDtTmToDtTm = value if value is not None else base_types.UninitialisedField(self, 'FrDtTmToDtTm', DateTimePeriod1, False)

	@FrDtTmToDtTm.deleter
	def FrDtTmToDtTm(self):
		del self._FrDtTmToDtTm
		self._FrDtTmToDtTm = base_types.UninitialisedField(self, 'FrDtTmToDtTm', DateTimePeriod1, False)

	@property
	def FrDtToDt(self):
		return self._FrDtToDt

	@FrDtToDt.setter
	def FrDtToDt(self, value):
		self._FrDtToDt = value if value is not None else base_types.UninitialisedField(self, 'FrDtToDt', Period2, False)

	@FrDtToDt.deleter
	def FrDtToDt(self):
		del self._FrDtToDt
		self._FrDtToDt = base_types.UninitialisedField(self, 'FrDtToDt', Period2, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='FrDtTmToDtTm', type=DateTimePeriod1, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='FrDtToDt', type=Period2, min=0, max=1, mutex_group=1, array=False),
	))