from . import base_types
from .RepurchaseAgreement3 import RepurchaseAgreement3
from .Derivative3 import Derivative3
from .FinancialInstrument59 import FinancialInstrument59

class Product1Choice(base_types._BaseFieldType):

	__slots__ = ["_Deriv", "_SctiesFincgTx", "_Scty"]
	@property
	def Deriv(self):
		return self._Deriv

	@Deriv.setter
	def Deriv(self, value):
		self._Deriv = value if type(value) != auto else self.make_default("Deriv")

	@Deriv.deleter
	def Deriv(self):
		del self._Deriv
		self._Deriv = None

	@property
	def SctiesFincgTx(self):
		return self._SctiesFincgTx

	@SctiesFincgTx.setter
	def SctiesFincgTx(self, value):
		self._SctiesFincgTx = value if type(value) != auto else self.make_default("SctiesFincgTx")

	@SctiesFincgTx.deleter
	def SctiesFincgTx(self):
		del self._SctiesFincgTx
		self._SctiesFincgTx = None

	@property
	def Scty(self):
		return self._Scty

	@Scty.setter
	def Scty(self, value):
		self._Scty = value if type(value) != auto else self.make_default("Scty")

	@Scty.deleter
	def Scty(self):
		del self._Scty
		self._Scty = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Deriv', type=Derivative3, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='SctiesFincgTx', type=RepurchaseAgreement3, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Scty', type=FinancialInstrument59, min=0, max=1, mutex_group=1, array=False),
	))

