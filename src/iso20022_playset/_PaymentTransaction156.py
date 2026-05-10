from . import base_types
from ._ActiveOrHistoricCurrencyAndAmount import ActiveOrHistoricCurrencyAndAmount
from ._ChargeBearerType1Code import ChargeBearerType1Code
from ._Max35Text import Max35Text
from ._OriginalTransactionReference42 import OriginalTransactionReference42
from ._PaymentReversalReason10 import PaymentReversalReason10
from ._SupplementaryData1 import SupplementaryData1
from ._UUIDv4Identifier import UUIDv4Identifier

class PaymentTransaction156(base_types._BaseFieldType):

	__slots__ = ["_ChrgBr", "_OrgnlEndToEndId", "_OrgnlInstdAmt", "_OrgnlInstrId", "_OrgnlTxRef", "_OrgnlUETR", "_RvsdInstdAmt", "_RvslId", "_RvslRsnInf", "_SplmtryData"]
	@property
	def ChrgBr(self):
		return self._ChrgBr

	@ChrgBr.setter
	def ChrgBr(self, value):
		self._ChrgBr = value if type(value) != base_types.auto else self.make_default("ChrgBr")

	@ChrgBr.deleter
	def ChrgBr(self):
		del self._ChrgBr
		self._ChrgBr = None

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
	def RvsdInstdAmt(self):
		return self._RvsdInstdAmt

	@RvsdInstdAmt.setter
	def RvsdInstdAmt(self, value):
		self._RvsdInstdAmt = value if type(value) != base_types.auto else self.make_default("RvsdInstdAmt")

	@RvsdInstdAmt.deleter
	def RvsdInstdAmt(self):
		del self._RvsdInstdAmt
		self._RvsdInstdAmt = None

	@property
	def RvslId(self):
		return self._RvslId

	@RvslId.setter
	def RvslId(self, value):
		self._RvslId = value if type(value) != base_types.auto else self.make_default("RvslId")

	@RvslId.deleter
	def RvslId(self):
		del self._RvslId
		self._RvslId = None

	@property
	def RvslRsnInf(self):
		return self._RvslRsnInf

	@RvslRsnInf.setter
	def RvslRsnInf(self, value):
		self._RvslRsnInf = value if type(value) != base_types.auto else self.make_default("RvslRsnInf")

	@RvslRsnInf.deleter
	def RvslRsnInf(self):
		del self._RvslRsnInf
		self._RvslRsnInf = None

	@property
	def SplmtryData(self):
		return self._SplmtryData

	@SplmtryData.setter
	def SplmtryData(self, value):
		self._SplmtryData = value if type(value) != base_types.auto else self.make_default("SplmtryData")

	@SplmtryData.deleter
	def SplmtryData(self):
		del self._SplmtryData
		self._SplmtryData = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='ChrgBr', type=ChargeBearerType1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlEndToEndId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlInstdAmt', type=ActiveOrHistoricCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlInstrId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlTxRef', type=OriginalTransactionReference42, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlUETR', type=UUIDv4Identifier, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RvsdInstdAmt', type=ActiveOrHistoricCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RvslId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RvslRsnInf', type=PaymentReversalReason10, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
	))

