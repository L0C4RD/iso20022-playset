from . import base_types
from .GenericIdentification1 import GenericIdentification1
from .OtherAmountType1Code import OtherAmountType1Code

class OtherAmountType1Choice(base_types._BaseFieldType):

	__slots__ = ["_Cd", "_PrtryCd"]
	@property
	def Cd(self):
		return self._Cd

	@Cd.setter
	def Cd(self, value):
		self._Cd = value if type(value) != auto else self.make_default("Cd")

	@Cd.deleter
	def Cd(self):
		del self._Cd
		self._Cd = None

	@property
	def PrtryCd(self):
		return self._PrtryCd

	@PrtryCd.setter
	def PrtryCd(self, value):
		self._PrtryCd = value if type(value) != auto else self.make_default("PrtryCd")

	@PrtryCd.deleter
	def PrtryCd(self):
		del self._PrtryCd
		self._PrtryCd = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Cd', type=OtherAmountType1Code, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='PrtryCd', type=GenericIdentification1, min=0, max=1, mutex_group=1, array=False),
	))

