from . import base_types
from ._Compensation5 import Compensation5
from ._Charges14 import Charges14
from ._ISODate import ISODate
from ._Max35Text import Max35Text
from ._ActiveOrHistoricCurrencyAndAmount import ActiveOrHistoricCurrencyAndAmount
from ._UUIDv4Identifier import UUIDv4Identifier
from ._ClearingChannel2Code import ClearingChannel2Code

class ResolutionData5(base_types._BaseFieldType):

	__slots__ = ["_IntrBkSttlmAmt", "_IntrBkSttlmDt", "_ClrChanl", "_Compstn", "_EndToEndId", "_ChrgsInf", "_TxId", "_UETR"]
	@property
	def IntrBkSttlmAmt(self):
		return self._IntrBkSttlmAmt

	@IntrBkSttlmAmt.setter
	def IntrBkSttlmAmt(self, value):
		self._IntrBkSttlmAmt = value if type(value) != base_types.auto else self.make_default("IntrBkSttlmAmt")

	@IntrBkSttlmAmt.deleter
	def IntrBkSttlmAmt(self):
		del self._IntrBkSttlmAmt
		self._IntrBkSttlmAmt = None

	@property
	def IntrBkSttlmDt(self):
		return self._IntrBkSttlmDt

	@IntrBkSttlmDt.setter
	def IntrBkSttlmDt(self, value):
		self._IntrBkSttlmDt = value if type(value) != base_types.auto else self.make_default("IntrBkSttlmDt")

	@IntrBkSttlmDt.deleter
	def IntrBkSttlmDt(self):
		del self._IntrBkSttlmDt
		self._IntrBkSttlmDt = None

	@property
	def ClrChanl(self):
		return self._ClrChanl

	@ClrChanl.setter
	def ClrChanl(self, value):
		self._ClrChanl = value if type(value) != base_types.auto else self.make_default("ClrChanl")

	@ClrChanl.deleter
	def ClrChanl(self):
		del self._ClrChanl
		self._ClrChanl = None

	@property
	def Compstn(self):
		return self._Compstn

	@Compstn.setter
	def Compstn(self, value):
		self._Compstn = value if type(value) != base_types.auto else self.make_default("Compstn")

	@Compstn.deleter
	def Compstn(self):
		del self._Compstn
		self._Compstn = None

	@property
	def EndToEndId(self):
		return self._EndToEndId

	@EndToEndId.setter
	def EndToEndId(self, value):
		self._EndToEndId = value if type(value) != base_types.auto else self.make_default("EndToEndId")

	@EndToEndId.deleter
	def EndToEndId(self):
		del self._EndToEndId
		self._EndToEndId = None

	@property
	def ChrgsInf(self):
		return self._ChrgsInf

	@ChrgsInf.setter
	def ChrgsInf(self, value):
		self._ChrgsInf = value if type(value) != base_types.auto else self.make_default("ChrgsInf")

	@ChrgsInf.deleter
	def ChrgsInf(self):
		del self._ChrgsInf
		self._ChrgsInf = None

	@property
	def TxId(self):
		return self._TxId

	@TxId.setter
	def TxId(self, value):
		self._TxId = value if type(value) != base_types.auto else self.make_default("TxId")

	@TxId.deleter
	def TxId(self):
		del self._TxId
		self._TxId = None

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
		base_types.FieldEntry(name='IntrBkSttlmAmt', type=ActiveOrHistoricCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IntrBkSttlmDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ClrChanl', type=ClearingChannel2Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Compstn', type=Compensation5, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='EndToEndId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ChrgsInf', type=Charges14, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='TxId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UETR', type=UUIDv4Identifier, min=0, max=1, mutex_group=None, array=False),
	))

