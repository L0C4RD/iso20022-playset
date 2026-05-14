# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._CashSettlementSystemPlace1Choice import CashSettlementSystemPlace1Choice
from ._Max30DecimalNumber import Max30DecimalNumber
from ._SecurityIdentification19 import SecurityIdentification19

class DigitalPaymentSettlement2(base_types._BaseFieldType):

	__slots__ = ["_CshSttlmSysPlc", "_ElctrncMnyTknSttlmQty", "_FinInstrmId"]
	@property
	def CshSttlmSysPlc(self):
		return self._CshSttlmSysPlc

	@CshSttlmSysPlc.setter
	def CshSttlmSysPlc(self, value):
		self._CshSttlmSysPlc = value if type(value) != base_types.auto else self.make_default("CshSttlmSysPlc")

	@CshSttlmSysPlc.deleter
	def CshSttlmSysPlc(self):
		del self._CshSttlmSysPlc
		self._CshSttlmSysPlc = None

	@property
	def ElctrncMnyTknSttlmQty(self):
		return self._ElctrncMnyTknSttlmQty

	@ElctrncMnyTknSttlmQty.setter
	def ElctrncMnyTknSttlmQty(self, value):
		self._ElctrncMnyTknSttlmQty = value if type(value) != base_types.auto else self.make_default("ElctrncMnyTknSttlmQty")

	@ElctrncMnyTknSttlmQty.deleter
	def ElctrncMnyTknSttlmQty(self):
		del self._ElctrncMnyTknSttlmQty
		self._ElctrncMnyTknSttlmQty = None

	@property
	def FinInstrmId(self):
		return self._FinInstrmId

	@FinInstrmId.setter
	def FinInstrmId(self, value):
		self._FinInstrmId = value if type(value) != base_types.auto else self.make_default("FinInstrmId")

	@FinInstrmId.deleter
	def FinInstrmId(self):
		del self._FinInstrmId
		self._FinInstrmId = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='CshSttlmSysPlc', type=CashSettlementSystemPlace1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ElctrncMnyTknSttlmQty', type=Max30DecimalNumber, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FinInstrmId', type=SecurityIdentification19, min=1, max=1, mutex_group=None, array=False),
	))