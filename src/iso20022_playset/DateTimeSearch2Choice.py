import base_types
import ISODateTime
import DateTimePeriod1

class DateTimeSearch2Choice(base_types._BaseFieldType):

	__slots__ = ["_EQDtTm", "_FrDtTm", "_NEQDtTm", "_ToDtTm", "_FrToDtTm"]
	@property
	def EQDtTm(self):
		return self._EQDtTm

	@EQDtTm.setter
	def EQDtTm(self, value):
		self._EQDtTm = value if type(value) != auto else self.make_default("EQDtTm")

	@EQDtTm.deleter
	def EQDtTm(self):
		del self._EQDtTm
		self._EQDtTm = None

	@property
	def FrDtTm(self):
		return self._FrDtTm

	@FrDtTm.setter
	def FrDtTm(self, value):
		self._FrDtTm = value if type(value) != auto else self.make_default("FrDtTm")

	@FrDtTm.deleter
	def FrDtTm(self):
		del self._FrDtTm
		self._FrDtTm = None

	@property
	def NEQDtTm(self):
		return self._NEQDtTm

	@NEQDtTm.setter
	def NEQDtTm(self, value):
		self._NEQDtTm = value if type(value) != auto else self.make_default("NEQDtTm")

	@NEQDtTm.deleter
	def NEQDtTm(self):
		del self._NEQDtTm
		self._NEQDtTm = None

	@property
	def ToDtTm(self):
		return self._ToDtTm

	@ToDtTm.setter
	def ToDtTm(self, value):
		self._ToDtTm = value if type(value) != auto else self.make_default("ToDtTm")

	@ToDtTm.deleter
	def ToDtTm(self):
		del self._ToDtTm
		self._ToDtTm = None

	@property
	def FrToDtTm(self):
		return self._FrToDtTm

	@FrToDtTm.setter
	def FrToDtTm(self, value):
		self._FrToDtTm = value if type(value) != auto else self.make_default("FrToDtTm")

	@FrToDtTm.deleter
	def FrToDtTm(self):
		del self._FrToDtTm
		self._FrToDtTm = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='EQDtTm', type=ISODateTime, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='FrDtTm', type=ISODateTime, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='NEQDtTm', type=ISODateTime, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='ToDtTm', type=ISODateTime, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='FrToDtTm', type=DateTimePeriod1, min=0, max=1, mutex_group=1, array=False),
	))

