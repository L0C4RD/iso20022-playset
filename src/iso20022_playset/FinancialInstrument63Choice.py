from . import base_types
from .OtherAsset2 import OtherAsset2
from .FinancialInstrumentIdentification2 import FinancialInstrumentIdentification2
from .CashAsset3 import CashAsset3

class FinancialInstrument63Choice(base_types._BaseFieldType):

	__slots__ = ["_OthrAsst", "_CshAsst", "_Scty"]
	@property
	def OthrAsst(self):
		return self._OthrAsst

	@OthrAsst.setter
	def OthrAsst(self, value):
		self._OthrAsst = value if type(value) != base_types.auto else self.make_default("OthrAsst")

	@OthrAsst.deleter
	def OthrAsst(self):
		del self._OthrAsst
		self._OthrAsst = None

	@property
	def CshAsst(self):
		return self._CshAsst

	@CshAsst.setter
	def CshAsst(self, value):
		self._CshAsst = value if type(value) != base_types.auto else self.make_default("CshAsst")

	@CshAsst.deleter
	def CshAsst(self):
		del self._CshAsst
		self._CshAsst = None

	@property
	def Scty(self):
		return self._Scty

	@Scty.setter
	def Scty(self, value):
		self._Scty = value if type(value) != base_types.auto else self.make_default("Scty")

	@Scty.deleter
	def Scty(self):
		del self._Scty
		self._Scty = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='OthrAsst', type=OtherAsset2, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='CshAsst', type=CashAsset3, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Scty', type=FinancialInstrumentIdentification2, min=0, max=1, mutex_group=1, array=False),
	))

