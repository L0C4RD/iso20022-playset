from . import base_types
import QuantityBreakdown61
import SecuritiesBalanceType6Choice

class SecuritiesSubBalanceTypeAndQuantityBreakdown5(base_types._BaseFieldType):

	__slots__ = ["_Tp", "_QtyBrkdwn"]
	@property
	def Tp(self):
		return self._Tp

	@Tp.setter
	def Tp(self, value):
		self._Tp = value if type(value) != auto else self.make_default("Tp")

	@Tp.deleter
	def Tp(self):
		del self._Tp
		self._Tp = None

	@property
	def QtyBrkdwn(self):
		return self._QtyBrkdwn

	@QtyBrkdwn.setter
	def QtyBrkdwn(self, value):
		self._QtyBrkdwn = value if type(value) != auto else self.make_default("QtyBrkdwn")

	@QtyBrkdwn.deleter
	def QtyBrkdwn(self):
		del self._QtyBrkdwn
		self._QtyBrkdwn = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Tp', type=SecuritiesBalanceType6Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='QtyBrkdwn', type=QuantityBreakdown61, min=0, max=None, mutex_group=None, array=True),
	))

