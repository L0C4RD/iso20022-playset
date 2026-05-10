from . import base_types
from ._GenericIdentification176 import GenericIdentification176
from ._TrueFalseIndicator import TrueFalseIndicator
from ._CardPaymentDataSet38 import CardPaymentDataSet38
from ._ResponseType10 import ResponseType10
from ._TransactionTotals12 import TransactionTotals12
from ._DataSetIdentification5 import DataSetIdentification5

class CardPaymentDataSet39(base_types._BaseFieldType):

	__slots__ = ["_RsmdApprvl", "_DataSetId", "_TxTtls", "_RsmdRjctn", "_RmvDataSet", "_RjctdTx", "_DataSetInitr", "_SspdTx", "_DataSetRslt"]
	@property
	def RsmdApprvl(self):
		return self._RsmdApprvl

	@RsmdApprvl.setter
	def RsmdApprvl(self, value):
		self._RsmdApprvl = value if type(value) != base_types.auto else self.make_default("RsmdApprvl")

	@RsmdApprvl.deleter
	def RsmdApprvl(self):
		del self._RsmdApprvl
		self._RsmdApprvl = None

	@property
	def DataSetId(self):
		return self._DataSetId

	@DataSetId.setter
	def DataSetId(self, value):
		self._DataSetId = value if type(value) != base_types.auto else self.make_default("DataSetId")

	@DataSetId.deleter
	def DataSetId(self):
		del self._DataSetId
		self._DataSetId = None

	@property
	def TxTtls(self):
		return self._TxTtls

	@TxTtls.setter
	def TxTtls(self, value):
		self._TxTtls = value if type(value) != base_types.auto else self.make_default("TxTtls")

	@TxTtls.deleter
	def TxTtls(self):
		del self._TxTtls
		self._TxTtls = None

	@property
	def RsmdRjctn(self):
		return self._RsmdRjctn

	@RsmdRjctn.setter
	def RsmdRjctn(self, value):
		self._RsmdRjctn = value if type(value) != base_types.auto else self.make_default("RsmdRjctn")

	@RsmdRjctn.deleter
	def RsmdRjctn(self):
		del self._RsmdRjctn
		self._RsmdRjctn = None

	@property
	def RmvDataSet(self):
		return self._RmvDataSet

	@RmvDataSet.setter
	def RmvDataSet(self, value):
		self._RmvDataSet = value if type(value) != base_types.auto else self.make_default("RmvDataSet")

	@RmvDataSet.deleter
	def RmvDataSet(self):
		del self._RmvDataSet
		self._RmvDataSet = None

	@property
	def RjctdTx(self):
		return self._RjctdTx

	@RjctdTx.setter
	def RjctdTx(self, value):
		self._RjctdTx = value if type(value) != base_types.auto else self.make_default("RjctdTx")

	@RjctdTx.deleter
	def RjctdTx(self):
		del self._RjctdTx
		self._RjctdTx = None

	@property
	def DataSetInitr(self):
		return self._DataSetInitr

	@DataSetInitr.setter
	def DataSetInitr(self, value):
		self._DataSetInitr = value if type(value) != base_types.auto else self.make_default("DataSetInitr")

	@DataSetInitr.deleter
	def DataSetInitr(self):
		del self._DataSetInitr
		self._DataSetInitr = None

	@property
	def SspdTx(self):
		return self._SspdTx

	@SspdTx.setter
	def SspdTx(self, value):
		self._SspdTx = value if type(value) != base_types.auto else self.make_default("SspdTx")

	@SspdTx.deleter
	def SspdTx(self):
		del self._SspdTx
		self._SspdTx = None

	@property
	def DataSetRslt(self):
		return self._DataSetRslt

	@DataSetRslt.setter
	def DataSetRslt(self, value):
		self._DataSetRslt = value if type(value) != base_types.auto else self.make_default("DataSetRslt")

	@DataSetRslt.deleter
	def DataSetRslt(self):
		del self._DataSetRslt
		self._DataSetRslt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='RsmdApprvl', type=CardPaymentDataSet38, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='DataSetId', type=DataSetIdentification5, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxTtls', type=TransactionTotals12, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='RsmdRjctn', type=CardPaymentDataSet38, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='RmvDataSet', type=TrueFalseIndicator, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RjctdTx', type=CardPaymentDataSet38, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='DataSetInitr', type=GenericIdentification176, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SspdTx', type=CardPaymentDataSet38, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='DataSetRslt', type=ResponseType10, min=1, max=1, mutex_group=None, array=False),
	))

