from . import base_types
from ._ISODate import ISODate
from ._UUIDv4Identifier import UUIDv4Identifier
from ._ActiveOrHistoricCurrencyAndAmount import ActiveOrHistoricCurrencyAndAmount
from ._Max35Text import Max35Text
from ._OriginalItemReference7 import OriginalItemReference7

class OriginalItem8(base_types._BaseFieldType):

	__slots__ = ["_OrgnlEndToEndId", "_XpctdValDt", "_OrgnlItmRef", "_UETR", "_Amt", "_OrgnlItmId"]
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
	def UETR(self):
		return self._UETR

	@UETR.setter
	def UETR(self, value):
		self._UETR = value if type(value) != base_types.auto else self.make_default("UETR")

	@UETR.deleter
	def UETR(self):
		del self._UETR
		self._UETR = None

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
		base_types.FieldEntry(name='Amt', type=ActiveOrHistoricCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlEndToEndId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlItmId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlItmRef', type=OriginalItemReference7, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UETR', type=UUIDv4Identifier, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='XpctdValDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
	))

