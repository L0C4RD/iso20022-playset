from . import base_types
from ._DateFormat41Choice import DateFormat41Choice

class CorporateActionDate89(base_types._BaseFieldType):

	__slots__ = ["_ExDvddDt", "_RcrdDt"]
	@property
	def ExDvddDt(self):
		return self._ExDvddDt

	@ExDvddDt.setter
	def ExDvddDt(self, value):
		self._ExDvddDt = value if type(value) != base_types.auto else self.make_default("ExDvddDt")

	@ExDvddDt.deleter
	def ExDvddDt(self):
		del self._ExDvddDt
		self._ExDvddDt = None

	@property
	def RcrdDt(self):
		return self._RcrdDt

	@RcrdDt.setter
	def RcrdDt(self, value):
		self._RcrdDt = value if type(value) != base_types.auto else self.make_default("RcrdDt")

	@RcrdDt.deleter
	def RcrdDt(self):
		del self._RcrdDt
		self._RcrdDt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='ExDvddDt', type=DateFormat41Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RcrdDt', type=DateFormat41Choice, min=0, max=1, mutex_group=None, array=False),
	))

