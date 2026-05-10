from . import base_types
from .Reference16 import Reference16
from .CollateralCancellationStatus2 import CollateralCancellationStatus2
from .SupplementaryData1 import SupplementaryData1
from .Obligation9 import Obligation9
from .Max35Text import Max35Text

class CollateralManagementCancellationStatusV05(base_types._BaseFieldType):

	__slots__ = ["_CxlSts", "_SplmtryData", "_Ref", "_Oblgtn", "_TxId"]
	@property
	def CxlSts(self):
		return self._CxlSts

	@CxlSts.setter
	def CxlSts(self, value):
		self._CxlSts = value if type(value) != base_types.auto else self.make_default("CxlSts")

	@CxlSts.deleter
	def CxlSts(self):
		del self._CxlSts
		self._CxlSts = None

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
	def Oblgtn(self):
		return self._Oblgtn

	@Oblgtn.setter
	def Oblgtn(self, value):
		self._Oblgtn = value if type(value) != base_types.auto else self.make_default("Oblgtn")

	@Oblgtn.deleter
	def Oblgtn(self):
		del self._Oblgtn
		self._Oblgtn = None

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

	_field_defs = frozenset((
		base_types.FieldEntry(name='CxlSts', type=CollateralCancellationStatus2, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Ref', type=Reference16, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Oblgtn', type=Obligation9, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
	))

