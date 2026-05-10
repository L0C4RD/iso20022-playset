from . import base_types
from .Number import Number
from .DecimalNumber import DecimalNumber

class StatisticsTransparency2(base_types._BaseFieldType):

	__slots__ = ["_TtlNbOfTxsExctd", "_TtlVolOfTxsExctd"]
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
		base_types.FieldEntry(name='TtlNbOfTxsExctd', type=Number, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlVolOfTxsExctd', type=DecimalNumber, min=1, max=1, mutex_group=None, array=False),
	))

