from . import base_types
from ._CardDataReading1Code import CardDataReading1Code
from ._ContentInformationType10 import ContentInformationType10
from ._CurrencyAndAmount import CurrencyAndAmount
from ._Exact3AlphaNumericText import Exact3AlphaNumericText
from ._Max3Text import Max3Text
from ._PlainCardData24 import PlainCardData24
from ._TrueFalseIndicator import TrueFalseIndicator

class PaymentCard37(base_types._BaseFieldType):

	__slots__ = ["_CardCcyCd", "_CardCtryCd", "_CardDataNtryMd", "_ElctrncPrsBal", "_FllbckInd", "_PlainCardData", "_PrtctdCardData"]
	@property
	def CardCcyCd(self):
		return self._CardCcyCd

	@CardCcyCd.setter
	def CardCcyCd(self, value):
		self._CardCcyCd = value if type(value) != base_types.auto else self.make_default("CardCcyCd")

	@CardCcyCd.deleter
	def CardCcyCd(self):
		del self._CardCcyCd
		self._CardCcyCd = None

	@property
	def CardCtryCd(self):
		return self._CardCtryCd

	@CardCtryCd.setter
	def CardCtryCd(self, value):
		self._CardCtryCd = value if type(value) != base_types.auto else self.make_default("CardCtryCd")

	@CardCtryCd.deleter
	def CardCtryCd(self):
		del self._CardCtryCd
		self._CardCtryCd = None

	@property
	def CardDataNtryMd(self):
		return self._CardDataNtryMd

	@CardDataNtryMd.setter
	def CardDataNtryMd(self, value):
		self._CardDataNtryMd = value if type(value) != base_types.auto else self.make_default("CardDataNtryMd")

	@CardDataNtryMd.deleter
	def CardDataNtryMd(self):
		del self._CardDataNtryMd
		self._CardDataNtryMd = None

	@property
	def ElctrncPrsBal(self):
		return self._ElctrncPrsBal

	@ElctrncPrsBal.setter
	def ElctrncPrsBal(self, value):
		self._ElctrncPrsBal = value if type(value) != base_types.auto else self.make_default("ElctrncPrsBal")

	@ElctrncPrsBal.deleter
	def ElctrncPrsBal(self):
		del self._ElctrncPrsBal
		self._ElctrncPrsBal = None

	@property
	def FllbckInd(self):
		return self._FllbckInd

	@FllbckInd.setter
	def FllbckInd(self, value):
		self._FllbckInd = value if type(value) != base_types.auto else self.make_default("FllbckInd")

	@FllbckInd.deleter
	def FllbckInd(self):
		del self._FllbckInd
		self._FllbckInd = None

	@property
	def PlainCardData(self):
		return self._PlainCardData

	@PlainCardData.setter
	def PlainCardData(self, value):
		self._PlainCardData = value if type(value) != base_types.auto else self.make_default("PlainCardData")

	@PlainCardData.deleter
	def PlainCardData(self):
		del self._PlainCardData
		self._PlainCardData = None

	@property
	def PrtctdCardData(self):
		return self._PrtctdCardData

	@PrtctdCardData.setter
	def PrtctdCardData(self, value):
		self._PrtctdCardData = value if type(value) != base_types.auto else self.make_default("PrtctdCardData")

	@PrtctdCardData.deleter
	def PrtctdCardData(self):
		del self._PrtctdCardData
		self._PrtctdCardData = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='CardCcyCd', type=Exact3AlphaNumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CardCtryCd', type=Max3Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CardDataNtryMd', type=CardDataReading1Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ElctrncPrsBal', type=CurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FllbckInd', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PlainCardData', type=PlainCardData24, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrtctdCardData', type=ContentInformationType10, min=0, max=1, mutex_group=None, array=False),
	))

