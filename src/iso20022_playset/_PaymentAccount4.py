from . import base_types
from ._ActiveCurrencyCode import ActiveCurrencyCode
from ._AmountAndDirection86 import AmountAndDirection86
from ._ImpliedCurrencyAndAmount import ImpliedCurrencyAndAmount
from ._Max10NumericText import Max10NumericText

class PaymentAccount4(base_types._BaseFieldType):

	__slots__ = ["_Ccy", "_GrssCdts", "_GrssDbts", "_LatePmtConf", "_NetPmt"]
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
	def GrssCdts(self):
		return self._GrssCdts

	@GrssCdts.setter
	def GrssCdts(self, value):
		self._GrssCdts = value if type(value) != base_types.auto else self.make_default("GrssCdts")

	@GrssCdts.deleter
	def GrssCdts(self):
		del self._GrssCdts
		self._GrssCdts = None

	@property
	def GrssDbts(self):
		return self._GrssDbts

	@GrssDbts.setter
	def GrssDbts(self, value):
		self._GrssDbts = value if type(value) != base_types.auto else self.make_default("GrssDbts")

	@GrssDbts.deleter
	def GrssDbts(self):
		del self._GrssDbts
		self._GrssDbts = None

	@property
	def LatePmtConf(self):
		return self._LatePmtConf

	@LatePmtConf.setter
	def LatePmtConf(self, value):
		self._LatePmtConf = value if type(value) != base_types.auto else self.make_default("LatePmtConf")

	@LatePmtConf.deleter
	def LatePmtConf(self):
		del self._LatePmtConf
		self._LatePmtConf = None

	@property
	def NetPmt(self):
		return self._NetPmt

	@NetPmt.setter
	def NetPmt(self, value):
		self._NetPmt = value if type(value) != base_types.auto else self.make_default("NetPmt")

	@NetPmt.deleter
	def NetPmt(self):
		del self._NetPmt
		self._NetPmt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Ccy', type=ActiveCurrencyCode, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='GrssCdts', type=ImpliedCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='GrssDbts', type=ImpliedCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LatePmtConf', type=Max10NumericText, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NetPmt', type=AmountAndDirection86, min=1, max=1, mutex_group=None, array=False),
	))

