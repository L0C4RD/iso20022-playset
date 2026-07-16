# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActiveOrHistoricCurrencyAndAmount
from . import CashAccount40
from . import DateAndDateTime2Choice
from . import Max35Text
from . import OriginalGroupInformation33
from . import UUIDv4Identifier

class UnderlyingStatementEntry11(base_types._BaseFieldType):

	__slots__ = ["_OrgnlAcct", "_OrgnlGrpInf", "_OrgnlNtryAmt", "_OrgnlNtryRef", "_OrgnlNtryValDt", "_OrgnlStmtId", "_OrgnlUETR"]
	@property
	def OrgnlAcct(self):
		return self._OrgnlAcct

	@OrgnlAcct.setter
	def OrgnlAcct(self, value):
		self._OrgnlAcct = value if value is not None else base_types.UninitialisedField(self, 'OrgnlAcct', CashAccount40, False)

	@OrgnlAcct.deleter
	def OrgnlAcct(self):
		del self._OrgnlAcct
		self._OrgnlAcct = base_types.UninitialisedField(self, 'OrgnlAcct', CashAccount40, False)

	@property
	def OrgnlGrpInf(self):
		return self._OrgnlGrpInf

	@OrgnlGrpInf.setter
	def OrgnlGrpInf(self, value):
		self._OrgnlGrpInf = value if value is not None else base_types.UninitialisedField(self, 'OrgnlGrpInf', OriginalGroupInformation33, False)

	@OrgnlGrpInf.deleter
	def OrgnlGrpInf(self):
		del self._OrgnlGrpInf
		self._OrgnlGrpInf = base_types.UninitialisedField(self, 'OrgnlGrpInf', OriginalGroupInformation33, False)

	@property
	def OrgnlNtryAmt(self):
		return self._OrgnlNtryAmt

	@OrgnlNtryAmt.setter
	def OrgnlNtryAmt(self, value):
		self._OrgnlNtryAmt = value if value is not None else base_types.UninitialisedField(self, 'OrgnlNtryAmt', ActiveOrHistoricCurrencyAndAmount, False)

	@OrgnlNtryAmt.deleter
	def OrgnlNtryAmt(self):
		del self._OrgnlNtryAmt
		self._OrgnlNtryAmt = base_types.UninitialisedField(self, 'OrgnlNtryAmt', ActiveOrHistoricCurrencyAndAmount, False)

	@property
	def OrgnlNtryRef(self):
		return self._OrgnlNtryRef

	@OrgnlNtryRef.setter
	def OrgnlNtryRef(self, value):
		self._OrgnlNtryRef = value if value is not None else base_types.UninitialisedField(self, 'OrgnlNtryRef', Max35Text, False)

	@OrgnlNtryRef.deleter
	def OrgnlNtryRef(self):
		del self._OrgnlNtryRef
		self._OrgnlNtryRef = base_types.UninitialisedField(self, 'OrgnlNtryRef', Max35Text, False)

	@property
	def OrgnlNtryValDt(self):
		return self._OrgnlNtryValDt

	@OrgnlNtryValDt.setter
	def OrgnlNtryValDt(self, value):
		self._OrgnlNtryValDt = value if value is not None else base_types.UninitialisedField(self, 'OrgnlNtryValDt', DateAndDateTime2Choice, False)

	@OrgnlNtryValDt.deleter
	def OrgnlNtryValDt(self):
		del self._OrgnlNtryValDt
		self._OrgnlNtryValDt = base_types.UninitialisedField(self, 'OrgnlNtryValDt', DateAndDateTime2Choice, False)

	@property
	def OrgnlStmtId(self):
		return self._OrgnlStmtId

	@OrgnlStmtId.setter
	def OrgnlStmtId(self, value):
		self._OrgnlStmtId = value if value is not None else base_types.UninitialisedField(self, 'OrgnlStmtId', Max35Text, False)

	@OrgnlStmtId.deleter
	def OrgnlStmtId(self):
		del self._OrgnlStmtId
		self._OrgnlStmtId = base_types.UninitialisedField(self, 'OrgnlStmtId', Max35Text, False)

	@property
	def OrgnlUETR(self):
		return self._OrgnlUETR

	@OrgnlUETR.setter
	def OrgnlUETR(self, value):
		self._OrgnlUETR = value if value is not None else base_types.UninitialisedField(self, 'OrgnlUETR', UUIDv4Identifier, False)

	@OrgnlUETR.deleter
	def OrgnlUETR(self):
		del self._OrgnlUETR
		self._OrgnlUETR = base_types.UninitialisedField(self, 'OrgnlUETR', UUIDv4Identifier, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='OrgnlAcct', type=CashAccount40, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlGrpInf', type=OriginalGroupInformation33, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlNtryAmt', type=ActiveOrHistoricCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlNtryRef', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlNtryValDt', type=DateAndDateTime2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlStmtId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlUETR', type=UUIDv4Identifier, min=0, max=1, mutex_group=None, array=False),
	))