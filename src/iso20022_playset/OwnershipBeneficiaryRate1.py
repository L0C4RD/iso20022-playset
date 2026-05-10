from . import base_types
from .PercentageRate import PercentageRate
from .Max35Text import Max35Text

class OwnershipBeneficiaryRate1(base_types._BaseFieldType):

	__slots__ = ["_Frctn", "_Rate"]
	@property
	def Frctn(self):
		return self._Frctn

	@Frctn.setter
	def Frctn(self, value):
		self._Frctn = value if type(value) != auto else self.make_default("Frctn")

	@Frctn.deleter
	def Frctn(self):
		del self._Frctn
		self._Frctn = None

	@property
	def Rate(self):
		return self._Rate

	@Rate.setter
	def Rate(self, value):
		self._Rate = value if type(value) != auto else self.make_default("Rate")

	@Rate.deleter
	def Rate(self):
		del self._Rate
		self._Rate = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Frctn', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Rate', type=PercentageRate, min=0, max=1, mutex_group=None, array=False),
	))

