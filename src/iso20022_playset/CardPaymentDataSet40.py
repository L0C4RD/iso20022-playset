import base_types
import TransactionTotals12
import GenericIdentification176
import CardPaymentDataSetTransaction13Choice
import CommonData14
import DataSetIdentification5
import Traceability8

class CardPaymentDataSet40(base_types._BaseFieldType):

	__slots__ = ["_CmonData", "_DataSetId", "_DataSetInitr", "_TxTtls", "_Tracblt", "_Tx"]
	@property
	def CmonData(self):
		return self._CmonData

	@CmonData.setter
	def CmonData(self, value):
		self._CmonData = value if type(value) != auto else self.make_default("CmonData")

	@CmonData.deleter
	def CmonData(self):
		del self._CmonData
		self._CmonData = None

	@property
	def DataSetId(self):
		return self._DataSetId

	@DataSetId.setter
	def DataSetId(self, value):
		self._DataSetId = value if type(value) != auto else self.make_default("DataSetId")

	@DataSetId.deleter
	def DataSetId(self):
		del self._DataSetId
		self._DataSetId = None

	@property
	def DataSetInitr(self):
		return self._DataSetInitr

	@DataSetInitr.setter
	def DataSetInitr(self, value):
		self._DataSetInitr = value if type(value) != auto else self.make_default("DataSetInitr")

	@DataSetInitr.deleter
	def DataSetInitr(self):
		del self._DataSetInitr
		self._DataSetInitr = None

	@property
	def TxTtls(self):
		return self._TxTtls

	@TxTtls.setter
	def TxTtls(self, value):
		self._TxTtls = value if type(value) != auto else self.make_default("TxTtls")

	@TxTtls.deleter
	def TxTtls(self):
		del self._TxTtls
		self._TxTtls = None

	@property
	def Tracblt(self):
		return self._Tracblt

	@Tracblt.setter
	def Tracblt(self, value):
		self._Tracblt = value if type(value) != auto else self.make_default("Tracblt")

	@Tracblt.deleter
	def Tracblt(self):
		del self._Tracblt
		self._Tracblt = None

	@property
	def Tx(self):
		return self._Tx

	@Tx.setter
	def Tx(self, value):
		self._Tx = value if type(value) != auto else self.make_default("Tx")

	@Tx.deleter
	def Tx(self):
		del self._Tx
		self._Tx = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='CmonData', type=CommonData14, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DataSetId', type=DataSetIdentification5, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DataSetInitr', type=GenericIdentification176, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxTtls', type=TransactionTotals12, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Tracblt', type=Traceability8, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Tx', type=CardPaymentDataSetTransaction13Choice, min=1, max=None, mutex_group=None, array=True),
	))

