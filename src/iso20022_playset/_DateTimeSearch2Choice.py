# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import DateTimePeriod1
from . import ISODateTime

class DateTimeSearch2Choice(base_types._BaseFieldType):

	__slots__ = ["_EQDtTm", "_FrDtTm", "_FrToDtTm", "_NEQDtTm", "_ToDtTm"]
	@property
	def EQDtTm(self):
		return self._EQDtTm

	@EQDtTm.setter
	def EQDtTm(self, value):
		self._EQDtTm = value if value is not None else base_types.UninitialisedField(self, 'EQDtTm', ISODateTime, False)

	@EQDtTm.deleter
	def EQDtTm(self):
		del self._EQDtTm
		self._EQDtTm = base_types.UninitialisedField(self, 'EQDtTm', ISODateTime, False)

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
	def FrToDtTm(self):
		return self._FrToDtTm

	@FrToDtTm.setter
	def FrToDtTm(self, value):
		self._FrToDtTm = value if value is not None else base_types.UninitialisedField(self, 'FrToDtTm', DateTimePeriod1, False)

	@FrToDtTm.deleter
	def FrToDtTm(self):
		del self._FrToDtTm
		self._FrToDtTm = base_types.UninitialisedField(self, 'FrToDtTm', DateTimePeriod1, False)

	@property
	def NEQDtTm(self):
		return self._NEQDtTm

	@NEQDtTm.setter
	def NEQDtTm(self, value):
		self._NEQDtTm = value if value is not None else base_types.UninitialisedField(self, 'NEQDtTm', ISODateTime, False)

	@NEQDtTm.deleter
	def NEQDtTm(self):
		del self._NEQDtTm
		self._NEQDtTm = base_types.UninitialisedField(self, 'NEQDtTm', ISODateTime, False)

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
		base_types.FieldEntry(name='EQDtTm', type=ISODateTime, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='FrDtTm', type=ISODateTime, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='FrToDtTm', type=DateTimePeriod1, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='NEQDtTm', type=ISODateTime, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='ToDtTm', type=ISODateTime, min=0, max=1, mutex_group=1, array=False),
	))