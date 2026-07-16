# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CardDataReading1Code
from . import ContentInformationType10
from . import CurrencyAndAmount
from . import Exact3AlphaNumericText
from . import Max3Text
from . import PlainCardData24
from . import TrueFalseIndicator

class PaymentCard37(base_types._BaseFieldType):

	__slots__ = ["_CardCcyCd", "_CardCtryCd", "_CardDataNtryMd", "_ElctrncPrsBal", "_FllbckInd", "_PlainCardData", "_PrtctdCardData"]
	@property
	def CardCcyCd(self):
		return self._CardCcyCd

	@CardCcyCd.setter
	def CardCcyCd(self, value):
		self._CardCcyCd = value if value is not None else base_types.UninitialisedField(self, 'CardCcyCd', Exact3AlphaNumericText, False)

	@CardCcyCd.deleter
	def CardCcyCd(self):
		del self._CardCcyCd
		self._CardCcyCd = base_types.UninitialisedField(self, 'CardCcyCd', Exact3AlphaNumericText, False)

	@property
	def CardCtryCd(self):
		return self._CardCtryCd

	@CardCtryCd.setter
	def CardCtryCd(self, value):
		self._CardCtryCd = value if value is not None else base_types.UninitialisedField(self, 'CardCtryCd', Max3Text, False)

	@CardCtryCd.deleter
	def CardCtryCd(self):
		del self._CardCtryCd
		self._CardCtryCd = base_types.UninitialisedField(self, 'CardCtryCd', Max3Text, False)

	@property
	def CardDataNtryMd(self):
		return self._CardDataNtryMd

	@CardDataNtryMd.setter
	def CardDataNtryMd(self, value):
		self._CardDataNtryMd = value if value is not None else base_types.UninitialisedField(self, 'CardDataNtryMd', CardDataReading1Code, False)

	@CardDataNtryMd.deleter
	def CardDataNtryMd(self):
		del self._CardDataNtryMd
		self._CardDataNtryMd = base_types.UninitialisedField(self, 'CardDataNtryMd', CardDataReading1Code, False)

	@property
	def ElctrncPrsBal(self):
		return self._ElctrncPrsBal

	@ElctrncPrsBal.setter
	def ElctrncPrsBal(self, value):
		self._ElctrncPrsBal = value if value is not None else base_types.UninitialisedField(self, 'ElctrncPrsBal', CurrencyAndAmount, False)

	@ElctrncPrsBal.deleter
	def ElctrncPrsBal(self):
		del self._ElctrncPrsBal
		self._ElctrncPrsBal = base_types.UninitialisedField(self, 'ElctrncPrsBal', CurrencyAndAmount, False)

	@property
	def FllbckInd(self):
		return self._FllbckInd

	@FllbckInd.setter
	def FllbckInd(self, value):
		self._FllbckInd = value if value is not None else base_types.UninitialisedField(self, 'FllbckInd', TrueFalseIndicator, False)

	@FllbckInd.deleter
	def FllbckInd(self):
		del self._FllbckInd
		self._FllbckInd = base_types.UninitialisedField(self, 'FllbckInd', TrueFalseIndicator, False)

	@property
	def PlainCardData(self):
		return self._PlainCardData

	@PlainCardData.setter
	def PlainCardData(self, value):
		self._PlainCardData = value if value is not None else base_types.UninitialisedField(self, 'PlainCardData', PlainCardData24, False)

	@PlainCardData.deleter
	def PlainCardData(self):
		del self._PlainCardData
		self._PlainCardData = base_types.UninitialisedField(self, 'PlainCardData', PlainCardData24, False)

	@property
	def PrtctdCardData(self):
		return self._PrtctdCardData

	@PrtctdCardData.setter
	def PrtctdCardData(self, value):
		self._PrtctdCardData = value if value is not None else base_types.UninitialisedField(self, 'PrtctdCardData', ContentInformationType10, False)

	@PrtctdCardData.deleter
	def PrtctdCardData(self):
		del self._PrtctdCardData
		self._PrtctdCardData = base_types.UninitialisedField(self, 'PrtctdCardData', ContentInformationType10, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='CardCcyCd', type=Exact3AlphaNumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CardCtryCd', type=Max3Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CardDataNtryMd', type=CardDataReading1Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ElctrncPrsBal', type=CurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FllbckInd', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PlainCardData', type=PlainCardData24, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrtctdCardData', type=ContentInformationType10, min=0, max=1, mutex_group=None, array=False),
	))