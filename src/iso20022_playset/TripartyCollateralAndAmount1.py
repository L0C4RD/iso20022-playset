from . import base_types
import CollateralType22Choice
import ActiveCurrencyAndAmount

class TripartyCollateralAndAmount1(base_types._BaseFieldType):

	__slots__ = ["_CollTp", "_Trpty"]
	@property
	def CollTp(self):
		return self._CollTp

	@CollTp.setter
	def CollTp(self, value):
		self._CollTp = value if type(value) != auto else self.make_default("CollTp")

	@CollTp.deleter
	def CollTp(self):
		del self._CollTp
		self._CollTp = None

	@property
	def Trpty(self):
		return self._Trpty

	@Trpty.setter
	def Trpty(self, value):
		self._Trpty = value if type(value) != auto else self.make_default("Trpty")

	@Trpty.deleter
	def Trpty(self):
		del self._Trpty
		self._Trpty = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='CollTp', type=CollateralType22Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Trpty', type=ActiveCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
	))

