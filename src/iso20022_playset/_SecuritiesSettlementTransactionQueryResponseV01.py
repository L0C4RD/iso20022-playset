# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Pagination1
from . import SecuritiesReport2
from . import SecuritiesSettlementTransactions6

class SecuritiesSettlementTransactionQueryResponseV01(base_types._BaseFieldType):

	__slots__ = ["_Pgntn", "_RptGnlDtls", "_Txs"]
	@property
	def Pgntn(self):
		return self._Pgntn

	@Pgntn.setter
	def Pgntn(self, value):
		self._Pgntn = value if value is not None else base_types.UninitialisedField(self, 'Pgntn', Pagination1, False)

	@Pgntn.deleter
	def Pgntn(self):
		del self._Pgntn
		self._Pgntn = base_types.UninitialisedField(self, 'Pgntn', Pagination1, False)

	@property
	def RptGnlDtls(self):
		return self._RptGnlDtls

	@RptGnlDtls.setter
	def RptGnlDtls(self, value):
		self._RptGnlDtls = value if value is not None else base_types.UninitialisedField(self, 'RptGnlDtls', SecuritiesReport2, False)

	@RptGnlDtls.deleter
	def RptGnlDtls(self):
		del self._RptGnlDtls
		self._RptGnlDtls = base_types.UninitialisedField(self, 'RptGnlDtls', SecuritiesReport2, False)

	@property
	def Txs(self):
		return self._Txs

	@Txs.setter
	def Txs(self, value):
		self._Txs = value if value is not None else base_types.UninitialisedField(self, 'Txs', SecuritiesSettlementTransactions6, True)

	@Txs.deleter
	def Txs(self):
		del self._Txs
		self._Txs = base_types.UninitialisedField(self, 'Txs', SecuritiesSettlementTransactions6, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Pgntn', type=Pagination1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RptGnlDtls', type=SecuritiesReport2, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Txs', type=SecuritiesSettlementTransactions6, min=0, max=None, mutex_group=None, array=True),
	))