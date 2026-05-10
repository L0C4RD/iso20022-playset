from . import base_types
from ._ActiveOrHistoricCurrencyAndAmount import ActiveOrHistoricCurrencyAndAmount
from ._ISODate import ISODate
from ._Max105Text import Max105Text
from ._Max35Text import Max35Text
from ._NotificationStatus3Code import NotificationStatus3Code
from ._OriginalItemReference7 import OriginalItemReference7
from ._UUIDv4Identifier import UUIDv4Identifier

class OriginalItemAndStatus8(base_types._BaseFieldType):

	__slots__ = ["_AddtlStsInf", "_Amt", "_ItmSts", "_OrgnlEndToEndId", "_OrgnlItmId", "_OrgnlItmRef", "_OrgnlUETR", "_XpctdValDt"]
	@property
	def AddtlStsInf(self):
		return self._AddtlStsInf

	@AddtlStsInf.setter
	def AddtlStsInf(self, value):
		self._AddtlStsInf = value if type(value) != base_types.auto else self.make_default("AddtlStsInf")

	@AddtlStsInf.deleter
	def AddtlStsInf(self):
		del self._AddtlStsInf
		self._AddtlStsInf = None

	@property
	def Amt(self):
		return self._Amt

	@Amt.setter
	def Amt(self, value):
		self._Amt = value if type(value) != base_types.auto else self.make_default("Amt")

	@Amt.deleter
	def Amt(self):
		del self._Amt
		self._Amt = None

	@property
	def ItmSts(self):
		return self._ItmSts

	@ItmSts.setter
	def ItmSts(self, value):
		self._ItmSts = value if type(value) != base_types.auto else self.make_default("ItmSts")

	@ItmSts.deleter
	def ItmSts(self):
		del self._ItmSts
		self._ItmSts = None

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
	def OrgnlItmId(self):
		return self._OrgnlItmId

	@OrgnlItmId.setter
	def OrgnlItmId(self, value):
		self._OrgnlItmId = value if type(value) != base_types.auto else self.make_default("OrgnlItmId")

	@OrgnlItmId.deleter
	def OrgnlItmId(self):
		del self._OrgnlItmId
		self._OrgnlItmId = None

	@property
	def OrgnlItmRef(self):
		return self._OrgnlItmRef

	@OrgnlItmRef.setter
	def OrgnlItmRef(self, value):
		self._OrgnlItmRef = value if type(value) != base_types.auto else self.make_default("OrgnlItmRef")

	@OrgnlItmRef.deleter
	def OrgnlItmRef(self):
		del self._OrgnlItmRef
		self._OrgnlItmRef = None

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
	def XpctdValDt(self):
		return self._XpctdValDt

	@XpctdValDt.setter
	def XpctdValDt(self, value):
		self._XpctdValDt = value if type(value) != base_types.auto else self.make_default("XpctdValDt")

	@XpctdValDt.deleter
	def XpctdValDt(self):
		del self._XpctdValDt
		self._XpctdValDt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AddtlStsInf', type=Max105Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Amt', type=ActiveOrHistoricCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ItmSts', type=NotificationStatus3Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlEndToEndId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlItmId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlItmRef', type=OriginalItemReference7, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlUETR', type=UUIDv4Identifier, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='XpctdValDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
	))

