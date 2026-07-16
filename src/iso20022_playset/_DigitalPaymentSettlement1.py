# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CashSettlementSystemPlace1Choice
from . import Quantity83Choice
from . import SecurityIdentification19

class DigitalPaymentSettlement1(base_types._BaseFieldType):

	__slots__ = ["_CshSttlmSysPlc", "_FinInstrmId", "_Qty"]
	@property
	def CshSttlmSysPlc(self):
		return self._CshSttlmSysPlc

	@CshSttlmSysPlc.setter
	def CshSttlmSysPlc(self, value):
		self._CshSttlmSysPlc = value if value is not None else base_types.UninitialisedField(self, 'CshSttlmSysPlc', CashSettlementSystemPlace1Choice, False)

	@CshSttlmSysPlc.deleter
	def CshSttlmSysPlc(self):
		del self._CshSttlmSysPlc
		self._CshSttlmSysPlc = base_types.UninitialisedField(self, 'CshSttlmSysPlc', CashSettlementSystemPlace1Choice, False)

	@property
	def FinInstrmId(self):
		return self._FinInstrmId

	@FinInstrmId.setter
	def FinInstrmId(self, value):
		self._FinInstrmId = value if value is not None else base_types.UninitialisedField(self, 'FinInstrmId', SecurityIdentification19, False)

	@FinInstrmId.deleter
	def FinInstrmId(self):
		del self._FinInstrmId
		self._FinInstrmId = base_types.UninitialisedField(self, 'FinInstrmId', SecurityIdentification19, False)

	@property
	def Qty(self):
		return self._Qty

	@Qty.setter
	def Qty(self, value):
		self._Qty = value if value is not None else base_types.UninitialisedField(self, 'Qty', Quantity83Choice, False)

	@Qty.deleter
	def Qty(self):
		del self._Qty
		self._Qty = base_types.UninitialisedField(self, 'Qty', Quantity83Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='CshSttlmSysPlc', type=CashSettlementSystemPlace1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FinInstrmId', type=SecurityIdentification19, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Qty', type=Quantity83Choice, min=1, max=1, mutex_group=None, array=False),
	))