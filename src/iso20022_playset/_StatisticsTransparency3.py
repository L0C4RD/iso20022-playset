# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActiveCurrencyAndAmount
from . import DecimalNumber
from . import Number

class StatisticsTransparency3(base_types._BaseFieldType):

	__slots__ = ["_AvrgDalyNbOfTxs", "_AvrgDalyTrnvr", "_AvrgTxVal", "_LrgInScale", "_StdMktSz", "_TtlNbOfTradgDays", "_TtlNbOfTxsExctd", "_TtlVolOfTxsExctd"]
	@property
	def AvrgDalyNbOfTxs(self):
		return self._AvrgDalyNbOfTxs

	@AvrgDalyNbOfTxs.setter
	def AvrgDalyNbOfTxs(self, value):
		self._AvrgDalyNbOfTxs = value if value is not None else base_types.UninitialisedField(self, 'AvrgDalyNbOfTxs', DecimalNumber, False)

	@AvrgDalyNbOfTxs.deleter
	def AvrgDalyNbOfTxs(self):
		del self._AvrgDalyNbOfTxs
		self._AvrgDalyNbOfTxs = base_types.UninitialisedField(self, 'AvrgDalyNbOfTxs', DecimalNumber, False)

	@property
	def AvrgDalyTrnvr(self):
		return self._AvrgDalyTrnvr

	@AvrgDalyTrnvr.setter
	def AvrgDalyTrnvr(self, value):
		self._AvrgDalyTrnvr = value if value is not None else base_types.UninitialisedField(self, 'AvrgDalyTrnvr', ActiveCurrencyAndAmount, False)

	@AvrgDalyTrnvr.deleter
	def AvrgDalyTrnvr(self):
		del self._AvrgDalyTrnvr
		self._AvrgDalyTrnvr = base_types.UninitialisedField(self, 'AvrgDalyTrnvr', ActiveCurrencyAndAmount, False)

	@property
	def AvrgTxVal(self):
		return self._AvrgTxVal

	@AvrgTxVal.setter
	def AvrgTxVal(self, value):
		self._AvrgTxVal = value if value is not None else base_types.UninitialisedField(self, 'AvrgTxVal', ActiveCurrencyAndAmount, False)

	@AvrgTxVal.deleter
	def AvrgTxVal(self):
		del self._AvrgTxVal
		self._AvrgTxVal = base_types.UninitialisedField(self, 'AvrgTxVal', ActiveCurrencyAndAmount, False)

	@property
	def LrgInScale(self):
		return self._LrgInScale

	@LrgInScale.setter
	def LrgInScale(self, value):
		self._LrgInScale = value if value is not None else base_types.UninitialisedField(self, 'LrgInScale', DecimalNumber, False)

	@LrgInScale.deleter
	def LrgInScale(self):
		del self._LrgInScale
		self._LrgInScale = base_types.UninitialisedField(self, 'LrgInScale', DecimalNumber, False)

	@property
	def StdMktSz(self):
		return self._StdMktSz

	@StdMktSz.setter
	def StdMktSz(self, value):
		self._StdMktSz = value if value is not None else base_types.UninitialisedField(self, 'StdMktSz', DecimalNumber, False)

	@StdMktSz.deleter
	def StdMktSz(self):
		del self._StdMktSz
		self._StdMktSz = base_types.UninitialisedField(self, 'StdMktSz', DecimalNumber, False)

	@property
	def TtlNbOfTradgDays(self):
		return self._TtlNbOfTradgDays

	@TtlNbOfTradgDays.setter
	def TtlNbOfTradgDays(self, value):
		self._TtlNbOfTradgDays = value if value is not None else base_types.UninitialisedField(self, 'TtlNbOfTradgDays', Number, False)

	@TtlNbOfTradgDays.deleter
	def TtlNbOfTradgDays(self):
		del self._TtlNbOfTradgDays
		self._TtlNbOfTradgDays = base_types.UninitialisedField(self, 'TtlNbOfTradgDays', Number, False)

	@property
	def TtlNbOfTxsExctd(self):
		return self._TtlNbOfTxsExctd

	@TtlNbOfTxsExctd.setter
	def TtlNbOfTxsExctd(self, value):
		self._TtlNbOfTxsExctd = value if value is not None else base_types.UninitialisedField(self, 'TtlNbOfTxsExctd', DecimalNumber, False)

	@TtlNbOfTxsExctd.deleter
	def TtlNbOfTxsExctd(self):
		del self._TtlNbOfTxsExctd
		self._TtlNbOfTxsExctd = base_types.UninitialisedField(self, 'TtlNbOfTxsExctd', DecimalNumber, False)

	@property
	def TtlVolOfTxsExctd(self):
		return self._TtlVolOfTxsExctd

	@TtlVolOfTxsExctd.setter
	def TtlVolOfTxsExctd(self, value):
		self._TtlVolOfTxsExctd = value if value is not None else base_types.UninitialisedField(self, 'TtlVolOfTxsExctd', DecimalNumber, False)

	@TtlVolOfTxsExctd.deleter
	def TtlVolOfTxsExctd(self):
		del self._TtlVolOfTxsExctd
		self._TtlVolOfTxsExctd = base_types.UninitialisedField(self, 'TtlVolOfTxsExctd', DecimalNumber, False)

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