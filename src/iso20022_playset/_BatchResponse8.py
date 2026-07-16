# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import PerformedTransaction8
from . import TransactionIdentifier1

class BatchResponse8(base_types._BaseFieldType):

	__slots__ = ["_POIBtchId", "_PrfrmdTx", "_SaleBtchId"]
	@property
	def POIBtchId(self):
		return self._POIBtchId

	@POIBtchId.setter
	def POIBtchId(self, value):
		self._POIBtchId = value if value is not None else base_types.UninitialisedField(self, 'POIBtchId', TransactionIdentifier1, False)

	@POIBtchId.deleter
	def POIBtchId(self):
		del self._POIBtchId
		self._POIBtchId = base_types.UninitialisedField(self, 'POIBtchId', TransactionIdentifier1, False)

	@property
	def PrfrmdTx(self):
		return self._PrfrmdTx

	@PrfrmdTx.setter
	def PrfrmdTx(self, value):
		self._PrfrmdTx = value if value is not None else base_types.UninitialisedField(self, 'PrfrmdTx', PerformedTransaction8, True)

	@PrfrmdTx.deleter
	def PrfrmdTx(self):
		del self._PrfrmdTx
		self._PrfrmdTx = base_types.UninitialisedField(self, 'PrfrmdTx', PerformedTransaction8, True)

	@property
	def SaleBtchId(self):
		return self._SaleBtchId

	@SaleBtchId.setter
	def SaleBtchId(self, value):
		self._SaleBtchId = value if value is not None else base_types.UninitialisedField(self, 'SaleBtchId', TransactionIdentifier1, False)

	@SaleBtchId.deleter
	def SaleBtchId(self):
		del self._SaleBtchId
		self._SaleBtchId = base_types.UninitialisedField(self, 'SaleBtchId', TransactionIdentifier1, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='POIBtchId', type=TransactionIdentifier1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrfrmdTx', type=PerformedTransaction8, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SaleBtchId', type=TransactionIdentifier1, min=0, max=1, mutex_group=None, array=False),
	))