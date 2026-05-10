from . import base_types
from .Max35Text import Max35Text
from .ServiceLevel8Choice import ServiceLevel8Choice
from .OriginalTransactionReference35 import OriginalTransactionReference35
from .ActiveOrHistoricCurrencyAndAmount import ActiveOrHistoricCurrencyAndAmount
from .ISODate import ISODate
from .UUIDv4Identifier import UUIDv4Identifier
from .UnderlyingGroupInformation1 import UnderlyingGroupInformation1

class UnderlyingPaymentTransaction7(base_types._BaseFieldType):

	__slots__ = ["_OrgnlUETR", "_OrgnlEndToEndId", "_OrgnlSvcLvl", "_OrgnlTxRef", "_OrgnlTxId", "_OrgnlIntrBkSttlmDt", "_OrgnlGrpInf", "_OrgnlIntrBkSttlmAmt", "_OrgnlInstrId"]
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
	def OrgnlSvcLvl(self):
		return self._OrgnlSvcLvl

	@OrgnlSvcLvl.setter
	def OrgnlSvcLvl(self, value):
		self._OrgnlSvcLvl = value if type(value) != base_types.auto else self.make_default("OrgnlSvcLvl")

	@OrgnlSvcLvl.deleter
	def OrgnlSvcLvl(self):
		del self._OrgnlSvcLvl
		self._OrgnlSvcLvl = None

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
	def OrgnlInstrId(self):
		return self._OrgnlInstrId

	@OrgnlInstrId.setter
	def OrgnlInstrId(self, value):
		self._OrgnlInstrId = value if type(value) != base_types.auto else self.make_default("OrgnlInstrId")

	@OrgnlInstrId.deleter
	def OrgnlInstrId(self):
		del self._OrgnlInstrId
		self._OrgnlInstrId = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='OrgnlUETR', type=UUIDv4Identifier, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlEndToEndId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlSvcLvl', type=ServiceLevel8Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlTxRef', type=OriginalTransactionReference35, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlTxId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlIntrBkSttlmDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlGrpInf', type=UnderlyingGroupInformation1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlIntrBkSttlmAmt', type=ActiveOrHistoricCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlInstrId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
	))

