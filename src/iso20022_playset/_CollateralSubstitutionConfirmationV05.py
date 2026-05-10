from . import base_types
from ._Agreement4 import Agreement4
from ._CollateralConfirmation1 import CollateralConfirmation1
from ._Max35Text import Max35Text
from ._Obligation9 import Obligation9
from ._SupplementaryData1 import SupplementaryData1

class CollateralSubstitutionConfirmationV05(base_types._BaseFieldType):

	__slots__ = ["_Agrmt", "_Oblgtn", "_SbstitnConf", "_SplmtryData", "_TxId"]
	@property
	def Agrmt(self):
		return self._Agrmt

	@Agrmt.setter
	def Agrmt(self, value):
		self._Agrmt = value if type(value) != base_types.auto else self.make_default("Agrmt")

	@Agrmt.deleter
	def Agrmt(self):
		del self._Agrmt
		self._Agrmt = None

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
	def SbstitnConf(self):
		return self._SbstitnConf

	@SbstitnConf.setter
	def SbstitnConf(self, value):
		self._SbstitnConf = value if type(value) != base_types.auto else self.make_default("SbstitnConf")

	@SbstitnConf.deleter
	def SbstitnConf(self):
		del self._SbstitnConf
		self._SbstitnConf = None

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
		base_types.FieldEntry(name='Agrmt', type=Agreement4, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Oblgtn', type=Obligation9, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SbstitnConf', type=CollateralConfirmation1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='TxId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
	))

