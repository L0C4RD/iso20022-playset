# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActiveOrHistoricCurrencyAndAmount
from . import CancellationIndividualStatus1Code
from . import CancellationStatusReason5
from . import Case6
from . import DateAndDateTime2Choice
from . import ISODate
from . import Max35Text
from . import OriginalTransactionReference47
from . import UUIDv4Identifier

class PaymentTransaction175(base_types._BaseFieldType):

	__slots__ = ["_CxlStsId", "_CxlStsRsnInf", "_OrgnlEndToEndId", "_OrgnlInstdAmt", "_OrgnlInstrId", "_OrgnlReqdColltnDt", "_OrgnlReqdExctnDt", "_OrgnlTxRef", "_RslvdCase", "_TxCxlSts", "_UETR"]
	@property
	def CxlStsId(self):
		return self._CxlStsId

	@CxlStsId.setter
	def CxlStsId(self, value):
		self._CxlStsId = value if value is not None else base_types.UninitialisedField(self, 'CxlStsId', Max35Text, False)

	@CxlStsId.deleter
	def CxlStsId(self):
		del self._CxlStsId
		self._CxlStsId = base_types.UninitialisedField(self, 'CxlStsId', Max35Text, False)

	@property
	def CxlStsRsnInf(self):
		return self._CxlStsRsnInf

	@CxlStsRsnInf.setter
	def CxlStsRsnInf(self, value):
		self._CxlStsRsnInf = value if value is not None else base_types.UninitialisedField(self, 'CxlStsRsnInf', CancellationStatusReason5, True)

	@CxlStsRsnInf.deleter
	def CxlStsRsnInf(self):
		del self._CxlStsRsnInf
		self._CxlStsRsnInf = base_types.UninitialisedField(self, 'CxlStsRsnInf', CancellationStatusReason5, True)

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
	def RslvdCase(self):
		return self._RslvdCase

	@RslvdCase.setter
	def RslvdCase(self, value):
		self._RslvdCase = value if value is not None else base_types.UninitialisedField(self, 'RslvdCase', Case6, False)

	@RslvdCase.deleter
	def RslvdCase(self):
		del self._RslvdCase
		self._RslvdCase = base_types.UninitialisedField(self, 'RslvdCase', Case6, False)

	@property
	def TxCxlSts(self):
		return self._TxCxlSts

	@TxCxlSts.setter
	def TxCxlSts(self, value):
		self._TxCxlSts = value if value is not None else base_types.UninitialisedField(self, 'TxCxlSts', CancellationIndividualStatus1Code, False)

	@TxCxlSts.deleter
	def TxCxlSts(self):
		del self._TxCxlSts
		self._TxCxlSts = base_types.UninitialisedField(self, 'TxCxlSts', CancellationIndividualStatus1Code, False)

	@property
	def UETR(self):
		return self._UETR

	@UETR.setter
	def UETR(self, value):
		self._UETR = value if value is not None else base_types.UninitialisedField(self, 'UETR', UUIDv4Identifier, False)

	@UETR.deleter
	def UETR(self):
		del self._UETR
		self._UETR = base_types.UninitialisedField(self, 'UETR', UUIDv4Identifier, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='CxlStsId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CxlStsRsnInf', type=CancellationStatusReason5, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='OrgnlEndToEndId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlInstdAmt', type=ActiveOrHistoricCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlInstrId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlReqdColltnDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlReqdExctnDt', type=DateAndDateTime2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlTxRef', type=OriginalTransactionReference47, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RslvdCase', type=Case6, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxCxlSts', type=CancellationIndividualStatus1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UETR', type=UUIDv4Identifier, min=0, max=1, mutex_group=None, array=False),
	))