from . import base_types
from ._ValuationType1Code import ValuationType1Code
from ._ISODateTime import ISODateTime
from ._AmountAndDirection109 import AmountAndDirection109
from ._LongFraction19DecimalNumber import LongFraction19DecimalNumber

class ContractValuationData8(base_types._BaseFieldType):

	__slots__ = ["_Tp", "_TmStmp", "_CtrctVal", "_Dlta"]
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
		base_types.FieldEntry(name='Dlta', type=LongFraction19DecimalNumber, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TmStmp', type=ISODateTime, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tp', type=ValuationType1Code, min=0, max=1, mutex_group=None, array=False),
	))

