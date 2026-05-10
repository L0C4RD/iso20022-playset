from . import base_types
from ._ActiveCurrencyAndAmount import ActiveCurrencyAndAmount
from ._CollateralType22Choice import CollateralType22Choice

class TripartyCollateralAndAmount1(base_types._BaseFieldType):

	__slots__ = ["_Trpty", "_CollTp"]
	@property
	def Trpty(self):
		return self._Trpty

	@Trpty.setter
	def Trpty(self, value):
		self._Trpty = value if type(value) != base_types.auto else self.make_default("Trpty")

	@Trpty.deleter
	def Trpty(self):
		del self._Trpty
		self._Trpty = None

	@property
	def CollTp(self):
		return self._CollTp

	@CollTp.setter
	def CollTp(self, value):
		self._CollTp = value if type(value) != base_types.auto else self.make_default("CollTp")

	@CollTp.deleter
	def CollTp(self):
		del self._CollTp
		self._CollTp = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Trpty', type=ActiveCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CollTp', type=CollateralType22Choice, min=1, max=1, mutex_group=None, array=False),
	))

