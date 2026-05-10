from . import base_types
import ISODate
import UnderlyingGroupInformation1
import DateAndDateTime2Choice
import OriginalTransactionReference35
import Max35Text
import UUIDv4Identifier
import ServiceLevel8Choice
import ActiveOrHistoricCurrencyAndAmount

class UnderlyingPaymentInstruction8(base_types._BaseFieldType):

	__slots__ = ["_OrgnlEndToEndId", "_ReqdExctnDt", "_OrgnlSvcLvl", "_OrgnlPmtInfId", "_OrgnlInstrId", "_OrgnlTxRef", "_ReqdColltnDt", "_OrgnlInstdAmt", "_OrgnlGrpInf", "_OrgnlUETR"]
	@property
	def OrgnlEndToEndId(self):
		return self._OrgnlEndToEndId

	@OrgnlEndToEndId.setter
	def OrgnlEndToEndId(self, value):
		self._OrgnlEndToEndId = value if type(value) != auto else self.make_default("OrgnlEndToEndId")

	@OrgnlEndToEndId.deleter
	def OrgnlEndToEndId(self):
		del self._OrgnlEndToEndId
		self._OrgnlEndToEndId = None

	@property
	def ReqdExctnDt(self):
		return self._ReqdExctnDt

	@ReqdExctnDt.setter
	def ReqdExctnDt(self, value):
		self._ReqdExctnDt = value if type(value) != auto else self.make_default("ReqdExctnDt")

	@ReqdExctnDt.deleter
	def ReqdExctnDt(self):
		del self._ReqdExctnDt
		self._ReqdExctnDt = None

	@property
	def OrgnlSvcLvl(self):
		return self._OrgnlSvcLvl

	@OrgnlSvcLvl.setter
	def OrgnlSvcLvl(self, value):
		self._OrgnlSvcLvl = value if type(value) != auto else self.make_default("OrgnlSvcLvl")

	@OrgnlSvcLvl.deleter
	def OrgnlSvcLvl(self):
		del self._OrgnlSvcLvl
		self._OrgnlSvcLvl = None

	@property
	def OrgnlPmtInfId(self):
		return self._OrgnlPmtInfId

	@OrgnlPmtInfId.setter
	def OrgnlPmtInfId(self, value):
		self._OrgnlPmtInfId = value if type(value) != auto else self.make_default("OrgnlPmtInfId")

	@OrgnlPmtInfId.deleter
	def OrgnlPmtInfId(self):
		del self._OrgnlPmtInfId
		self._OrgnlPmtInfId = None

	@property
	def OrgnlInstrId(self):
		return self._OrgnlInstrId

	@OrgnlInstrId.setter
	def OrgnlInstrId(self, value):
		self._OrgnlInstrId = value if type(value) != auto else self.make_default("OrgnlInstrId")

	@OrgnlInstrId.deleter
	def OrgnlInstrId(self):
		del self._OrgnlInstrId
		self._OrgnlInstrId = None

	@property
	def OrgnlTxRef(self):
		return self._OrgnlTxRef

	@OrgnlTxRef.setter
	def OrgnlTxRef(self, value):
		self._OrgnlTxRef = value if type(value) != auto else self.make_default("OrgnlTxRef")

	@OrgnlTxRef.deleter
	def OrgnlTxRef(self):
		del self._OrgnlTxRef
		self._OrgnlTxRef = None

	@property
	def ReqdColltnDt(self):
		return self._ReqdColltnDt

	@ReqdColltnDt.setter
	def ReqdColltnDt(self, value):
		self._ReqdColltnDt = value if type(value) != auto else self.make_default("ReqdColltnDt")

	@ReqdColltnDt.deleter
	def ReqdColltnDt(self):
		del self._ReqdColltnDt
		self._ReqdColltnDt = None

	@property
	def OrgnlInstdAmt(self):
		return self._OrgnlInstdAmt

	@OrgnlInstdAmt.setter
	def OrgnlInstdAmt(self, value):
		self._OrgnlInstdAmt = value if type(value) != auto else self.make_default("OrgnlInstdAmt")

	@OrgnlInstdAmt.deleter
	def OrgnlInstdAmt(self):
		del self._OrgnlInstdAmt
		self._OrgnlInstdAmt = None

	@property
	def OrgnlGrpInf(self):
		return self._OrgnlGrpInf

	@OrgnlGrpInf.setter
	def OrgnlGrpInf(self, value):
		self._OrgnlGrpInf = value if type(value) != auto else self.make_default("OrgnlGrpInf")

	@OrgnlGrpInf.deleter
	def OrgnlGrpInf(self):
		del self._OrgnlGrpInf
		self._OrgnlGrpInf = None

	@property
	def OrgnlUETR(self):
		return self._OrgnlUETR

	@OrgnlUETR.setter
	def OrgnlUETR(self, value):
		self._OrgnlUETR = value if type(value) != auto else self.make_default("OrgnlUETR")

	@OrgnlUETR.deleter
	def OrgnlUETR(self):
		del self._OrgnlUETR
		self._OrgnlUETR = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='OrgnlEndToEndId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ReqdExctnDt', type=DateAndDateTime2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlSvcLvl', type=ServiceLevel8Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlPmtInfId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlInstrId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlTxRef', type=OriginalTransactionReference35, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ReqdColltnDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlInstdAmt', type=ActiveOrHistoricCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlGrpInf', type=UnderlyingGroupInformation1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlUETR', type=UUIDv4Identifier, min=0, max=1, mutex_group=None, array=False),
	))

