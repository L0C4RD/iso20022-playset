# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Amount2Choice
from . import CashSubBalanceTypeAndQuantityBreakdown3
from . import DateAndDateTime2Choice
from . import GenericIdentification37
from . import Max350Text

class IntraBalance6(base_types._BaseFieldType):

	__slots__ = ["_BalFr", "_BalTo", "_CshSubBalId", "_InstrPrcgAddtlDtls", "_PrevslySttldAmt", "_RmngSttlmAmt", "_SttldAmt", "_SttlmDt"]
	@property
	def BalFr(self):
		return self._BalFr

	@BalFr.setter
	def BalFr(self, value):
		self._BalFr = value if value is not None else base_types.UninitialisedField(self, 'BalFr', CashSubBalanceTypeAndQuantityBreakdown3, False)

	@BalFr.deleter
	def BalFr(self):
		del self._BalFr
		self._BalFr = base_types.UninitialisedField(self, 'BalFr', CashSubBalanceTypeAndQuantityBreakdown3, False)

	@property
	def BalTo(self):
		return self._BalTo

	@BalTo.setter
	def BalTo(self, value):
		self._BalTo = value if value is not None else base_types.UninitialisedField(self, 'BalTo', CashSubBalanceTypeAndQuantityBreakdown3, False)

	@BalTo.deleter
	def BalTo(self):
		del self._BalTo
		self._BalTo = base_types.UninitialisedField(self, 'BalTo', CashSubBalanceTypeAndQuantityBreakdown3, False)

	@property
	def CshSubBalId(self):
		return self._CshSubBalId

	@CshSubBalId.setter
	def CshSubBalId(self, value):
		self._CshSubBalId = value if value is not None else base_types.UninitialisedField(self, 'CshSubBalId', GenericIdentification37, False)

	@CshSubBalId.deleter
	def CshSubBalId(self):
		del self._CshSubBalId
		self._CshSubBalId = base_types.UninitialisedField(self, 'CshSubBalId', GenericIdentification37, False)

	@property
	def InstrPrcgAddtlDtls(self):
		return self._InstrPrcgAddtlDtls

	@InstrPrcgAddtlDtls.setter
	def InstrPrcgAddtlDtls(self, value):
		self._InstrPrcgAddtlDtls = value if value is not None else base_types.UninitialisedField(self, 'InstrPrcgAddtlDtls', Max350Text, False)

	@InstrPrcgAddtlDtls.deleter
	def InstrPrcgAddtlDtls(self):
		del self._InstrPrcgAddtlDtls
		self._InstrPrcgAddtlDtls = base_types.UninitialisedField(self, 'InstrPrcgAddtlDtls', Max350Text, False)

	@property
	def PrevslySttldAmt(self):
		return self._PrevslySttldAmt

	@PrevslySttldAmt.setter
	def PrevslySttldAmt(self, value):
		self._PrevslySttldAmt = value if value is not None else base_types.UninitialisedField(self, 'PrevslySttldAmt', Amount2Choice, False)

	@PrevslySttldAmt.deleter
	def PrevslySttldAmt(self):
		del self._PrevslySttldAmt
		self._PrevslySttldAmt = base_types.UninitialisedField(self, 'PrevslySttldAmt', Amount2Choice, False)

	@property
	def RmngSttlmAmt(self):
		return self._RmngSttlmAmt

	@RmngSttlmAmt.setter
	def RmngSttlmAmt(self, value):
		self._RmngSttlmAmt = value if value is not None else base_types.UninitialisedField(self, 'RmngSttlmAmt', Amount2Choice, False)

	@RmngSttlmAmt.deleter
	def RmngSttlmAmt(self):
		del self._RmngSttlmAmt
		self._RmngSttlmAmt = base_types.UninitialisedField(self, 'RmngSttlmAmt', Amount2Choice, False)

	@property
	def SttldAmt(self):
		return self._SttldAmt

	@SttldAmt.setter
	def SttldAmt(self, value):
		self._SttldAmt = value if value is not None else base_types.UninitialisedField(self, 'SttldAmt', Amount2Choice, False)

	@SttldAmt.deleter
	def SttldAmt(self):
		del self._SttldAmt
		self._SttldAmt = base_types.UninitialisedField(self, 'SttldAmt', Amount2Choice, False)

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

	_field_defs = frozenset((
		base_types.FieldEntry(name='BalFr', type=CashSubBalanceTypeAndQuantityBreakdown3, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BalTo', type=CashSubBalanceTypeAndQuantityBreakdown3, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CshSubBalId', type=GenericIdentification37, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InstrPrcgAddtlDtls', type=Max350Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrevslySttldAmt', type=Amount2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RmngSttlmAmt', type=Amount2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SttldAmt', type=Amount2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SttlmDt', type=DateAndDateTime2Choice, min=1, max=1, mutex_group=None, array=False),
	))