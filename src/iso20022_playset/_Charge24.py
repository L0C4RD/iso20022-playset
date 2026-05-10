from . import base_types
from ._ChargesDetails3 import ChargesDetails3
from ._FreightCharges1Code import FreightCharges1Code

class Charge24(base_types._BaseFieldType):

	__slots__ = ["_Tp", "_Chrgs"]
	@property
	def Chrgs(self):
		return self._Chrgs

	@Chrgs.setter
	def Chrgs(self, value):
		self._Chrgs = value if type(value) != base_types.auto else self.make_default("Chrgs")

	@Chrgs.deleter
	def Chrgs(self):
		del self._Chrgs
		self._Chrgs = None

	@property
	def Tp(self):
		return self._Tp

	@Tp.setter
	def Tp(self, value):
		self._Tp = value if type(value) != base_types.auto else self.make_default("Tp")

	@Tp.deleter
	def Tp(self):
		del self._Tp
		self._Tp = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Chrgs', type=ChargesDetails3, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Tp', type=FreightCharges1Code, min=1, max=1, mutex_group=None, array=False),
	))

