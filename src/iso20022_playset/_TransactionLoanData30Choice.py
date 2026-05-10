from . import base_types
from ._LoanData136 import LoanData136
from ._LoanData135 import LoanData135
from ._LoanData138 import LoanData138
from ._LoanData137 import LoanData137

class TransactionLoanData30Choice(base_types._BaseFieldType):

	__slots__ = ["_MrgnLndg", "_RpTrad", "_BuySellBck", "_SctiesLndg"]
	@property
	def BuySellBck(self):
		return self._BuySellBck

	@BuySellBck.setter
	def BuySellBck(self, value):
		self._BuySellBck = value if type(value) != base_types.auto else self.make_default("BuySellBck")

	@BuySellBck.deleter
	def BuySellBck(self):
		del self._BuySellBck
		self._BuySellBck = None

	@property
	def MrgnLndg(self):
		return self._MrgnLndg

	@MrgnLndg.setter
	def MrgnLndg(self, value):
		self._MrgnLndg = value if type(value) != base_types.auto else self.make_default("MrgnLndg")

	@MrgnLndg.deleter
	def MrgnLndg(self):
		del self._MrgnLndg
		self._MrgnLndg = None

	@property
	def RpTrad(self):
		return self._RpTrad

	@RpTrad.setter
	def RpTrad(self, value):
		self._RpTrad = value if type(value) != base_types.auto else self.make_default("RpTrad")

	@RpTrad.deleter
	def RpTrad(self):
		del self._RpTrad
		self._RpTrad = None

	@property
	def SctiesLndg(self):
		return self._SctiesLndg

	@SctiesLndg.setter
	def SctiesLndg(self, value):
		self._SctiesLndg = value if type(value) != base_types.auto else self.make_default("SctiesLndg")

	@SctiesLndg.deleter
	def SctiesLndg(self):
		del self._SctiesLndg
		self._SctiesLndg = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='BuySellBck', type=LoanData136, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='MrgnLndg', type=LoanData138, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='RpTrad', type=LoanData135, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='SctiesLndg', type=LoanData137, min=0, max=1, mutex_group=1, array=False),
	))

