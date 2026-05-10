from . import base_types
from ._InterestComputationMethod4Code import InterestComputationMethod4Code
from ._Max1000Text import Max1000Text

class InterestComputationMethodFormat7(base_types._BaseFieldType):

	__slots__ = ["_Cd", "_Nrrtv"]
	@property
	def Cd(self):
		return self._Cd

	@Cd.setter
	def Cd(self, value):
		self._Cd = value if type(value) != base_types.auto else self.make_default("Cd")

	@Cd.deleter
	def Cd(self):
		del self._Cd
		self._Cd = None

	@property
	def Nrrtv(self):
		return self._Nrrtv

	@Nrrtv.setter
	def Nrrtv(self, value):
		self._Nrrtv = value if type(value) != base_types.auto else self.make_default("Nrrtv")

	@Nrrtv.deleter
	def Nrrtv(self):
		del self._Nrrtv
		self._Nrrtv = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Cd', type=InterestComputationMethod4Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Nrrtv', type=Max1000Text, min=0, max=1, mutex_group=None, array=False),
	))

