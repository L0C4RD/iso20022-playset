# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActiveOrHistoricCurrencyAndAmount
from . import GenericIdentification178
from . import Period4Choice

class CollateralTransactionAmountBreakdown2(base_types._BaseFieldType):

	__slots__ = ["_LotNb", "_Prd", "_TxAmt"]
	@property
	def LotNb(self):
		return self._LotNb

	@LotNb.setter
	def LotNb(self, value):
		self._LotNb = value if value is not None else base_types.UninitialisedField(self, 'LotNb', GenericIdentification178, False)

	@LotNb.deleter
	def LotNb(self):
		del self._LotNb
		self._LotNb = base_types.UninitialisedField(self, 'LotNb', GenericIdentification178, False)

	@property
	def Prd(self):
		return self._Prd

	@Prd.setter
	def Prd(self, value):
		self._Prd = value if value is not None else base_types.UninitialisedField(self, 'Prd', Period4Choice, False)

	@Prd.deleter
	def Prd(self):
		del self._Prd
		self._Prd = base_types.UninitialisedField(self, 'Prd', Period4Choice, False)

	@property
	def TxAmt(self):
		return self._TxAmt

	@TxAmt.setter
	def TxAmt(self, value):
		self._TxAmt = value if value is not None else base_types.UninitialisedField(self, 'TxAmt', ActiveOrHistoricCurrencyAndAmount, False)

	@TxAmt.deleter
	def TxAmt(self):
		del self._TxAmt
		self._TxAmt = base_types.UninitialisedField(self, 'TxAmt', ActiveOrHistoricCurrencyAndAmount, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='LotNb', type=GenericIdentification178, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Prd', type=Period4Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxAmt', type=ActiveOrHistoricCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
	))