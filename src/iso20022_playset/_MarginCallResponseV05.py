# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AgreedAmount1Choice
from . import Agreement4
from . import MarginCall1
from . import Max35Text
from . import Obligation9
from . import Response1
from . import SupplementaryData1

class MarginCallResponseV05(base_types._BaseFieldType):

	__slots__ = ["_AgrdAmtDueToA", "_AgrdAmtDueToB", "_Agrmt", "_MrgnDtlsDueToA", "_MrgnDtlsDueToB", "_Oblgtn", "_RspnDtls", "_SplmtryData", "_TxId"]
	@property
	def AgrdAmtDueToA(self):
		return self._AgrdAmtDueToA

	@AgrdAmtDueToA.setter
	def AgrdAmtDueToA(self, value):
		self._AgrdAmtDueToA = value if value is not None else base_types.UninitialisedField(self, 'AgrdAmtDueToA', AgreedAmount1Choice, False)

	@AgrdAmtDueToA.deleter
	def AgrdAmtDueToA(self):
		del self._AgrdAmtDueToA
		self._AgrdAmtDueToA = base_types.UninitialisedField(self, 'AgrdAmtDueToA', AgreedAmount1Choice, False)

	@property
	def AgrdAmtDueToB(self):
		return self._AgrdAmtDueToB

	@AgrdAmtDueToB.setter
	def AgrdAmtDueToB(self, value):
		self._AgrdAmtDueToB = value if value is not None else base_types.UninitialisedField(self, 'AgrdAmtDueToB', AgreedAmount1Choice, False)

	@AgrdAmtDueToB.deleter
	def AgrdAmtDueToB(self):
		del self._AgrdAmtDueToB
		self._AgrdAmtDueToB = base_types.UninitialisedField(self, 'AgrdAmtDueToB', AgreedAmount1Choice, False)

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
	def RspnDtls(self):
		return self._RspnDtls

	@RspnDtls.setter
	def RspnDtls(self, value):
		self._RspnDtls = value if value is not None else base_types.UninitialisedField(self, 'RspnDtls', Response1, False)

	@RspnDtls.deleter
	def RspnDtls(self):
		del self._RspnDtls
		self._RspnDtls = base_types.UninitialisedField(self, 'RspnDtls', Response1, False)

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

	_field_defs = frozenset((
		base_types.FieldEntry(name='AgrdAmtDueToA', type=AgreedAmount1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AgrdAmtDueToB', type=AgreedAmount1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Agrmt', type=Agreement4, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MrgnDtlsDueToA', type=MarginCall1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MrgnDtlsDueToB', type=MarginCall1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Oblgtn', type=Obligation9, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RspnDtls', type=Response1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='TxId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
	))