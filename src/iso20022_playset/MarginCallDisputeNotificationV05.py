import base_types
import Max35Text
import SupplementaryData1
import Obligation9
import DisputeNotification2Choice

class MarginCallDisputeNotificationV05(base_types._BaseFieldType):

	__slots__ = ["_TxId", "_SplmtryData", "_DsptNtfctn", "_Oblgtn"]
	@property
	def TxId(self):
		return self._TxId

	@TxId.setter
	def TxId(self, value):
		self._TxId = value if type(value) != auto else self.make_default("TxId")

	@TxId.deleter
	def TxId(self):
		del self._TxId
		self._TxId = None

	@property
	def SplmtryData(self):
		return self._SplmtryData

	@SplmtryData.setter
	def SplmtryData(self, value):
		self._SplmtryData = value if type(value) != auto else self.make_default("SplmtryData")

	@SplmtryData.deleter
	def SplmtryData(self):
		del self._SplmtryData
		self._SplmtryData = None

	@property
	def DsptNtfctn(self):
		return self._DsptNtfctn

	@DsptNtfctn.setter
	def DsptNtfctn(self, value):
		self._DsptNtfctn = value if type(value) != auto else self.make_default("DsptNtfctn")

	@DsptNtfctn.deleter
	def DsptNtfctn(self):
		del self._DsptNtfctn
		self._DsptNtfctn = None

	@property
	def Oblgtn(self):
		return self._Oblgtn

	@Oblgtn.setter
	def Oblgtn(self, value):
		self._Oblgtn = value if type(value) != auto else self.make_default("Oblgtn")

	@Oblgtn.deleter
	def Oblgtn(self):
		del self._Oblgtn
		self._Oblgtn = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='TxId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='DsptNtfctn', type=DisputeNotification2Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Oblgtn', type=Obligation9, min=1, max=1, mutex_group=None, array=False),
	))

