from . import base_types
from .ErrorHandling5 import ErrorHandling5
from .Limit7 import Limit7

class LimitOrError4Choice(base_types._BaseFieldType):

	__slots__ = ["_BizErr", "_Lmt"]
	@property
	def BizErr(self):
		return self._BizErr

	@BizErr.setter
	def BizErr(self, value):
		self._BizErr = value if type(value) != base_types.auto else self.make_default("BizErr")

	@BizErr.deleter
	def BizErr(self):
		del self._BizErr
		self._BizErr = None

	@property
	def Lmt(self):
		return self._Lmt

	@Lmt.setter
	def Lmt(self, value):
		self._Lmt = value if type(value) != base_types.auto else self.make_default("Lmt")

	@Lmt.deleter
	def Lmt(self):
		del self._Lmt
		self._Lmt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='BizErr', type=ErrorHandling5, min=1, max=None, mutex_group=1, array=True),
		base_types.FieldEntry(name='Lmt', type=Limit7, min=0, max=1, mutex_group=1, array=False),
	))

