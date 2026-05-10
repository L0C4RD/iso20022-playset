from . import base_types
from ._RoundingDirection1Code import RoundingDirection1Code
from ._DecimalNumber import DecimalNumber

class RoundingParameters1(base_types._BaseFieldType):

	__slots__ = ["_RndgDrctn", "_RndgMdlus"]
	@property
	def RndgDrctn(self):
		return self._RndgDrctn

	@RndgDrctn.setter
	def RndgDrctn(self, value):
		self._RndgDrctn = value if type(value) != base_types.auto else self.make_default("RndgDrctn")

	@RndgDrctn.deleter
	def RndgDrctn(self):
		del self._RndgDrctn
		self._RndgDrctn = None

	@property
	def RndgMdlus(self):
		return self._RndgMdlus

	@RndgMdlus.setter
	def RndgMdlus(self, value):
		self._RndgMdlus = value if type(value) != base_types.auto else self.make_default("RndgMdlus")

	@RndgMdlus.deleter
	def RndgMdlus(self):
		del self._RndgMdlus
		self._RndgMdlus = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='RndgDrctn', type=RoundingDirection1Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RndgMdlus', type=DecimalNumber, min=0, max=1, mutex_group=None, array=False),
	))

