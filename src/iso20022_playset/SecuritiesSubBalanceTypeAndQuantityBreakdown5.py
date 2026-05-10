from . import base_types
from .QuantityBreakdown61 import QuantityBreakdown61
from .SecuritiesBalanceType6Choice import SecuritiesBalanceType6Choice

class SecuritiesSubBalanceTypeAndQuantityBreakdown5(base_types._BaseFieldType):

	__slots__ = ["_QtyBrkdwn", "_Tp"]
	@property
	def QtyBrkdwn(self):
		return self._QtyBrkdwn

	@QtyBrkdwn.setter
	def QtyBrkdwn(self, value):
		self._QtyBrkdwn = value if type(value) != base_types.auto else self.make_default("QtyBrkdwn")

	@QtyBrkdwn.deleter
	def QtyBrkdwn(self):
		del self._QtyBrkdwn
		self._QtyBrkdwn = None

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
		base_types.FieldEntry(name='QtyBrkdwn', type=QuantityBreakdown61, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Tp', type=SecuritiesBalanceType6Choice, min=1, max=1, mutex_group=None, array=False),
	))

