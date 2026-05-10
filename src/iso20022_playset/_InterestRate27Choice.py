from . import base_types
from ._FixedRate11 import FixedRate11
from ._FloatingInterestRate22 import FloatingInterestRate22

class InterestRate27Choice(base_types._BaseFieldType):

	__slots__ = ["_Fxd", "_Fltg"]
	@property
	def Fxd(self):
		return self._Fxd

	@Fxd.setter
	def Fxd(self, value):
		self._Fxd = value if type(value) != base_types.auto else self.make_default("Fxd")

	@Fxd.deleter
	def Fxd(self):
		del self._Fxd
		self._Fxd = None

	@property
	def Fltg(self):
		return self._Fltg

	@Fltg.setter
	def Fltg(self, value):
		self._Fltg = value if type(value) != base_types.auto else self.make_default("Fltg")

	@Fltg.deleter
	def Fltg(self):
		del self._Fltg
		self._Fltg = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Fxd', type=FixedRate11, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Fltg', type=FloatingInterestRate22, min=0, max=1, mutex_group=1, array=False),
	))

