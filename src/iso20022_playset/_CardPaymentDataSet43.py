# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CardPaymentDataSetTransaction14Choice
from . import CommonData15
from . import DataSetIdentification5
from . import GenericIdentification176
from . import Traceability8
from . import TransactionTotals12

class CardPaymentDataSet43(base_types._BaseFieldType):

	__slots__ = ["_CmonData", "_DataSetId", "_DataSetInitr", "_Tracblt", "_Tx", "_TxTtls"]
	@property
	def CmonData(self):
		return self._CmonData

	@CmonData.setter
	def CmonData(self, value):
		self._CmonData = value if value is not None else base_types.UninitialisedField(self, 'CmonData', CommonData15, False)

	@CmonData.deleter
	def CmonData(self):
		del self._CmonData
		self._CmonData = base_types.UninitialisedField(self, 'CmonData', CommonData15, False)

	@property
	def DataSetId(self):
		return self._DataSetId

	@DataSetId.setter
	def DataSetId(self, value):
		self._DataSetId = value if value is not None else base_types.UninitialisedField(self, 'DataSetId', DataSetIdentification5, False)

	@DataSetId.deleter
	def DataSetId(self):
		del self._DataSetId
		self._DataSetId = base_types.UninitialisedField(self, 'DataSetId', DataSetIdentification5, False)

	@property
	def DataSetInitr(self):
		return self._DataSetInitr

	@DataSetInitr.setter
	def DataSetInitr(self, value):
		self._DataSetInitr = value if value is not None else base_types.UninitialisedField(self, 'DataSetInitr', GenericIdentification176, False)

	@DataSetInitr.deleter
	def DataSetInitr(self):
		del self._DataSetInitr
		self._DataSetInitr = base_types.UninitialisedField(self, 'DataSetInitr', GenericIdentification176, False)

	@property
	def Tracblt(self):
		return self._Tracblt

	@Tracblt.setter
	def Tracblt(self, value):
		self._Tracblt = value if value is not None else base_types.UninitialisedField(self, 'Tracblt', Traceability8, True)

	@Tracblt.deleter
	def Tracblt(self):
		del self._Tracblt
		self._Tracblt = base_types.UninitialisedField(self, 'Tracblt', Traceability8, True)

	@property
	def Tx(self):
		return self._Tx

	@Tx.setter
	def Tx(self, value):
		self._Tx = value if value is not None else base_types.UninitialisedField(self, 'Tx', CardPaymentDataSetTransaction14Choice, True)

	@Tx.deleter
	def Tx(self):
		del self._Tx
		self._Tx = base_types.UninitialisedField(self, 'Tx', CardPaymentDataSetTransaction14Choice, True)

	@property
	def TxTtls(self):
		return self._TxTtls

	@TxTtls.setter
	def TxTtls(self, value):
		self._TxTtls = value if value is not None else base_types.UninitialisedField(self, 'TxTtls', TransactionTotals12, True)

	@TxTtls.deleter
	def TxTtls(self):
		del self._TxTtls
		self._TxTtls = base_types.UninitialisedField(self, 'TxTtls', TransactionTotals12, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='CmonData', type=CommonData15, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DataSetId', type=DataSetIdentification5, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DataSetInitr', type=GenericIdentification176, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tracblt', type=Traceability8, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Tx', type=CardPaymentDataSetTransaction14Choice, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='TxTtls', type=TransactionTotals12, min=1, max=None, mutex_group=None, array=True),
	))