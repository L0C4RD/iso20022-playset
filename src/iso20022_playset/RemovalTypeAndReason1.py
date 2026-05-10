import base_types
import GenericIdentification30
import Removal1Choice
import DateOrDateTimePeriod3Choice

class RemovalTypeAndReason1(base_types._BaseFieldType):

	__slots__ = ["_RmvlTp", "_ExclsnPrd", "_Rsn"]
	@property
	def RmvlTp(self):
		return self._RmvlTp

	@RmvlTp.setter
	def RmvlTp(self, value):
		self._RmvlTp = value if type(value) != auto else self.make_default("RmvlTp")

	@RmvlTp.deleter
	def RmvlTp(self):
		del self._RmvlTp
		self._RmvlTp = None

	@property
	def ExclsnPrd(self):
		return self._ExclsnPrd

	@ExclsnPrd.setter
	def ExclsnPrd(self, value):
		self._ExclsnPrd = value if type(value) != auto else self.make_default("ExclsnPrd")

	@ExclsnPrd.deleter
	def ExclsnPrd(self):
		del self._ExclsnPrd
		self._ExclsnPrd = None

	@property
	def Rsn(self):
		return self._Rsn

	@Rsn.setter
	def Rsn(self, value):
		self._Rsn = value if type(value) != auto else self.make_default("Rsn")

	@Rsn.deleter
	def Rsn(self):
		del self._Rsn
		self._Rsn = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='RmvlTp', type=Removal1Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ExclsnPrd', type=DateOrDateTimePeriod3Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Rsn', type=GenericIdentification30, min=0, max=1, mutex_group=None, array=False),
	))

