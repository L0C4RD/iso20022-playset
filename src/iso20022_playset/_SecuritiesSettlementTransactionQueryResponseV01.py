from . import base_types
from ._Pagination1 import Pagination1
from ._SecuritiesReport2 import SecuritiesReport2
from ._SecuritiesSettlementTransactions6 import SecuritiesSettlementTransactions6

class SecuritiesSettlementTransactionQueryResponseV01(base_types._BaseFieldType):

	__slots__ = ["_Pgntn", "_RptGnlDtls", "_Txs"]
	@property
	def Pgntn(self):
		return self._Pgntn

	@Pgntn.setter
	def Pgntn(self, value):
		self._Pgntn = value if type(value) != base_types.auto else self.make_default("Pgntn")

	@Pgntn.deleter
	def Pgntn(self):
		del self._Pgntn
		self._Pgntn = None

	@property
	def RptGnlDtls(self):
		return self._RptGnlDtls

	@RptGnlDtls.setter
	def RptGnlDtls(self, value):
		self._RptGnlDtls = value if type(value) != base_types.auto else self.make_default("RptGnlDtls")

	@RptGnlDtls.deleter
	def RptGnlDtls(self):
		del self._RptGnlDtls
		self._RptGnlDtls = None

	@property
	def Txs(self):
		return self._Txs

	@Txs.setter
	def Txs(self, value):
		self._Txs = value if type(value) != base_types.auto else self.make_default("Txs")

	@Txs.deleter
	def Txs(self):
		del self._Txs
		self._Txs = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Pgntn', type=Pagination1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RptGnlDtls', type=SecuritiesReport2, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Txs', type=SecuritiesSettlementTransactions6, min=0, max=None, mutex_group=None, array=True),
	))

