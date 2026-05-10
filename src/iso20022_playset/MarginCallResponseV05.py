import base_types
import AgreedAmount1Choice
import Response1
import MarginCall1
import Max35Text
import Obligation9
import Agreement4
import SupplementaryData1

class MarginCallResponseV05(base_types._BaseFieldType):

	__slots__ = ["_SplmtryData", "_Agrmt", "_AgrdAmtDueToA", "_RspnDtls", "_Oblgtn", "_TxId", "_AgrdAmtDueToB", "_MrgnDtlsDueToA", "_MrgnDtlsDueToB"]
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
	def AgrdAmtDueToA(self):
		return self._AgrdAmtDueToA

	@AgrdAmtDueToA.setter
	def AgrdAmtDueToA(self, value):
		self._AgrdAmtDueToA = value if type(value) != auto else self.make_default("AgrdAmtDueToA")

	@AgrdAmtDueToA.deleter
	def AgrdAmtDueToA(self):
		del self._AgrdAmtDueToA
		self._AgrdAmtDueToA = None

	@property
	def RspnDtls(self):
		return self._RspnDtls

	@RspnDtls.setter
	def RspnDtls(self, value):
		self._RspnDtls = value if type(value) != auto else self.make_default("RspnDtls")

	@RspnDtls.deleter
	def RspnDtls(self):
		del self._RspnDtls
		self._RspnDtls = None

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
	def AgrdAmtDueToB(self):
		return self._AgrdAmtDueToB

	@AgrdAmtDueToB.setter
	def AgrdAmtDueToB(self, value):
		self._AgrdAmtDueToB = value if type(value) != auto else self.make_default("AgrdAmtDueToB")

	@AgrdAmtDueToB.deleter
	def AgrdAmtDueToB(self):
		del self._AgrdAmtDueToB
		self._AgrdAmtDueToB = None

	@property
	def MrgnDtlsDueToA(self):
		return self._MrgnDtlsDueToA

	@MrgnDtlsDueToA.setter
	def MrgnDtlsDueToA(self, value):
		self._MrgnDtlsDueToA = value if type(value) != auto else self.make_default("MrgnDtlsDueToA")

	@MrgnDtlsDueToA.deleter
	def MrgnDtlsDueToA(self):
		del self._MrgnDtlsDueToA
		self._MrgnDtlsDueToA = None

	@property
	def MrgnDtlsDueToB(self):
		return self._MrgnDtlsDueToB

	@MrgnDtlsDueToB.setter
	def MrgnDtlsDueToB(self, value):
		self._MrgnDtlsDueToB = value if type(value) != auto else self.make_default("MrgnDtlsDueToB")

	@MrgnDtlsDueToB.deleter
	def MrgnDtlsDueToB(self):
		del self._MrgnDtlsDueToB
		self._MrgnDtlsDueToB = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Agrmt', type=Agreement4, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AgrdAmtDueToA', type=AgreedAmount1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RspnDtls', type=Response1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Oblgtn', type=Obligation9, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AgrdAmtDueToB', type=AgreedAmount1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MrgnDtlsDueToA', type=MarginCall1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MrgnDtlsDueToB', type=MarginCall1, min=0, max=1, mutex_group=None, array=False),
	))

