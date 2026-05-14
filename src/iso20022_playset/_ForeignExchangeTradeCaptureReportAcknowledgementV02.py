# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._AdditionalReferences2 import AdditionalReferences2
from ._Max35Text import Max35Text
from ._MessageIdentification1 import MessageIdentification1
from ._Status5Code import Status5Code
from ._SupplementaryData1 import SupplementaryData1

class ForeignExchangeTradeCaptureReportAcknowledgementV02(base_types._BaseFieldType):

	__slots__ = ["_AckId", "_DealTcktId", "_Ref", "_SplmtryData", "_Sts", "_TradId"]
	@property
	def AckId(self):
		return self._AckId

	@AckId.setter
	def AckId(self, value):
		self._AckId = value if type(value) != base_types.auto else self.make_default("AckId")

	@AckId.deleter
	def AckId(self):
		del self._AckId
		self._AckId = None

	@property
	def DealTcktId(self):
		return self._DealTcktId

	@DealTcktId.setter
	def DealTcktId(self, value):
		self._DealTcktId = value if type(value) != base_types.auto else self.make_default("DealTcktId")

	@DealTcktId.deleter
	def DealTcktId(self):
		del self._DealTcktId
		self._DealTcktId = None

	@property
	def Ref(self):
		return self._Ref

	@Ref.setter
	def Ref(self, value):
		self._Ref = value if type(value) != base_types.auto else self.make_default("Ref")

	@Ref.deleter
	def Ref(self):
		del self._Ref
		self._Ref = None

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

	@property
	def Sts(self):
		return self._Sts

	@Sts.setter
	def Sts(self, value):
		self._Sts = value if type(value) != base_types.auto else self.make_default("Sts")

	@Sts.deleter
	def Sts(self):
		del self._Sts
		self._Sts = None

	@property
	def TradId(self):
		return self._TradId

	@TradId.setter
	def TradId(self, value):
		self._TradId = value if type(value) != base_types.auto else self.make_default("TradId")

	@TradId.deleter
	def TradId(self):
		del self._TradId
		self._TradId = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AckId', type=MessageIdentification1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DealTcktId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Ref', type=AdditionalReferences2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Sts', type=Status5Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TradId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
	))