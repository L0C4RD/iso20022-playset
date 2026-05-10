from . import base_types
from .GenericIdentification30 import GenericIdentification30
from .DateOrDateTimePeriod3Choice import DateOrDateTimePeriod3Choice
from .Removal1Choice import Removal1Choice

class RemovalTypeAndReason1(base_types._BaseFieldType):

	__slots__ = ["_ExclsnPrd", "_Rsn", "_RmvlTp"]
	@property
	def ExclsnPrd(self):
		return self._ExclsnPrd

	@ExclsnPrd.setter
	def ExclsnPrd(self, value):
		self._ExclsnPrd = value if type(value) != base_types.auto else self.make_default("ExclsnPrd")

	@ExclsnPrd.deleter
	def ExclsnPrd(self):
		del self._ExclsnPrd
		self._ExclsnPrd = None

	@property
	def Rsn(self):
		return self._Rsn

	@Rsn.setter
	def Rsn(self, value):
		self._Rsn = value if type(value) != base_types.auto else self.make_default("Rsn")

	@Rsn.deleter
	def Rsn(self):
		del self._Rsn
		self._Rsn = None

	@property
	def RmvlTp(self):
		return self._RmvlTp

	@RmvlTp.setter
	def RmvlTp(self, value):
		self._RmvlTp = value if type(value) != base_types.auto else self.make_default("RmvlTp")

	@RmvlTp.deleter
	def RmvlTp(self):
		del self._RmvlTp
		self._RmvlTp = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='ExclsnPrd', type=DateOrDateTimePeriod3Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Rsn', type=GenericIdentification30, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RmvlTp', type=Removal1Choice, min=1, max=1, mutex_group=None, array=False),
	))

