from . import base_types
from ._YesNoIndicator import YesNoIndicator
from ._RegistrationReason6 import RegistrationReason6

class HoldIndicator7(base_types._BaseFieldType):

	__slots__ = ["_Ind", "_Rsn"]
	@property
	def Ind(self):
		return self._Ind

	@Ind.setter
	def Ind(self, value):
		self._Ind = value if type(value) != base_types.auto else self.make_default("Ind")

	@Ind.deleter
	def Ind(self):
		del self._Ind
		self._Ind = None

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

	_field_defs = frozenset((
		base_types.FieldEntry(name='Ind', type=YesNoIndicator, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Rsn', type=RegistrationReason6, min=0, max=None, mutex_group=None, array=True),
	))

