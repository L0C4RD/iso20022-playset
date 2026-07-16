# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CardPaymentDataSet38
from . import DataSetIdentification5
from . import GenericIdentification176
from . import ResponseType10
from . import TransactionTotals12
from . import TrueFalseIndicator

class CardPaymentDataSet39(base_types._BaseFieldType):

	__slots__ = ["_DataSetId", "_DataSetInitr", "_DataSetRslt", "_RjctdTx", "_RmvDataSet", "_RsmdApprvl", "_RsmdRjctn", "_SspdTx", "_TxTtls"]
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
	def DataSetRslt(self):
		return self._DataSetRslt

	@DataSetRslt.setter
	def DataSetRslt(self, value):
		self._DataSetRslt = value if value is not None else base_types.UninitialisedField(self, 'DataSetRslt', ResponseType10, False)

	@DataSetRslt.deleter
	def DataSetRslt(self):
		del self._DataSetRslt
		self._DataSetRslt = base_types.UninitialisedField(self, 'DataSetRslt', ResponseType10, False)

	@property
	def RjctdTx(self):
		return self._RjctdTx

	@RjctdTx.setter
	def RjctdTx(self, value):
		self._RjctdTx = value if value is not None else base_types.UninitialisedField(self, 'RjctdTx', CardPaymentDataSet38, True)

	@RjctdTx.deleter
	def RjctdTx(self):
		del self._RjctdTx
		self._RjctdTx = base_types.UninitialisedField(self, 'RjctdTx', CardPaymentDataSet38, True)

	@property
	def RmvDataSet(self):
		return self._RmvDataSet

	@RmvDataSet.setter
	def RmvDataSet(self, value):
		self._RmvDataSet = value if value is not None else base_types.UninitialisedField(self, 'RmvDataSet', TrueFalseIndicator, False)

	@RmvDataSet.deleter
	def RmvDataSet(self):
		del self._RmvDataSet
		self._RmvDataSet = base_types.UninitialisedField(self, 'RmvDataSet', TrueFalseIndicator, False)

	@property
	def RsmdApprvl(self):
		return self._RsmdApprvl

	@RsmdApprvl.setter
	def RsmdApprvl(self, value):
		self._RsmdApprvl = value if value is not None else base_types.UninitialisedField(self, 'RsmdApprvl', CardPaymentDataSet38, True)

	@RsmdApprvl.deleter
	def RsmdApprvl(self):
		del self._RsmdApprvl
		self._RsmdApprvl = base_types.UninitialisedField(self, 'RsmdApprvl', CardPaymentDataSet38, True)

	@property
	def RsmdRjctn(self):
		return self._RsmdRjctn

	@RsmdRjctn.setter
	def RsmdRjctn(self, value):
		self._RsmdRjctn = value if value is not None else base_types.UninitialisedField(self, 'RsmdRjctn', CardPaymentDataSet38, True)

	@RsmdRjctn.deleter
	def RsmdRjctn(self):
		del self._RsmdRjctn
		self._RsmdRjctn = base_types.UninitialisedField(self, 'RsmdRjctn', CardPaymentDataSet38, True)

	@property
	def SspdTx(self):
		return self._SspdTx

	@SspdTx.setter
	def SspdTx(self, value):
		self._SspdTx = value if value is not None else base_types.UninitialisedField(self, 'SspdTx', CardPaymentDataSet38, True)

	@SspdTx.deleter
	def SspdTx(self):
		del self._SspdTx
		self._SspdTx = base_types.UninitialisedField(self, 'SspdTx', CardPaymentDataSet38, True)

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
		base_types.FieldEntry(name='DataSetId', type=DataSetIdentification5, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DataSetInitr', type=GenericIdentification176, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DataSetRslt', type=ResponseType10, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RjctdTx', type=CardPaymentDataSet38, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='RmvDataSet', type=TrueFalseIndicator, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RsmdApprvl', type=CardPaymentDataSet38, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='RsmdRjctn', type=CardPaymentDataSet38, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SspdTx', type=CardPaymentDataSet38, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='TxTtls', type=TransactionTotals12, min=1, max=None, mutex_group=None, array=True),
	))