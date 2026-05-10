from . import base_types
from .PriceStatus1Code import PriceStatus1Code
from .DigitalTokenAmount2 import DigitalTokenAmount2
from .ActiveOrHistoricCurrencyCode import ActiveOrHistoricCurrencyCode

class SecuritiesTransactionPrice6(base_types._BaseFieldType):

	__slots__ = ["_Ccy", "_Pdg", "_DgtlTkn"]
	@property
	def Ccy(self):
		return self._Ccy

	@Ccy.setter
	def Ccy(self, value):
		self._Ccy = value if type(value) != base_types.auto else self.make_default("Ccy")

	@Ccy.deleter
	def Ccy(self):
		del self._Ccy
		self._Ccy = None

	@property
	def Pdg(self):
		return self._Pdg

	@Pdg.setter
	def Pdg(self, value):
		self._Pdg = value if type(value) != base_types.auto else self.make_default("Pdg")

	@Pdg.deleter
	def Pdg(self):
		del self._Pdg
		self._Pdg = None

	@property
	def DgtlTkn(self):
		return self._DgtlTkn

	@DgtlTkn.setter
	def DgtlTkn(self, value):
		self._DgtlTkn = value if type(value) != base_types.auto else self.make_default("DgtlTkn")

	@DgtlTkn.deleter
	def DgtlTkn(self):
		del self._DgtlTkn
		self._DgtlTkn = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Ccy', type=ActiveOrHistoricCurrencyCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Pdg', type=PriceStatus1Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DgtlTkn', type=DigitalTokenAmount2, min=0, max=None, mutex_group=None, array=True),
	))

