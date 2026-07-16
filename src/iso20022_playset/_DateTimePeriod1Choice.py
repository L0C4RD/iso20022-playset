# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import DateTimePeriod1
from . import ISODateTime

class DateTimePeriod1Choice(base_types._BaseFieldType):

	__slots__ = ["_DtTmRg", "_FrDtTm", "_ToDtTm"]
	@property
	def DtTmRg(self):
		return self._DtTmRg

	@DtTmRg.setter
	def DtTmRg(self, value):
		self._DtTmRg = value if value is not None else base_types.UninitialisedField(self, 'DtTmRg', DateTimePeriod1, False)

	@DtTmRg.deleter
	def DtTmRg(self):
		del self._DtTmRg
		self._DtTmRg = base_types.UninitialisedField(self, 'DtTmRg', DateTimePeriod1, False)

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
		base_types.FieldEntry(name='DtTmRg', type=DateTimePeriod1, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='FrDtTm', type=ISODateTime, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='ToDtTm', type=ISODateTime, min=0, max=1, mutex_group=1, array=False),
	))