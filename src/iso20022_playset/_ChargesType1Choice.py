from . import base_types
from ._Max35Text import Max35Text
from ._ChargeType8Code import ChargeType8Code

class ChargesType1Choice(base_types._BaseFieldType):

	__slots__ = ["_OthrChrgsTp", "_Tp"]
	@property
	def OthrChrgsTp(self):
		return self._OthrChrgsTp

	@OthrChrgsTp.setter
	def OthrChrgsTp(self, value):
		self._OthrChrgsTp = value if type(value) != base_types.auto else self.make_default("OthrChrgsTp")

	@OthrChrgsTp.deleter
	def OthrChrgsTp(self):
		del self._OthrChrgsTp
		self._OthrChrgsTp = None

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
		base_types.FieldEntry(name='OthrChrgsTp', type=Max35Text, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Tp', type=ChargeType8Code, min=0, max=1, mutex_group=1, array=False),
	))

