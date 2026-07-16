# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import TransactionIdentifier1
from . import TransactionToPerform7Choice
from . import TrueFalseIndicator

class BatchRequest7(base_types._BaseFieldType):

	__slots__ = ["_RmvAllFlg", "_SaleBtchId", "_TxToPrfrm"]
	@property
	def RmvAllFlg(self):
		return self._RmvAllFlg

	@RmvAllFlg.setter
	def RmvAllFlg(self, value):
		self._RmvAllFlg = value if value is not None else base_types.UninitialisedField(self, 'RmvAllFlg', TrueFalseIndicator, False)

	@RmvAllFlg.deleter
	def RmvAllFlg(self):
		del self._RmvAllFlg
		self._RmvAllFlg = base_types.UninitialisedField(self, 'RmvAllFlg', TrueFalseIndicator, False)

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

	@property
	def TxToPrfrm(self):
		return self._TxToPrfrm

	@TxToPrfrm.setter
	def TxToPrfrm(self, value):
		self._TxToPrfrm = value if value is not None else base_types.UninitialisedField(self, 'TxToPrfrm', TransactionToPerform7Choice, True)

	@TxToPrfrm.deleter
	def TxToPrfrm(self):
		del self._TxToPrfrm
		self._TxToPrfrm = base_types.UninitialisedField(self, 'TxToPrfrm', TransactionToPerform7Choice, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='RmvAllFlg', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SaleBtchId', type=TransactionIdentifier1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxToPrfrm', type=TransactionToPerform7Choice, min=0, max=None, mutex_group=None, array=True),
	))