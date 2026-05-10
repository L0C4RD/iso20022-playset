from . import base_types
from .DateFormat30Choice import DateFormat30Choice

class CorporateActionDate85(base_types._BaseFieldType):

	__slots__ = ["_RcrdDt", "_LtryDt", "_ExDvddDt"]
	@property
	def RcrdDt(self):
		return self._RcrdDt

	@RcrdDt.setter
	def RcrdDt(self, value):
		self._RcrdDt = value if type(value) != auto else self.make_default("RcrdDt")

	@RcrdDt.deleter
	def RcrdDt(self):
		del self._RcrdDt
		self._RcrdDt = None

	@property
	def LtryDt(self):
		return self._LtryDt

	@LtryDt.setter
	def LtryDt(self, value):
		self._LtryDt = value if type(value) != auto else self.make_default("LtryDt")

	@LtryDt.deleter
	def LtryDt(self):
		del self._LtryDt
		self._LtryDt = None

	@property
	def ExDvddDt(self):
		return self._ExDvddDt

	@ExDvddDt.setter
	def ExDvddDt(self, value):
		self._ExDvddDt = value if type(value) != auto else self.make_default("ExDvddDt")

	@ExDvddDt.deleter
	def ExDvddDt(self):
		del self._ExDvddDt
		self._ExDvddDt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='RcrdDt', type=DateFormat30Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LtryDt', type=DateFormat30Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ExDvddDt', type=DateFormat30Choice, min=0, max=1, mutex_group=None, array=False),
	))

