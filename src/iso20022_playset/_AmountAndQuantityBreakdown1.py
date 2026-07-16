# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AmountAndDirection5
from . import FinancialInstrumentQuantity1Choice
from . import GenericIdentification30
from . import GenericIdentification37

class AmountAndQuantityBreakdown1(base_types._BaseFieldType):

	__slots__ = ["_CshSubBalTp", "_LotAmt", "_LotNb", "_LotQty"]
	@property
	def CshSubBalTp(self):
		return self._CshSubBalTp

	@CshSubBalTp.setter
	def CshSubBalTp(self, value):
		self._CshSubBalTp = value if value is not None else base_types.UninitialisedField(self, 'CshSubBalTp', GenericIdentification30, False)

	@CshSubBalTp.deleter
	def CshSubBalTp(self):
		del self._CshSubBalTp
		self._CshSubBalTp = base_types.UninitialisedField(self, 'CshSubBalTp', GenericIdentification30, False)

	@property
	def LotAmt(self):
		return self._LotAmt

	@LotAmt.setter
	def LotAmt(self, value):
		self._LotAmt = value if value is not None else base_types.UninitialisedField(self, 'LotAmt', AmountAndDirection5, False)

	@LotAmt.deleter
	def LotAmt(self):
		del self._LotAmt
		self._LotAmt = base_types.UninitialisedField(self, 'LotAmt', AmountAndDirection5, False)

	@property
	def LotNb(self):
		return self._LotNb

	@LotNb.setter
	def LotNb(self, value):
		self._LotNb = value if value is not None else base_types.UninitialisedField(self, 'LotNb', GenericIdentification37, False)

	@LotNb.deleter
	def LotNb(self):
		del self._LotNb
		self._LotNb = base_types.UninitialisedField(self, 'LotNb', GenericIdentification37, False)

	@property
	def LotQty(self):
		return self._LotQty

	@LotQty.setter
	def LotQty(self, value):
		self._LotQty = value if value is not None else base_types.UninitialisedField(self, 'LotQty', FinancialInstrumentQuantity1Choice, False)

	@LotQty.deleter
	def LotQty(self):
		del self._LotQty
		self._LotQty = base_types.UninitialisedField(self, 'LotQty', FinancialInstrumentQuantity1Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='CshSubBalTp', type=GenericIdentification30, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LotAmt', type=AmountAndDirection5, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LotNb', type=GenericIdentification37, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LotQty', type=FinancialInstrumentQuantity1Choice, min=0, max=1, mutex_group=None, array=False),
	))