from . import base_types
from ._ActiveOrHistoricCurrencyAndAmount import ActiveOrHistoricCurrencyAndAmount
from ._CancellationIndividualStatus1Code import CancellationIndividualStatus1Code
from ._CancellationStatusReason5 import CancellationStatusReason5
from ._Case6 import Case6
from ._ISODate import ISODate
from ._Max35Text import Max35Text
from ._OriginalGroupInformation33 import OriginalGroupInformation33
from ._OriginalTransactionReference47 import OriginalTransactionReference47
from ._Party50Choice import Party50Choice
from ._ResolutionData5 import ResolutionData5
from ._UUIDv4Identifier import UUIDv4Identifier

class PaymentTransaction170(base_types._BaseFieldType):

	__slots__ = ["_Assgne", "_Assgnr", "_CxlStsId", "_CxlStsRsnInf", "_OrgnlClrSysRef", "_OrgnlEndToEndId", "_OrgnlGrpInf", "_OrgnlInstrId", "_OrgnlIntrBkSttlmAmt", "_OrgnlIntrBkSttlmDt", "_OrgnlTxId", "_OrgnlTxRef", "_OrgnlUETR", "_RsltnRltdInf", "_RslvdCase", "_TxCxlSts"]
	@property
	def Assgne(self):
		return self._Assgne

	@Assgne.setter
	def Assgne(self, value):
		self._Assgne = value if type(value) != base_types.auto else self.make_default("Assgne")

	@Assgne.deleter
	def Assgne(self):
		del self._Assgne
		self._Assgne = None

	@property
	def Assgnr(self):
		return self._Assgnr

	@Assgnr.setter
	def Assgnr(self, value):
		self._Assgnr = value if type(value) != base_types.auto else self.make_default("Assgnr")

	@Assgnr.deleter
	def Assgnr(self):
		del self._Assgnr
		self._Assgnr = None

	@property
	def CxlStsId(self):
		return self._CxlStsId

	@CxlStsId.setter
	def CxlStsId(self, value):
		self._CxlStsId = value if type(value) != base_types.auto else self.make_default("CxlStsId")

	@CxlStsId.deleter
	def CxlStsId(self):
		del self._CxlStsId
		self._CxlStsId = None

	@property
	def CxlStsRsnInf(self):
		return self._CxlStsRsnInf

	@CxlStsRsnInf.setter
	def CxlStsRsnInf(self, value):
		self._CxlStsRsnInf = value if type(value) != base_types.auto else self.make_default("CxlStsRsnInf")

	@CxlStsRsnInf.deleter
	def CxlStsRsnInf(self):
		del self._CxlStsRsnInf
		self._CxlStsRsnInf = None

	@property
	def OrgnlClrSysRef(self):
		return self._OrgnlClrSysRef

	@OrgnlClrSysRef.setter
	def OrgnlClrSysRef(self, value):
		self._OrgnlClrSysRef = value if type(value) != base_types.auto else self.make_default("OrgnlClrSysRef")

	@OrgnlClrSysRef.deleter
	def OrgnlClrSysRef(self):
		del self._OrgnlClrSysRef
		self._OrgnlClrSysRef = None

	@property
	def OrgnlEndToEndId(self):
		return self._OrgnlEndToEndId

	@OrgnlEndToEndId.setter
	def OrgnlEndToEndId(self, value):
		self._OrgnlEndToEndId = value if type(value) != base_types.auto else self.make_default("OrgnlEndToEndId")

	@OrgnlEndToEndId.deleter
	def OrgnlEndToEndId(self):
		del self._OrgnlEndToEndId
		self._OrgnlEndToEndId = None

	@property
	def OrgnlGrpInf(self):
		return self._OrgnlGrpInf

	@OrgnlGrpInf.setter
	def OrgnlGrpInf(self, value):
		self._OrgnlGrpInf = value if type(value) != base_types.auto else self.make_default("OrgnlGrpInf")

	@OrgnlGrpInf.deleter
	def OrgnlGrpInf(self):
		del self._OrgnlGrpInf
		self._OrgnlGrpInf = None

	@property
	def OrgnlInstrId(self):
		return self._OrgnlInstrId

	@OrgnlInstrId.setter
	def OrgnlInstrId(self, value):
		self._OrgnlInstrId = value if type(value) != base_types.auto else self.make_default("OrgnlInstrId")

	@OrgnlInstrId.deleter
	def OrgnlInstrId(self):
		del self._OrgnlInstrId
		self._OrgnlInstrId = None

	@property
	def OrgnlIntrBkSttlmAmt(self):
		return self._OrgnlIntrBkSttlmAmt

	@OrgnlIntrBkSttlmAmt.setter
	def OrgnlIntrBkSttlmAmt(self, value):
		self._OrgnlIntrBkSttlmAmt = value if type(value) != base_types.auto else self.make_default("OrgnlIntrBkSttlmAmt")

	@OrgnlIntrBkSttlmAmt.deleter
	def OrgnlIntrBkSttlmAmt(self):
		del self._OrgnlIntrBkSttlmAmt
		self._OrgnlIntrBkSttlmAmt = None

	@property
	def OrgnlIntrBkSttlmDt(self):
		return self._OrgnlIntrBkSttlmDt

	@OrgnlIntrBkSttlmDt.setter
	def OrgnlIntrBkSttlmDt(self, value):
		self._OrgnlIntrBkSttlmDt = value if type(value) != base_types.auto else self.make_default("OrgnlIntrBkSttlmDt")

	@OrgnlIntrBkSttlmDt.deleter
	def OrgnlIntrBkSttlmDt(self):
		del self._OrgnlIntrBkSttlmDt
		self._OrgnlIntrBkSttlmDt = None

	@property
	def OrgnlTxId(self):
		return self._OrgnlTxId

	@OrgnlTxId.setter
	def OrgnlTxId(self, value):
		self._OrgnlTxId = value if type(value) != base_types.auto else self.make_default("OrgnlTxId")

	@OrgnlTxId.deleter
	def OrgnlTxId(self):
		del self._OrgnlTxId
		self._OrgnlTxId = None

	@property
	def OrgnlTxRef(self):
		return self._OrgnlTxRef

	@OrgnlTxRef.setter
	def OrgnlTxRef(self, value):
		self._OrgnlTxRef = value if type(value) != base_types.auto else self.make_default("OrgnlTxRef")

	@OrgnlTxRef.deleter
	def OrgnlTxRef(self):
		del self._OrgnlTxRef
		self._OrgnlTxRef = None

	@property
	def OrgnlUETR(self):
		return self._OrgnlUETR

	@OrgnlUETR.setter
	def OrgnlUETR(self, value):
		self._OrgnlUETR = value if type(value) != base_types.auto else self.make_default("OrgnlUETR")

	@OrgnlUETR.deleter
	def OrgnlUETR(self):
		del self._OrgnlUETR
		self._OrgnlUETR = None

	@property
	def RsltnRltdInf(self):
		return self._RsltnRltdInf

	@RsltnRltdInf.setter
	def RsltnRltdInf(self, value):
		self._RsltnRltdInf = value if type(value) != base_types.auto else self.make_default("RsltnRltdInf")

	@RsltnRltdInf.deleter
	def RsltnRltdInf(self):
		del self._RsltnRltdInf
		self._RsltnRltdInf = None

	@property
	def RslvdCase(self):
		return self._RslvdCase

	@RslvdCase.setter
	def RslvdCase(self, value):
		self._RslvdCase = value if type(value) != base_types.auto else self.make_default("RslvdCase")

	@RslvdCase.deleter
	def RslvdCase(self):
		del self._RslvdCase
		self._RslvdCase = None

	@property
	def TxCxlSts(self):
		return self._TxCxlSts

	@TxCxlSts.setter
	def TxCxlSts(self, value):
		self._TxCxlSts = value if type(value) != base_types.auto else self.make_default("TxCxlSts")

	@TxCxlSts.deleter
	def TxCxlSts(self):
		del self._TxCxlSts
		self._TxCxlSts = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Assgne', type=Party50Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Assgnr', type=Party50Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CxlStsId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CxlStsRsnInf', type=CancellationStatusReason5, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='OrgnlClrSysRef', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlEndToEndId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlGrpInf', type=OriginalGroupInformation33, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlInstrId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlIntrBkSttlmAmt', type=ActiveOrHistoricCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlIntrBkSttlmDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlTxId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlTxRef', type=OriginalTransactionReference47, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlUETR', type=UUIDv4Identifier, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RsltnRltdInf', type=ResolutionData5, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RslvdCase', type=Case6, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxCxlSts', type=CancellationIndividualStatus1Code, min=0, max=1, mutex_group=None, array=False),
	))

