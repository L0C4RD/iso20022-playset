# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._DatePeriod2 import DatePeriod2
from ._ISODate import ISODate

class DatePeriodSearch1Choice(base_types._BaseFieldType):

	__slots__ = ["_EQDt", "_FrDt", "_FrToDt", "_NEQDt", "_ToDt"]
	@property
	def EQDt(self):
		return self._EQDt

	@EQDt.setter
	def EQDt(self, value):
		self._EQDt = value if type(value) != base_types.auto else self.make_default("EQDt")

	@EQDt.deleter
	def EQDt(self):
		del self._EQDt
		self._EQDt = None

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
	def FrToDt(self):
		return self._FrToDt

	@FrToDt.setter
	def FrToDt(self, value):
		self._FrToDt = value if type(value) != base_types.auto else self.make_default("FrToDt")

	@FrToDt.deleter
	def FrToDt(self):
		del self._FrToDt
		self._FrToDt = None

	@property
	def NEQDt(self):
		return self._NEQDt

	@NEQDt.setter
	def NEQDt(self, value):
		self._NEQDt = value if type(value) != base_types.auto else self.make_default("NEQDt")

	@NEQDt.deleter
	def NEQDt(self):
		del self._NEQDt
		self._NEQDt = None

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
		base_types.FieldEntry(name='EQDt', type=ISODate, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='FrDt', type=ISODate, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='FrToDt', type=DatePeriod2, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='NEQDt', type=ISODate, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='ToDt', type=ISODate, min=0, max=1, mutex_group=1, array=False),
	))