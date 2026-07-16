# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import DecimalNumber
from . import Number

class StatisticsTransparency2(base_types._BaseFieldType):

	__slots__ = ["_TtlNbOfTxsExctd", "_TtlVolOfTxsExctd"]
	@property
	def TtlNbOfTxsExctd(self):
		return self._TtlNbOfTxsExctd

	@TtlNbOfTxsExctd.setter
	def TtlNbOfTxsExctd(self, value):
		self._TtlNbOfTxsExctd = value if value is not None else base_types.UninitialisedField(self, 'TtlNbOfTxsExctd', Number, False)

	@TtlNbOfTxsExctd.deleter
	def TtlNbOfTxsExctd(self):
		del self._TtlNbOfTxsExctd
		self._TtlNbOfTxsExctd = base_types.UninitialisedField(self, 'TtlNbOfTxsExctd', Number, False)

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
		base_types.FieldEntry(name='TtlNbOfTxsExctd', type=Number, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlVolOfTxsExctd', type=DecimalNumber, min=1, max=1, mutex_group=None, array=False),
	))