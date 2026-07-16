# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AdditionalReferences2
from . import Max35Text
from . import MessageIdentification1
from . import Status5Code
from . import SupplementaryData1

class ForeignExchangeTradeCaptureReportAcknowledgementV02(base_types._BaseFieldType):

	__slots__ = ["_AckId", "_DealTcktId", "_Ref", "_SplmtryData", "_Sts", "_TradId"]
	@property
	def AckId(self):
		return self._AckId

	@AckId.setter
	def AckId(self, value):
		self._AckId = value if value is not None else base_types.UninitialisedField(self, 'AckId', MessageIdentification1, False)

	@AckId.deleter
	def AckId(self):
		del self._AckId
		self._AckId = base_types.UninitialisedField(self, 'AckId', MessageIdentification1, False)

	@property
	def DealTcktId(self):
		return self._DealTcktId

	@DealTcktId.setter
	def DealTcktId(self, value):
		self._DealTcktId = value if value is not None else base_types.UninitialisedField(self, 'DealTcktId', Max35Text, False)

	@DealTcktId.deleter
	def DealTcktId(self):
		del self._DealTcktId
		self._DealTcktId = base_types.UninitialisedField(self, 'DealTcktId', Max35Text, False)

	@property
	def Ref(self):
		return self._Ref

	@Ref.setter
	def Ref(self, value):
		self._Ref = value if value is not None else base_types.UninitialisedField(self, 'Ref', AdditionalReferences2, False)

	@Ref.deleter
	def Ref(self):
		del self._Ref
		self._Ref = base_types.UninitialisedField(self, 'Ref', AdditionalReferences2, False)

	@property
	def SplmtryData(self):
		return self._SplmtryData

	@SplmtryData.setter
	def SplmtryData(self, value):
		self._SplmtryData = value if value is not None else base_types.UninitialisedField(self, 'SplmtryData', SupplementaryData1, True)

	@SplmtryData.deleter
	def SplmtryData(self):
		del self._SplmtryData
		self._SplmtryData = base_types.UninitialisedField(self, 'SplmtryData', SupplementaryData1, True)

	@property
	def Sts(self):
		return self._Sts

	@Sts.setter
	def Sts(self, value):
		self._Sts = value if value is not None else base_types.UninitialisedField(self, 'Sts', Status5Code, False)

	@Sts.deleter
	def Sts(self):
		del self._Sts
		self._Sts = base_types.UninitialisedField(self, 'Sts', Status5Code, False)

	@property
	def TradId(self):
		return self._TradId

	@TradId.setter
	def TradId(self, value):
		self._TradId = value if value is not None else base_types.UninitialisedField(self, 'TradId', Max35Text, False)

	@TradId.deleter
	def TradId(self):
		del self._TradId
		self._TradId = base_types.UninitialisedField(self, 'TradId', Max35Text, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AckId', type=MessageIdentification1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DealTcktId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Ref', type=AdditionalReferences2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Sts', type=Status5Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TradId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
	))