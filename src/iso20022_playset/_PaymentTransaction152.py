# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActiveOrHistoricCurrencyAndAmount
from . import CancellationIndividualStatus1Code
from . import CancellationStatusReason5
from . import Case6
from . import ISODate
from . import Max35Text
from . import OriginalGroupInformation29
from . import OriginalTransactionReference42
from . import Party50Choice
from . import ResolutionData5
from . import UUIDv4Identifier

class PaymentTransaction152(base_types._BaseFieldType):

	__slots__ = ["_Assgne", "_Assgnr", "_CxlStsId", "_CxlStsRsnInf", "_OrgnlClrSysRef", "_OrgnlEndToEndId", "_OrgnlGrpInf", "_OrgnlInstrId", "_OrgnlIntrBkSttlmAmt", "_OrgnlIntrBkSttlmDt", "_OrgnlTxId", "_OrgnlTxRef", "_OrgnlUETR", "_RsltnRltdInf", "_RslvdCase", "_TxCxlSts"]
	@property
	def Assgne(self):
		return self._Assgne

	@Assgne.setter
	def Assgne(self, value):
		self._Assgne = value if value is not None else base_types.UninitialisedField(self, 'Assgne', Party50Choice, False)

	@Assgne.deleter
	def Assgne(self):
		del self._Assgne
		self._Assgne = base_types.UninitialisedField(self, 'Assgne', Party50Choice, False)

	@property
	def Assgnr(self):
		return self._Assgnr

	@Assgnr.setter
	def Assgnr(self, value):
		self._Assgnr = value if value is not None else base_types.UninitialisedField(self, 'Assgnr', Party50Choice, False)

	@Assgnr.deleter
	def Assgnr(self):
		del self._Assgnr
		self._Assgnr = base_types.UninitialisedField(self, 'Assgnr', Party50Choice, False)

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
	def OrgnlClrSysRef(self):
		return self._OrgnlClrSysRef

	@OrgnlClrSysRef.setter
	def OrgnlClrSysRef(self, value):
		self._OrgnlClrSysRef = value if value is not None else base_types.UninitialisedField(self, 'OrgnlClrSysRef', Max35Text, False)

	@OrgnlClrSysRef.deleter
	def OrgnlClrSysRef(self):
		del self._OrgnlClrSysRef
		self._OrgnlClrSysRef = base_types.UninitialisedField(self, 'OrgnlClrSysRef', Max35Text, False)

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
	def OrgnlGrpInf(self):
		return self._OrgnlGrpInf

	@OrgnlGrpInf.setter
	def OrgnlGrpInf(self, value):
		self._OrgnlGrpInf = value if value is not None else base_types.UninitialisedField(self, 'OrgnlGrpInf', OriginalGroupInformation29, False)

	@OrgnlGrpInf.deleter
	def OrgnlGrpInf(self):
		del self._OrgnlGrpInf
		self._OrgnlGrpInf = base_types.UninitialisedField(self, 'OrgnlGrpInf', OriginalGroupInformation29, False)

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
	def OrgnlIntrBkSttlmAmt(self):
		return self._OrgnlIntrBkSttlmAmt

	@OrgnlIntrBkSttlmAmt.setter
	def OrgnlIntrBkSttlmAmt(self, value):
		self._OrgnlIntrBkSttlmAmt = value if value is not None else base_types.UninitialisedField(self, 'OrgnlIntrBkSttlmAmt', ActiveOrHistoricCurrencyAndAmount, False)

	@OrgnlIntrBkSttlmAmt.deleter
	def OrgnlIntrBkSttlmAmt(self):
		del self._OrgnlIntrBkSttlmAmt
		self._OrgnlIntrBkSttlmAmt = base_types.UninitialisedField(self, 'OrgnlIntrBkSttlmAmt', ActiveOrHistoricCurrencyAndAmount, False)

	@property
	def OrgnlIntrBkSttlmDt(self):
		return self._OrgnlIntrBkSttlmDt

	@OrgnlIntrBkSttlmDt.setter
	def OrgnlIntrBkSttlmDt(self, value):
		self._OrgnlIntrBkSttlmDt = value if value is not None else base_types.UninitialisedField(self, 'OrgnlIntrBkSttlmDt', ISODate, False)

	@OrgnlIntrBkSttlmDt.deleter
	def OrgnlIntrBkSttlmDt(self):
		del self._OrgnlIntrBkSttlmDt
		self._OrgnlIntrBkSttlmDt = base_types.UninitialisedField(self, 'OrgnlIntrBkSttlmDt', ISODate, False)

	@property
	def OrgnlTxId(self):
		return self._OrgnlTxId

	@OrgnlTxId.setter
	def OrgnlTxId(self, value):
		self._OrgnlTxId = value if value is not None else base_types.UninitialisedField(self, 'OrgnlTxId', Max35Text, False)

	@OrgnlTxId.deleter
	def OrgnlTxId(self):
		del self._OrgnlTxId
		self._OrgnlTxId = base_types.UninitialisedField(self, 'OrgnlTxId', Max35Text, False)

	@property
	def OrgnlTxRef(self):
		return self._OrgnlTxRef

	@OrgnlTxRef.setter
	def OrgnlTxRef(self, value):
		self._OrgnlTxRef = value if value is not None else base_types.UninitialisedField(self, 'OrgnlTxRef', OriginalTransactionReference42, False)

	@OrgnlTxRef.deleter
	def OrgnlTxRef(self):
		del self._OrgnlTxRef
		self._OrgnlTxRef = base_types.UninitialisedField(self, 'OrgnlTxRef', OriginalTransactionReference42, False)

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
	def RsltnRltdInf(self):
		return self._RsltnRltdInf

	@RsltnRltdInf.setter
	def RsltnRltdInf(self, value):
		self._RsltnRltdInf = value if value is not None else base_types.UninitialisedField(self, 'RsltnRltdInf', ResolutionData5, False)

	@RsltnRltdInf.deleter
	def RsltnRltdInf(self):
		del self._RsltnRltdInf
		self._RsltnRltdInf = base_types.UninitialisedField(self, 'RsltnRltdInf', ResolutionData5, False)

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

	_field_defs = frozenset((
		base_types.FieldEntry(name='Assgne', type=Party50Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Assgnr', type=Party50Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CxlStsId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CxlStsRsnInf', type=CancellationStatusReason5, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='OrgnlClrSysRef', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlEndToEndId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlGrpInf', type=OriginalGroupInformation29, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlInstrId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlIntrBkSttlmAmt', type=ActiveOrHistoricCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlIntrBkSttlmDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlTxId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlTxRef', type=OriginalTransactionReference42, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlUETR', type=UUIDv4Identifier, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RsltnRltdInf', type=ResolutionData5, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RslvdCase', type=Case6, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxCxlSts', type=CancellationIndividualStatus1Code, min=0, max=1, mutex_group=None, array=False),
	))