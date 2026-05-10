from . import base_types
from .CardPaymentEnvironment81 import CardPaymentEnvironment81
from .CardPaymentTransaction137 import CardPaymentTransaction137
from .CurrencyConversion31 import CurrencyConversion31

class AcceptorCurrencyConversionResponse12(base_types._BaseFieldType):

	__slots__ = ["_CcyConvsRslt", "_Tx", "_Envt"]
	@property
	def CcyConvsRslt(self):
		return self._CcyConvsRslt

	@CcyConvsRslt.setter
	def CcyConvsRslt(self, value):
		self._CcyConvsRslt = value if type(value) != base_types.auto else self.make_default("CcyConvsRslt")

	@CcyConvsRslt.deleter
	def CcyConvsRslt(self):
		del self._CcyConvsRslt
		self._CcyConvsRslt = None

	@property
	def Tx(self):
		return self._Tx

	@Tx.setter
	def Tx(self, value):
		self._Tx = value if type(value) != base_types.auto else self.make_default("Tx")

	@Tx.deleter
	def Tx(self):
		del self._Tx
		self._Tx = None

	@property
	def Envt(self):
		return self._Envt

	@Envt.setter
	def Envt(self, value):
		self._Envt = value if type(value) != base_types.auto else self.make_default("Envt")

	@Envt.deleter
	def Envt(self):
		del self._Envt
		self._Envt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='CcyConvsRslt', type=CurrencyConversion31, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tx', type=CardPaymentTransaction137, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Envt', type=CardPaymentEnvironment81, min=1, max=1, mutex_group=None, array=False),
	))

