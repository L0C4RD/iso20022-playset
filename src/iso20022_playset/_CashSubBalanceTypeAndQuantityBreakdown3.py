# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AmountAndQuantityBreakdown1
from . import CashBalanceType3Choice

class CashSubBalanceTypeAndQuantityBreakdown3(base_types._BaseFieldType):

	__slots__ = ["_QtyBrkdwn", "_Tp"]
	@property
	def QtyBrkdwn(self):
		return self._QtyBrkdwn

	@QtyBrkdwn.setter
	def QtyBrkdwn(self, value):
		self._QtyBrkdwn = value if value is not None else base_types.UninitialisedField(self, 'QtyBrkdwn', AmountAndQuantityBreakdown1, True)

	@QtyBrkdwn.deleter
	def QtyBrkdwn(self):
		del self._QtyBrkdwn
		self._QtyBrkdwn = base_types.UninitialisedField(self, 'QtyBrkdwn', AmountAndQuantityBreakdown1, True)

	@property
	def Tp(self):
		return self._Tp

	@Tp.setter
	def Tp(self, value):
		self._Tp = value if value is not None else base_types.UninitialisedField(self, 'Tp', CashBalanceType3Choice, False)

	@Tp.deleter
	def Tp(self):
		del self._Tp
		self._Tp = base_types.UninitialisedField(self, 'Tp', CashBalanceType3Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='QtyBrkdwn', type=AmountAndQuantityBreakdown1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Tp', type=CashBalanceType3Choice, min=1, max=1, mutex_group=None, array=False),
	))