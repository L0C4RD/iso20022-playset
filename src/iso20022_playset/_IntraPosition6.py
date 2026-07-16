# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import DateAndDateTime2Choice
from . import FinancialInstrumentQuantity1Choice
from . import GenericIdentification37
from . import PriorityNumeric4Choice
from . import SecuritiesSubBalanceTypeAndQuantityBreakdown3
from . import SecurityIdentification19

class IntraPosition6(base_types._BaseFieldType):

	__slots__ = ["_BalFr", "_BalTo", "_FinInstrmId", "_Prty", "_SctiesSubBalId", "_SttlmDt", "_SttlmQty"]
	@property
	def BalFr(self):
		return self._BalFr

	@BalFr.setter
	def BalFr(self, value):
		self._BalFr = value if value is not None else base_types.UninitialisedField(self, 'BalFr', SecuritiesSubBalanceTypeAndQuantityBreakdown3, False)

	@BalFr.deleter
	def BalFr(self):
		del self._BalFr
		self._BalFr = base_types.UninitialisedField(self, 'BalFr', SecuritiesSubBalanceTypeAndQuantityBreakdown3, False)

	@property
	def BalTo(self):
		return self._BalTo

	@BalTo.setter
	def BalTo(self, value):
		self._BalTo = value if value is not None else base_types.UninitialisedField(self, 'BalTo', SecuritiesSubBalanceTypeAndQuantityBreakdown3, False)

	@BalTo.deleter
	def BalTo(self):
		del self._BalTo
		self._BalTo = base_types.UninitialisedField(self, 'BalTo', SecuritiesSubBalanceTypeAndQuantityBreakdown3, False)

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
	def Prty(self):
		return self._Prty

	@Prty.setter
	def Prty(self, value):
		self._Prty = value if value is not None else base_types.UninitialisedField(self, 'Prty', PriorityNumeric4Choice, False)

	@Prty.deleter
	def Prty(self):
		del self._Prty
		self._Prty = base_types.UninitialisedField(self, 'Prty', PriorityNumeric4Choice, False)

	@property
	def SctiesSubBalId(self):
		return self._SctiesSubBalId

	@SctiesSubBalId.setter
	def SctiesSubBalId(self, value):
		self._SctiesSubBalId = value if value is not None else base_types.UninitialisedField(self, 'SctiesSubBalId', GenericIdentification37, False)

	@SctiesSubBalId.deleter
	def SctiesSubBalId(self):
		del self._SctiesSubBalId
		self._SctiesSubBalId = base_types.UninitialisedField(self, 'SctiesSubBalId', GenericIdentification37, False)

	@property
	def SttlmDt(self):
		return self._SttlmDt

	@SttlmDt.setter
	def SttlmDt(self, value):
		self._SttlmDt = value if value is not None else base_types.UninitialisedField(self, 'SttlmDt', DateAndDateTime2Choice, False)

	@SttlmDt.deleter
	def SttlmDt(self):
		del self._SttlmDt
		self._SttlmDt = base_types.UninitialisedField(self, 'SttlmDt', DateAndDateTime2Choice, False)

	@property
	def SttlmQty(self):
		return self._SttlmQty

	@SttlmQty.setter
	def SttlmQty(self, value):
		self._SttlmQty = value if value is not None else base_types.UninitialisedField(self, 'SttlmQty', FinancialInstrumentQuantity1Choice, False)

	@SttlmQty.deleter
	def SttlmQty(self):
		del self._SttlmQty
		self._SttlmQty = base_types.UninitialisedField(self, 'SttlmQty', FinancialInstrumentQuantity1Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='BalFr', type=SecuritiesSubBalanceTypeAndQuantityBreakdown3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BalTo', type=SecuritiesSubBalanceTypeAndQuantityBreakdown3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FinInstrmId', type=SecurityIdentification19, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Prty', type=PriorityNumeric4Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctiesSubBalId', type=GenericIdentification37, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SttlmDt', type=DateAndDateTime2Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SttlmQty', type=FinancialInstrumentQuantity1Choice, min=1, max=1, mutex_group=None, array=False),
	))