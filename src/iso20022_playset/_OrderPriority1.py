from . import base_types
from ._PositiveNumber import PositiveNumber
from ._ISODateTime import ISODateTime

class OrderPriority1(base_types._BaseFieldType):

	__slots__ = ["_TmStmp", "_Sz"]
	@property
	def TmStmp(self):
		return self._TmStmp

	@TmStmp.setter
	def TmStmp(self, value):
		self._TmStmp = value if type(value) != base_types.auto else self.make_default("TmStmp")

	@TmStmp.deleter
	def TmStmp(self):
		del self._TmStmp
		self._TmStmp = None

	@property
	def Sz(self):
		return self._Sz

	@Sz.setter
	def Sz(self, value):
		self._Sz = value if type(value) != base_types.auto else self.make_default("Sz")

	@Sz.deleter
	def Sz(self):
		del self._Sz
		self._Sz = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='TmStmp', type=ISODateTime, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Sz', type=PositiveNumber, min=0, max=1, mutex_group=None, array=False),
	))

