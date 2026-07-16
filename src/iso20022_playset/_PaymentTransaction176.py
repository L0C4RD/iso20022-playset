# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActiveOrHistoricCurrencyAndAmount
from . import Case6
from . import DateAndDateTime2Choice
from . import ISODate
from . import Max35Text
from . import OriginalTransactionReference47
from . import PaymentCancellationReason6
from . import SupplementaryData1
from . import UUIDv4Identifier

class PaymentTransaction176(base_types._BaseFieldType):

	__slots__ = ["_Case", "_CxlId", "_CxlRsnInf", "_OrgnlEndToEndId", "_OrgnlInstdAmt", "_OrgnlInstrId", "_OrgnlReqdColltnDt", "_OrgnlReqdExctnDt", "_OrgnlTxRef", "_OrgnlUETR", "_SplmtryData"]
	@property
	def Case(self):
		return self._Case

	@Case.setter
	def Case(self, value):
		self._Case = value if value is not None else base_types.UninitialisedField(self, 'Case', Case6, False)

	@Case.deleter
	def Case(self):
		del self._Case
		self._Case = base_types.UninitialisedField(self, 'Case', Case6, False)

	@property
	def CxlId(self):
		return self._CxlId

	@CxlId.setter
	def CxlId(self, value):
		self._CxlId = value if value is not None else base_types.UninitialisedField(self, 'CxlId', Max35Text, False)

	@CxlId.deleter
	def CxlId(self):
		del self._CxlId
		self._CxlId = base_types.UninitialisedField(self, 'CxlId', Max35Text, False)

	@property
	def CxlRsnInf(self):
		return self._CxlRsnInf

	@CxlRsnInf.setter
	def CxlRsnInf(self, value):
		self._CxlRsnInf = value if value is not None else base_types.UninitialisedField(self, 'CxlRsnInf', PaymentCancellationReason6, True)

	@CxlRsnInf.deleter
	def CxlRsnInf(self):
		del self._CxlRsnInf
		self._CxlRsnInf = base_types.UninitialisedField(self, 'CxlRsnInf', PaymentCancellationReason6, True)

	@property
	def OrgnlEndToEndId(self):
		return self._OrgnlEndToEndId

	@OrgnlEndToEndId.setter
	def OrgnlEndToEndId(self, value):
		self._OrgnlEndToEndId = value if value is not None else base_types.UninitialisedField(self, 'OrgnlEndToEndId', Max35Text, False)

	@OrgnlEndToEndId.deleter
	def OrgnlEndToEndId(self):
		del self._OrgnlEndToEndId
		self._OrgnlEndToEndId = base_types.UninitialisedField(self, 'OrgnlEndToEndId', Max35Text, False)

	@property
	def OrgnlInstdAmt(self):
		return self._OrgnlInstdAmt

	@OrgnlInstdAmt.setter
	def OrgnlInstdAmt(self, value):
		self._OrgnlInstdAmt = value if value is not None else base_types.UninitialisedField(self, 'OrgnlInstdAmt', ActiveOrHistoricCurrencyAndAmount, False)

	@OrgnlInstdAmt.deleter
	def OrgnlInstdAmt(self):
		del self._OrgnlInstdAmt
		self._OrgnlInstdAmt = base_types.UninitialisedField(self, 'OrgnlInstdAmt', ActiveOrHistoricCurrencyAndAmount, False)

	@property
	def OrgnlInstrId(self):
		return self._OrgnlInstrId

	@OrgnlInstrId.setter
	def OrgnlInstrId(self, value):
		self._OrgnlInstrId = value if value is not None else base_types.UninitialisedField(self, 'OrgnlInstrId', Max35Text, False)

	@OrgnlInstrId.deleter
	def OrgnlInstrId(self):
		del self._OrgnlInstrId
		self._OrgnlInstrId = base_types.UninitialisedField(self, 'OrgnlInstrId', Max35Text, False)

	@property
	def OrgnlReqdColltnDt(self):
		return self._OrgnlReqdColltnDt

	@OrgnlReqdColltnDt.setter
	def OrgnlReqdColltnDt(self, value):
		self._OrgnlReqdColltnDt = value if value is not None else base_types.UninitialisedField(self, 'OrgnlReqdColltnDt', ISODate, False)

	@OrgnlReqdColltnDt.deleter
	def OrgnlReqdColltnDt(self):
		del self._OrgnlReqdColltnDt
		self._OrgnlReqdColltnDt = base_types.UninitialisedField(self, 'OrgnlReqdColltnDt', ISODate, False)

	@property
	def OrgnlReqdExctnDt(self):
		return self._OrgnlReqdExctnDt

	@OrgnlReqdExctnDt.setter
	def OrgnlReqdExctnDt(self, value):
		self._OrgnlReqdExctnDt = value if value is not None else base_types.UninitialisedField(self, 'OrgnlReqdExctnDt', DateAndDateTime2Choice, False)

	@OrgnlReqdExctnDt.deleter
	def OrgnlReqdExctnDt(self):
		del self._OrgnlReqdExctnDt
		self._OrgnlReqdExctnDt = base_types.UninitialisedField(self, 'OrgnlReqdExctnDt', DateAndDateTime2Choice, False)

	@property
	def OrgnlTxRef(self):
		return self._OrgnlTxRef

	@OrgnlTxRef.setter
	def OrgnlTxRef(self, value):
		self._OrgnlTxRef = value if value is not None else base_types.UninitialisedField(self, 'OrgnlTxRef', OriginalTransactionReference47, False)

	@OrgnlTxRef.deleter
	def OrgnlTxRef(self):
		del self._OrgnlTxRef
		self._OrgnlTxRef = base_types.UninitialisedField(self, 'OrgnlTxRef', OriginalTransactionReference47, False)

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

	@property
	def SplmtryData(self):
		return self._SplmtryData

	@SplmtryData.setter
	def SplmtryData(self, value):
		self._SplmtryData = value if value is not None else base_types.UninitialisedField(self, 'SplmtryData', SupplementaryData1, True)

	@SplmtryData.deleter
	def SplmtryData(self):
		del self._SplmtryData
		self._SplmtryData = base_types.UninitialisedField(self, 'SplmtryData', SupplementaryData1, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Case', type=Case6, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CxlId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CxlRsnInf', type=PaymentCancellationReason6, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='OrgnlEndToEndId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlInstdAmt', type=ActiveOrHistoricCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlInstrId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlReqdColltnDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlReqdExctnDt', type=DateAndDateTime2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlTxRef', type=OriginalTransactionReference47, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlUETR', type=UUIDv4Identifier, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
	))