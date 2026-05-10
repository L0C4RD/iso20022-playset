from . import base_types
from ._OriginalTransactionReference42 import OriginalTransactionReference42
from ._Case6 import Case6
from ._UUIDv4Identifier import UUIDv4Identifier
from ._CancellationIndividualStatus1Code import CancellationIndividualStatus1Code
from ._DateAndDateTime2Choice import DateAndDateTime2Choice
from ._CancellationStatusReason5 import CancellationStatusReason5
from ._Max35Text import Max35Text
from ._ActiveOrHistoricCurrencyAndAmount import ActiveOrHistoricCurrencyAndAmount
from ._ISODate import ISODate

class PaymentTransaction153(base_types._BaseFieldType):

	__slots__ = ["_OrgnlEndToEndId", "_RslvdCase", "_OrgnlInstdAmt", "_OrgnlInstrId", "_OrgnlTxRef", "_TxCxlSts", "_CxlStsRsnInf", "_OrgnlReqdExctnDt", "_OrgnlReqdColltnDt", "_CxlStsId", "_UETR"]
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
	def OrgnlInstdAmt(self):
		return self._OrgnlInstdAmt

	@OrgnlInstdAmt.setter
	def OrgnlInstdAmt(self, value):
		self._OrgnlInstdAmt = value if type(value) != base_types.auto else self.make_default("OrgnlInstdAmt")

	@OrgnlInstdAmt.deleter
	def OrgnlInstdAmt(self):
		del self._OrgnlInstdAmt
		self._OrgnlInstdAmt = None

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
	def TxCxlSts(self):
		return self._TxCxlSts

	@TxCxlSts.setter
	def TxCxlSts(self, value):
		self._TxCxlSts = value if type(value) != base_types.auto else self.make_default("TxCxlSts")

	@TxCxlSts.deleter
	def TxCxlSts(self):
		del self._TxCxlSts
		self._TxCxlSts = None

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
	def OrgnlReqdExctnDt(self):
		return self._OrgnlReqdExctnDt

	@OrgnlReqdExctnDt.setter
	def OrgnlReqdExctnDt(self, value):
		self._OrgnlReqdExctnDt = value if type(value) != base_types.auto else self.make_default("OrgnlReqdExctnDt")

	@OrgnlReqdExctnDt.deleter
	def OrgnlReqdExctnDt(self):
		del self._OrgnlReqdExctnDt
		self._OrgnlReqdExctnDt = None

	@property
	def OrgnlReqdColltnDt(self):
		return self._OrgnlReqdColltnDt

	@OrgnlReqdColltnDt.setter
	def OrgnlReqdColltnDt(self, value):
		self._OrgnlReqdColltnDt = value if type(value) != base_types.auto else self.make_default("OrgnlReqdColltnDt")

	@OrgnlReqdColltnDt.deleter
	def OrgnlReqdColltnDt(self):
		del self._OrgnlReqdColltnDt
		self._OrgnlReqdColltnDt = None

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
	def UETR(self):
		return self._UETR

	@UETR.setter
	def UETR(self, value):
		self._UETR = value if type(value) != base_types.auto else self.make_default("UETR")

	@UETR.deleter
	def UETR(self):
		del self._UETR
		self._UETR = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='OrgnlEndToEndId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RslvdCase', type=Case6, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlInstdAmt', type=ActiveOrHistoricCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlInstrId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlTxRef', type=OriginalTransactionReference42, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxCxlSts', type=CancellationIndividualStatus1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CxlStsRsnInf', type=CancellationStatusReason5, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='OrgnlReqdExctnDt', type=DateAndDateTime2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlReqdColltnDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CxlStsId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UETR', type=UUIDv4Identifier, min=0, max=1, mutex_group=None, array=False),
	))

