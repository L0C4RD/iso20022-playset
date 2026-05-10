from . import base_types
from ._ActiveCurrencyAndAmount import ActiveCurrencyAndAmount
from ._Number import Number
from ._DecimalNumber import DecimalNumber

class StatisticsTransparency3(base_types._BaseFieldType):

	__slots__ = ["_TtlNbOfTxsExctd", "_StdMktSz", "_AvrgTxVal", "_AvrgDalyTrnvr", "_TtlVolOfTxsExctd", "_AvrgDalyNbOfTxs", "_LrgInScale", "_TtlNbOfTradgDays"]
	@property
	def AvrgDalyNbOfTxs(self):
		return self._AvrgDalyNbOfTxs

	@AvrgDalyNbOfTxs.setter
	def AvrgDalyNbOfTxs(self, value):
		self._AvrgDalyNbOfTxs = value if type(value) != base_types.auto else self.make_default("AvrgDalyNbOfTxs")

	@AvrgDalyNbOfTxs.deleter
	def AvrgDalyNbOfTxs(self):
		del self._AvrgDalyNbOfTxs
		self._AvrgDalyNbOfTxs = None

	@property
	def AvrgDalyTrnvr(self):
		return self._AvrgDalyTrnvr

	@AvrgDalyTrnvr.setter
	def AvrgDalyTrnvr(self, value):
		self._AvrgDalyTrnvr = value if type(value) != base_types.auto else self.make_default("AvrgDalyTrnvr")

	@AvrgDalyTrnvr.deleter
	def AvrgDalyTrnvr(self):
		del self._AvrgDalyTrnvr
		self._AvrgDalyTrnvr = None

	@property
	def AvrgTxVal(self):
		return self._AvrgTxVal

	@AvrgTxVal.setter
	def AvrgTxVal(self, value):
		self._AvrgTxVal = value if type(value) != base_types.auto else self.make_default("AvrgTxVal")

	@AvrgTxVal.deleter
	def AvrgTxVal(self):
		del self._AvrgTxVal
		self._AvrgTxVal = None

	@property
	def LrgInScale(self):
		return self._LrgInScale

	@LrgInScale.setter
	def LrgInScale(self, value):
		self._LrgInScale = value if type(value) != base_types.auto else self.make_default("LrgInScale")

	@LrgInScale.deleter
	def LrgInScale(self):
		del self._LrgInScale
		self._LrgInScale = None

	@property
	def StdMktSz(self):
		return self._StdMktSz

	@StdMktSz.setter
	def StdMktSz(self, value):
		self._StdMktSz = value if type(value) != base_types.auto else self.make_default("StdMktSz")

	@StdMktSz.deleter
	def StdMktSz(self):
		del self._StdMktSz
		self._StdMktSz = None

	@property
	def TtlNbOfTradgDays(self):
		return self._TtlNbOfTradgDays

	@TtlNbOfTradgDays.setter
	def TtlNbOfTradgDays(self, value):
		self._TtlNbOfTradgDays = value if type(value) != base_types.auto else self.make_default("TtlNbOfTradgDays")

	@TtlNbOfTradgDays.deleter
	def TtlNbOfTradgDays(self):
		del self._TtlNbOfTradgDays
		self._TtlNbOfTradgDays = None

	@property
	def TtlNbOfTxsExctd(self):
		return self._TtlNbOfTxsExctd

	@TtlNbOfTxsExctd.setter
	def TtlNbOfTxsExctd(self, value):
		self._TtlNbOfTxsExctd = value if type(value) != base_types.auto else self.make_default("TtlNbOfTxsExctd")

	@TtlNbOfTxsExctd.deleter
	def TtlNbOfTxsExctd(self):
		del self._TtlNbOfTxsExctd
		self._TtlNbOfTxsExctd = None

	@property
	def TtlVolOfTxsExctd(self):
		return self._TtlVolOfTxsExctd

	@TtlVolOfTxsExctd.setter
	def TtlVolOfTxsExctd(self, value):
		self._TtlVolOfTxsExctd = value if type(value) != base_types.auto else self.make_default("TtlVolOfTxsExctd")

	@TtlVolOfTxsExctd.deleter
	def TtlVolOfTxsExctd(self):
		del self._TtlVolOfTxsExctd
		self._TtlVolOfTxsExctd = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AvrgDalyNbOfTxs', type=DecimalNumber, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AvrgDalyTrnvr', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AvrgTxVal', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LrgInScale', type=DecimalNumber, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StdMktSz', type=DecimalNumber, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlNbOfTradgDays', type=Number, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlNbOfTxsExctd', type=DecimalNumber, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlVolOfTxsExctd', type=DecimalNumber, min=0, max=1, mutex_group=None, array=False),
	))

