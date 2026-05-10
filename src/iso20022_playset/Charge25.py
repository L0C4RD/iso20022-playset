import base_types
import ChargesDetails4
import FreightCharges1Code

class Charge25(base_types._BaseFieldType):

	__slots__ = ["_Tp", "_Chrgs"]
	@property
	def Tp(self):
		return self._Tp

	@Tp.setter
	def Tp(self, value):
		self._Tp = value if type(value) != auto else self.make_default("Tp")

	@Tp.deleter
	def Tp(self):
		del self._Tp
		self._Tp = None

	@property
	def Chrgs(self):
		return self._Chrgs

	@Chrgs.setter
	def Chrgs(self, value):
		self._Chrgs = value if type(value) != auto else self.make_default("Chrgs")

	@Chrgs.deleter
	def Chrgs(self):
		del self._Chrgs
		self._Chrgs = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Tp', type=FreightCharges1Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Chrgs', type=ChargesDetails4, min=0, max=None, mutex_group=None, array=True),
	))

