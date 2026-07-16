# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Agreement4
from . import ExpectedCollateral2Choice
from . import MarginCall1
from . import MarginCall3
from . import MarginCallResult3
from . import MarginRequirement1Choice
from . import Max35Text
from . import Obligation9
from . import SupplementaryData1

class MarginCallRequestV05(base_types._BaseFieldType):

	__slots__ = ["_Agrmt", "_MrgnCallDtls", "_MrgnCallRslt", "_MrgnDtlsDueToA", "_MrgnDtlsDueToB", "_Oblgtn", "_RqrmntDtlsDueToA", "_RqrmntDtlsDueToB", "_SplmtryData", "_TxId", "_XpctdCollDueToA", "_XpctdCollDueToB"]
	@property
	def Agrmt(self):
		return self._Agrmt

	@Agrmt.setter
	def Agrmt(self, value):
		self._Agrmt = value if value is not None else base_types.UninitialisedField(self, 'Agrmt', Agreement4, False)

	@Agrmt.deleter
	def Agrmt(self):
		del self._Agrmt
		self._Agrmt = base_types.UninitialisedField(self, 'Agrmt', Agreement4, False)

	@property
	def MrgnCallDtls(self):
		return self._MrgnCallDtls

	@MrgnCallDtls.setter
	def MrgnCallDtls(self, value):
		self._MrgnCallDtls = value if value is not None else base_types.UninitialisedField(self, 'MrgnCallDtls', MarginCall3, True)

	@MrgnCallDtls.deleter
	def MrgnCallDtls(self):
		del self._MrgnCallDtls
		self._MrgnCallDtls = base_types.UninitialisedField(self, 'MrgnCallDtls', MarginCall3, True)

	@property
	def MrgnCallRslt(self):
		return self._MrgnCallRslt

	@MrgnCallRslt.setter
	def MrgnCallRslt(self, value):
		self._MrgnCallRslt = value if value is not None else base_types.UninitialisedField(self, 'MrgnCallRslt', MarginCallResult3, False)

	@MrgnCallRslt.deleter
	def MrgnCallRslt(self):
		del self._MrgnCallRslt
		self._MrgnCallRslt = base_types.UninitialisedField(self, 'MrgnCallRslt', MarginCallResult3, False)

	@property
	def MrgnDtlsDueToA(self):
		return self._MrgnDtlsDueToA

	@MrgnDtlsDueToA.setter
	def MrgnDtlsDueToA(self, value):
		self._MrgnDtlsDueToA = value if value is not None else base_types.UninitialisedField(self, 'MrgnDtlsDueToA', MarginCall1, False)

	@MrgnDtlsDueToA.deleter
	def MrgnDtlsDueToA(self):
		del self._MrgnDtlsDueToA
		self._MrgnDtlsDueToA = base_types.UninitialisedField(self, 'MrgnDtlsDueToA', MarginCall1, False)

	@property
	def MrgnDtlsDueToB(self):
		return self._MrgnDtlsDueToB

	@MrgnDtlsDueToB.setter
	def MrgnDtlsDueToB(self, value):
		self._MrgnDtlsDueToB = value if value is not None else base_types.UninitialisedField(self, 'MrgnDtlsDueToB', MarginCall1, False)

	@MrgnDtlsDueToB.deleter
	def MrgnDtlsDueToB(self):
		del self._MrgnDtlsDueToB
		self._MrgnDtlsDueToB = base_types.UninitialisedField(self, 'MrgnDtlsDueToB', MarginCall1, False)

	@property
	def Oblgtn(self):
		return self._Oblgtn

	@Oblgtn.setter
	def Oblgtn(self, value):
		self._Oblgtn = value if value is not None else base_types.UninitialisedField(self, 'Oblgtn', Obligation9, False)

	@Oblgtn.deleter
	def Oblgtn(self):
		del self._Oblgtn
		self._Oblgtn = base_types.UninitialisedField(self, 'Oblgtn', Obligation9, False)

	@property
	def RqrmntDtlsDueToA(self):
		return self._RqrmntDtlsDueToA

	@RqrmntDtlsDueToA.setter
	def RqrmntDtlsDueToA(self, value):
		self._RqrmntDtlsDueToA = value if value is not None else base_types.UninitialisedField(self, 'RqrmntDtlsDueToA', MarginRequirement1Choice, False)

	@RqrmntDtlsDueToA.deleter
	def RqrmntDtlsDueToA(self):
		del self._RqrmntDtlsDueToA
		self._RqrmntDtlsDueToA = base_types.UninitialisedField(self, 'RqrmntDtlsDueToA', MarginRequirement1Choice, False)

	@property
	def RqrmntDtlsDueToB(self):
		return self._RqrmntDtlsDueToB

	@RqrmntDtlsDueToB.setter
	def RqrmntDtlsDueToB(self, value):
		self._RqrmntDtlsDueToB = value if value is not None else base_types.UninitialisedField(self, 'RqrmntDtlsDueToB', MarginRequirement1Choice, False)

	@RqrmntDtlsDueToB.deleter
	def RqrmntDtlsDueToB(self):
		del self._RqrmntDtlsDueToB
		self._RqrmntDtlsDueToB = base_types.UninitialisedField(self, 'RqrmntDtlsDueToB', MarginRequirement1Choice, False)

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
	def TxId(self):
		return self._TxId

	@TxId.setter
	def TxId(self, value):
		self._TxId = value if value is not None else base_types.UninitialisedField(self, 'TxId', Max35Text, False)

	@TxId.deleter
	def TxId(self):
		del self._TxId
		self._TxId = base_types.UninitialisedField(self, 'TxId', Max35Text, False)

	@property
	def XpctdCollDueToA(self):
		return self._XpctdCollDueToA

	@XpctdCollDueToA.setter
	def XpctdCollDueToA(self, value):
		self._XpctdCollDueToA = value if value is not None else base_types.UninitialisedField(self, 'XpctdCollDueToA', ExpectedCollateral2Choice, False)

	@XpctdCollDueToA.deleter
	def XpctdCollDueToA(self):
		del self._XpctdCollDueToA
		self._XpctdCollDueToA = base_types.UninitialisedField(self, 'XpctdCollDueToA', ExpectedCollateral2Choice, False)

	@property
	def XpctdCollDueToB(self):
		return self._XpctdCollDueToB

	@XpctdCollDueToB.setter
	def XpctdCollDueToB(self, value):
		self._XpctdCollDueToB = value if value is not None else base_types.UninitialisedField(self, 'XpctdCollDueToB', ExpectedCollateral2Choice, False)

	@XpctdCollDueToB.deleter
	def XpctdCollDueToB(self):
		del self._XpctdCollDueToB
		self._XpctdCollDueToB = base_types.UninitialisedField(self, 'XpctdCollDueToB', ExpectedCollateral2Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Agrmt', type=Agreement4, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MrgnCallDtls', type=MarginCall3, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='MrgnCallRslt', type=MarginCallResult3, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MrgnDtlsDueToA', type=MarginCall1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MrgnDtlsDueToB', type=MarginCall1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Oblgtn', type=Obligation9, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RqrmntDtlsDueToA', type=MarginRequirement1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RqrmntDtlsDueToB', type=MarginRequirement1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='TxId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='XpctdCollDueToA', type=ExpectedCollateral2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='XpctdCollDueToB', type=ExpectedCollateral2Choice, min=0, max=1, mutex_group=None, array=False),
	))