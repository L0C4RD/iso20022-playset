import base_types
import MarginCallResult3
import MarginCall1
import Obligation9
import SupplementaryData1
import Max35Text
import MarginRequirement1Choice
import Agreement4
import ExpectedCollateral2Choice
import MarginCall3

class MarginCallRequestV05(base_types._BaseFieldType):

	__slots__ = ["_RqrmntDtlsDueToA", "_SplmtryData", "_RqrmntDtlsDueToB", "_XpctdCollDueToA", "_Agrmt", "_MrgnCallRslt", "_Oblgtn", "_TxId", "_XpctdCollDueToB", "_MrgnCallDtls", "_MrgnDtlsDueToA", "_MrgnDtlsDueToB"]
	@property
	def RqrmntDtlsDueToA(self):
		return self._RqrmntDtlsDueToA

	@RqrmntDtlsDueToA.setter
	def RqrmntDtlsDueToA(self, value):
		self._RqrmntDtlsDueToA = value if type(value) != auto else self.make_default("RqrmntDtlsDueToA")

	@RqrmntDtlsDueToA.deleter
	def RqrmntDtlsDueToA(self):
		del self._RqrmntDtlsDueToA
		self._RqrmntDtlsDueToA = None

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
	def RqrmntDtlsDueToB(self):
		return self._RqrmntDtlsDueToB

	@RqrmntDtlsDueToB.setter
	def RqrmntDtlsDueToB(self, value):
		self._RqrmntDtlsDueToB = value if type(value) != auto else self.make_default("RqrmntDtlsDueToB")

	@RqrmntDtlsDueToB.deleter
	def RqrmntDtlsDueToB(self):
		del self._RqrmntDtlsDueToB
		self._RqrmntDtlsDueToB = None

	@property
	def XpctdCollDueToA(self):
		return self._XpctdCollDueToA

	@XpctdCollDueToA.setter
	def XpctdCollDueToA(self, value):
		self._XpctdCollDueToA = value if type(value) != auto else self.make_default("XpctdCollDueToA")

	@XpctdCollDueToA.deleter
	def XpctdCollDueToA(self):
		del self._XpctdCollDueToA
		self._XpctdCollDueToA = None

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
	def MrgnCallRslt(self):
		return self._MrgnCallRslt

	@MrgnCallRslt.setter
	def MrgnCallRslt(self, value):
		self._MrgnCallRslt = value if type(value) != auto else self.make_default("MrgnCallRslt")

	@MrgnCallRslt.deleter
	def MrgnCallRslt(self):
		del self._MrgnCallRslt
		self._MrgnCallRslt = None

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
	def XpctdCollDueToB(self):
		return self._XpctdCollDueToB

	@XpctdCollDueToB.setter
	def XpctdCollDueToB(self, value):
		self._XpctdCollDueToB = value if type(value) != auto else self.make_default("XpctdCollDueToB")

	@XpctdCollDueToB.deleter
	def XpctdCollDueToB(self):
		del self._XpctdCollDueToB
		self._XpctdCollDueToB = None

	@property
	def MrgnCallDtls(self):
		return self._MrgnCallDtls

	@MrgnCallDtls.setter
	def MrgnCallDtls(self, value):
		self._MrgnCallDtls = value if type(value) != auto else self.make_default("MrgnCallDtls")

	@MrgnCallDtls.deleter
	def MrgnCallDtls(self):
		del self._MrgnCallDtls
		self._MrgnCallDtls = None

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
		base_types.FieldEntry(name='RqrmntDtlsDueToA', type=MarginRequirement1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='RqrmntDtlsDueToB', type=MarginRequirement1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='XpctdCollDueToA', type=ExpectedCollateral2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Agrmt', type=Agreement4, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MrgnCallRslt', type=MarginCallResult3, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Oblgtn', type=Obligation9, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='XpctdCollDueToB', type=ExpectedCollateral2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MrgnCallDtls', type=MarginCall3, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='MrgnDtlsDueToA', type=MarginCall1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MrgnDtlsDueToB', type=MarginCall1, min=0, max=1, mutex_group=None, array=False),
	))

