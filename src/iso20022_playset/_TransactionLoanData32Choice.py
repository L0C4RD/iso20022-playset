from . import base_types
from ._LoanData145 import LoanData145
from ._LoanData144 import LoanData144
from ._LoanData143 import LoanData143

class TransactionLoanData32Choice(base_types._BaseFieldType):

	__slots__ = ["_SctiesLndg", "_RpTrad", "_BuySellBck"]
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
		base_types.FieldEntry(name='BuySellBck', type=LoanData144, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='RpTrad', type=LoanData143, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='SctiesLndg', type=LoanData145, min=0, max=1, mutex_group=1, array=False),
	))

