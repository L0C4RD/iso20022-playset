# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import TradeTransactionIdentification16
from . import TradeTransactionIdentification17
from . import TradeTransactionIdentification20

class TransactionIdentification3Choice(base_types._BaseFieldType):

	__slots__ = ["_CollReuse", "_MrgnRptg", "_Tx"]
	@property
	def CollReuse(self):
		return self._CollReuse

	@CollReuse.setter
	def CollReuse(self, value):
		self._CollReuse = value if value is not None else base_types.UninitialisedField(self, 'CollReuse', TradeTransactionIdentification17, False)

	@CollReuse.deleter
	def CollReuse(self):
		del self._CollReuse
		self._CollReuse = base_types.UninitialisedField(self, 'CollReuse', TradeTransactionIdentification17, False)

	@property
	def MrgnRptg(self):
		return self._MrgnRptg

	@MrgnRptg.setter
	def MrgnRptg(self, value):
		self._MrgnRptg = value if value is not None else base_types.UninitialisedField(self, 'MrgnRptg', TradeTransactionIdentification16, False)

	@MrgnRptg.deleter
	def MrgnRptg(self):
		del self._MrgnRptg
		self._MrgnRptg = base_types.UninitialisedField(self, 'MrgnRptg', TradeTransactionIdentification16, False)

	@property
	def Tx(self):
		return self._Tx

	@Tx.setter
	def Tx(self, value):
		self._Tx = value if value is not None else base_types.UninitialisedField(self, 'Tx', TradeTransactionIdentification20, False)

	@Tx.deleter
	def Tx(self):
		del self._Tx
		self._Tx = base_types.UninitialisedField(self, 'Tx', TradeTransactionIdentification20, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='CollReuse', type=TradeTransactionIdentification17, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='MrgnRptg', type=TradeTransactionIdentification16, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Tx', type=TradeTransactionIdentification20, min=0, max=1, mutex_group=1, array=False),
	))