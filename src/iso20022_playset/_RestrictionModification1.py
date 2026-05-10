from . import base_types
from .Modification1Code import Modification1Code
from .Restriction1 import Restriction1

class RestrictionModification1(base_types._BaseFieldType):

	__slots__ = ["_Rstrctn", "_ModCd"]
	@property
	def Rstrctn(self):
		return self._Rstrctn

	@Rstrctn.setter
	def Rstrctn(self, value):
		self._Rstrctn = value if type(value) != base_types.auto else self.make_default("Rstrctn")

	@Rstrctn.deleter
	def Rstrctn(self):
		del self._Rstrctn
		self._Rstrctn = None

	@property
	def ModCd(self):
		return self._ModCd

	@ModCd.setter
	def ModCd(self, value):
		self._ModCd = value if type(value) != base_types.auto else self.make_default("ModCd")

	@ModCd.deleter
	def ModCd(self):
		del self._ModCd
		self._ModCd = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Rstrctn', type=Restriction1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ModCd', type=Modification1Code, min=0, max=1, mutex_group=None, array=False),
	))

