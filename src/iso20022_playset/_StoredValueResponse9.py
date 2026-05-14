# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._PaymentReceipt7 import PaymentReceipt7
from ._StoredValueData9 import StoredValueData9
from ._TransactionIdentifier1 import TransactionIdentifier1

class StoredValueResponse9(base_types._BaseFieldType):

	__slots__ = ["_POITxId", "_Rct", "_Rslt", "_SaleTxId"]
	@property
	def POITxId(self):
		return self._POITxId

	@POITxId.setter
	def POITxId(self, value):
		self._POITxId = value if type(value) != base_types.auto else self.make_default("POITxId")

	@POITxId.deleter
	def POITxId(self):
		del self._POITxId
		self._POITxId = None

	@property
	def Rct(self):
		return self._Rct

	@Rct.setter
	def Rct(self, value):
		self._Rct = value if type(value) != base_types.auto else self.make_default("Rct")

	@Rct.deleter
	def Rct(self):
		del self._Rct
		self._Rct = None

	@property
	def Rslt(self):
		return self._Rslt

	@Rslt.setter
	def Rslt(self, value):
		self._Rslt = value if type(value) != base_types.auto else self.make_default("Rslt")

	@Rslt.deleter
	def Rslt(self):
		del self._Rslt
		self._Rslt = None

	@property
	def SaleTxId(self):
		return self._SaleTxId

	@SaleTxId.setter
	def SaleTxId(self, value):
		self._SaleTxId = value if type(value) != base_types.auto else self.make_default("SaleTxId")

	@SaleTxId.deleter
	def SaleTxId(self):
		del self._SaleTxId
		self._SaleTxId = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='POITxId', type=TransactionIdentifier1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Rct', type=PaymentReceipt7, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Rslt', type=StoredValueData9, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SaleTxId', type=TransactionIdentifier1, min=0, max=1, mutex_group=None, array=False),
	))