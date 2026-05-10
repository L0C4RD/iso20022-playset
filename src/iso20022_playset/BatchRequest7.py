from . import base_types
import TransactionIdentifier1
import TransactionToPerform7Choice
import TrueFalseIndicator

class BatchRequest7(base_types._BaseFieldType):

	__slots__ = ["_TxToPrfrm", "_SaleBtchId", "_RmvAllFlg"]
	@property
	def TxToPrfrm(self):
		return self._TxToPrfrm

	@TxToPrfrm.setter
	def TxToPrfrm(self, value):
		self._TxToPrfrm = value if type(value) != auto else self.make_default("TxToPrfrm")

	@TxToPrfrm.deleter
	def TxToPrfrm(self):
		del self._TxToPrfrm
		self._TxToPrfrm = None

	@property
	def SaleBtchId(self):
		return self._SaleBtchId

	@SaleBtchId.setter
	def SaleBtchId(self, value):
		self._SaleBtchId = value if type(value) != auto else self.make_default("SaleBtchId")

	@SaleBtchId.deleter
	def SaleBtchId(self):
		del self._SaleBtchId
		self._SaleBtchId = None

	@property
	def RmvAllFlg(self):
		return self._RmvAllFlg

	@RmvAllFlg.setter
	def RmvAllFlg(self, value):
		self._RmvAllFlg = value if type(value) != auto else self.make_default("RmvAllFlg")

	@RmvAllFlg.deleter
	def RmvAllFlg(self):
		del self._RmvAllFlg
		self._RmvAllFlg = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='TxToPrfrm', type=TransactionToPerform7Choice, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SaleBtchId', type=TransactionIdentifier1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RmvAllFlg', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
	))

