from . import base_types
import Obligation9
import Max35Text
import CollateralSubstitution7
import Agreement4
import CollateralSubstitution8
import SupplementaryData1

class CollateralSubstitutionRequestV05(base_types._BaseFieldType):

	__slots__ = ["_Agrmt", "_CollSbstitnDlvr", "_TxId", "_CollSbstitnRtr", "_SplmtryData", "_Oblgtn"]
	@property
	def Agrmt(self):
		return self._Agrmt

	@Agrmt.setter
	def Agrmt(self, value):
		self._Agrmt = value if type(value) != auto else self.make_default("Agrmt")

	@Agrmt.deleter
	def Agrmt(self):
		del self._Agrmt
		self._Agrmt = None

	@property
	def CollSbstitnDlvr(self):
		return self._CollSbstitnDlvr

	@CollSbstitnDlvr.setter
	def CollSbstitnDlvr(self, value):
		self._CollSbstitnDlvr = value if type(value) != auto else self.make_default("CollSbstitnDlvr")

	@CollSbstitnDlvr.deleter
	def CollSbstitnDlvr(self):
		del self._CollSbstitnDlvr
		self._CollSbstitnDlvr = None

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
	def CollSbstitnRtr(self):
		return self._CollSbstitnRtr

	@CollSbstitnRtr.setter
	def CollSbstitnRtr(self, value):
		self._CollSbstitnRtr = value if type(value) != auto else self.make_default("CollSbstitnRtr")

	@CollSbstitnRtr.deleter
	def CollSbstitnRtr(self):
		del self._CollSbstitnRtr
		self._CollSbstitnRtr = None

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
		base_types.FieldEntry(name='Agrmt', type=Agreement4, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CollSbstitnDlvr', type=CollateralSubstitution8, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CollSbstitnRtr', type=CollateralSubstitution7, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Oblgtn', type=Obligation9, min=1, max=1, mutex_group=None, array=False),
	))

