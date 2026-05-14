# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._PerformedTransaction8 import PerformedTransaction8
from ._TransactionIdentifier1 import TransactionIdentifier1

class BatchResponse8(base_types._BaseFieldType):

	__slots__ = ["_POIBtchId", "_PrfrmdTx", "_SaleBtchId"]
	@property
	def POIBtchId(self):
		return self._POIBtchId

	@POIBtchId.setter
	def POIBtchId(self, value):
		self._POIBtchId = value if type(value) != base_types.auto else self.make_default("POIBtchId")

	@POIBtchId.deleter
	def POIBtchId(self):
		del self._POIBtchId
		self._POIBtchId = None

	@property
	def PrfrmdTx(self):
		return self._PrfrmdTx

	@PrfrmdTx.setter
	def PrfrmdTx(self, value):
		self._PrfrmdTx = value if type(value) != base_types.auto else self.make_default("PrfrmdTx")

	@PrfrmdTx.deleter
	def PrfrmdTx(self):
		del self._PrfrmdTx
		self._PrfrmdTx = None

	@property
	def SaleBtchId(self):
		return self._SaleBtchId

	@SaleBtchId.setter
	def SaleBtchId(self, value):
		self._SaleBtchId = value if type(value) != base_types.auto else self.make_default("SaleBtchId")

	@SaleBtchId.deleter
	def SaleBtchId(self):
		del self._SaleBtchId
		self._SaleBtchId = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='POIBtchId', type=TransactionIdentifier1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrfrmdTx', type=PerformedTransaction8, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SaleBtchId', type=TransactionIdentifier1, min=0, max=1, mutex_group=None, array=False),
	))