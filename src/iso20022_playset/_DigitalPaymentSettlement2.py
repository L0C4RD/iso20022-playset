# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CashSettlementSystemPlace1Choice
from . import Max30DecimalNumber
from . import SecurityIdentification19

class DigitalPaymentSettlement2(base_types._BaseFieldType):

	__slots__ = ["_CshSttlmSysPlc", "_ElctrncMnyTknSttlmQty", "_FinInstrmId"]
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
	def ElctrncMnyTknSttlmQty(self):
		return self._ElctrncMnyTknSttlmQty

	@ElctrncMnyTknSttlmQty.setter
	def ElctrncMnyTknSttlmQty(self, value):
		self._ElctrncMnyTknSttlmQty = value if value is not None else base_types.UninitialisedField(self, 'ElctrncMnyTknSttlmQty', Max30DecimalNumber, False)

	@ElctrncMnyTknSttlmQty.deleter
	def ElctrncMnyTknSttlmQty(self):
		del self._ElctrncMnyTknSttlmQty
		self._ElctrncMnyTknSttlmQty = base_types.UninitialisedField(self, 'ElctrncMnyTknSttlmQty', Max30DecimalNumber, False)

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

	_field_defs = frozenset((
		base_types.FieldEntry(name='CshSttlmSysPlc', type=CashSettlementSystemPlace1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ElctrncMnyTknSttlmQty', type=Max30DecimalNumber, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FinInstrmId', type=SecurityIdentification19, min=1, max=1, mutex_group=None, array=False),
	))