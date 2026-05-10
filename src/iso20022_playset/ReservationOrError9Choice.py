from . import base_types
from .Reservation3 import Reservation3
from .ErrorHandling5 import ErrorHandling5

class ReservationOrError9Choice(base_types._BaseFieldType):

	__slots__ = ["_Rsvatn", "_BizErr"]
	@property
	def Rsvatn(self):
		return self._Rsvatn

	@Rsvatn.setter
	def Rsvatn(self, value):
		self._Rsvatn = value if type(value) != auto else self.make_default("Rsvatn")

	@Rsvatn.deleter
	def Rsvatn(self):
		del self._Rsvatn
		self._Rsvatn = None

	@property
	def BizErr(self):
		return self._BizErr

	@BizErr.setter
	def BizErr(self, value):
		self._BizErr = value if type(value) != auto else self.make_default("BizErr")

	@BizErr.deleter
	def BizErr(self):
		del self._BizErr
		self._BizErr = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Rsvatn', type=Reservation3, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='BizErr', type=ErrorHandling5, min=1, max=None, mutex_group=1, array=True),
	))

