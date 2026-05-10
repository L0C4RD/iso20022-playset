from . import base_types
from ._LongFraction19DecimalNumber import LongFraction19DecimalNumber
from ._ValuationType1Code import ValuationType1Code
from ._AmountAndDirection109 import AmountAndDirection109
from ._ISODateTime import ISODateTime

class ContractValuationData8(base_types._BaseFieldType):

	__slots__ = ["_CtrctVal", "_TmStmp", "_Dlta", "_Tp"]
	@property
	def CtrctVal(self):
		return self._CtrctVal

	@CtrctVal.setter
	def CtrctVal(self, value):
		self._CtrctVal = value if type(value) != base_types.auto else self.make_default("CtrctVal")

	@CtrctVal.deleter
	def CtrctVal(self):
		del self._CtrctVal
		self._CtrctVal = None

	@property
	def TmStmp(self):
		return self._TmStmp

	@TmStmp.setter
	def TmStmp(self, value):
		self._TmStmp = value if type(value) != base_types.auto else self.make_default("TmStmp")

	@TmStmp.deleter
	def TmStmp(self):
		del self._TmStmp
		self._TmStmp = None

	@property
	def Dlta(self):
		return self._Dlta

	@Dlta.setter
	def Dlta(self, value):
		self._Dlta = value if type(value) != base_types.auto else self.make_default("Dlta")

	@Dlta.deleter
	def Dlta(self):
		del self._Dlta
		self._Dlta = None

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
		base_types.FieldEntry(name='CtrctVal', type=AmountAndDirection109, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TmStmp', type=ISODateTime, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Dlta', type=LongFraction19DecimalNumber, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tp', type=ValuationType1Code, min=0, max=1, mutex_group=None, array=False),
	))

