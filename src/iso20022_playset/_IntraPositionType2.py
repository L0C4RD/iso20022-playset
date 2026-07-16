# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import SecuritiesSubBalanceTypeAndQuantityBreakdown3

class IntraPositionType2(base_types._BaseFieldType):

	__slots__ = ["_BalFr", "_BalTo"]
	@property
	def BalFr(self):
		return self._BalFr

	@BalFr.setter
	def BalFr(self, value):
		self._BalFr = value if value is not None else base_types.UninitialisedField(self, 'BalFr', SecuritiesSubBalanceTypeAndQuantityBreakdown3, False)

	@BalFr.deleter
	def BalFr(self):
		del self._BalFr
		self._BalFr = base_types.UninitialisedField(self, 'BalFr', SecuritiesSubBalanceTypeAndQuantityBreakdown3, False)

	@property
	def BalTo(self):
		return self._BalTo

	@BalTo.setter
	def BalTo(self, value):
		self._BalTo = value if value is not None else base_types.UninitialisedField(self, 'BalTo', SecuritiesSubBalanceTypeAndQuantityBreakdown3, False)

	@BalTo.deleter
	def BalTo(self):
		del self._BalTo
		self._BalTo = base_types.UninitialisedField(self, 'BalTo', SecuritiesSubBalanceTypeAndQuantityBreakdown3, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='BalFr', type=SecuritiesSubBalanceTypeAndQuantityBreakdown3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BalTo', type=SecuritiesSubBalanceTypeAndQuantityBreakdown3, min=0, max=1, mutex_group=None, array=False),
	))