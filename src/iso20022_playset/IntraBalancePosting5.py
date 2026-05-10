from . import base_types
from .IntraBalancePosting6 import IntraBalancePosting6
from .CashSubBalanceTypeAndQuantityBreakdown3 import CashSubBalanceTypeAndQuantityBreakdown3

class IntraBalancePosting5(base_types._BaseFieldType):

	__slots__ = ["_Mvmnt", "_BalFr"]
	@property
	def Mvmnt(self):
		return self._Mvmnt

	@Mvmnt.setter
	def Mvmnt(self, value):
		self._Mvmnt = value if type(value) != auto else self.make_default("Mvmnt")

	@Mvmnt.deleter
	def Mvmnt(self):
		del self._Mvmnt
		self._Mvmnt = None

	@property
	def BalFr(self):
		return self._BalFr

	@BalFr.setter
	def BalFr(self, value):
		self._BalFr = value if type(value) != auto else self.make_default("BalFr")

	@BalFr.deleter
	def BalFr(self):
		del self._BalFr
		self._BalFr = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Mvmnt', type=IntraBalancePosting6, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='BalFr', type=CashSubBalanceTypeAndQuantityBreakdown3, min=1, max=1, mutex_group=None, array=False),
	))

