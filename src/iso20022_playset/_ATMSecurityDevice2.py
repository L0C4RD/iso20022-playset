# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ATMEquipment2
from . import ATMSecurityConfiguration1
from . import ATMStatus2Code
from . import FailureReason5Code
from . import TR34Status1Code

class ATMSecurityDevice2(base_types._BaseFieldType):

	__slots__ = ["_BndgStat", "_CurCfgtn", "_CurSts", "_DvcPrprty", "_Incdnt", "_SpprtdCfgtn"]
	@property
	def BndgStat(self):
		return self._BndgStat

	@BndgStat.setter
	def BndgStat(self, value):
		self._BndgStat = value if value is not None else base_types.UninitialisedField(self, 'BndgStat', TR34Status1Code, False)

	@BndgStat.deleter
	def BndgStat(self):
		del self._BndgStat
		self._BndgStat = base_types.UninitialisedField(self, 'BndgStat', TR34Status1Code, False)

	@property
	def CurCfgtn(self):
		return self._CurCfgtn

	@CurCfgtn.setter
	def CurCfgtn(self, value):
		self._CurCfgtn = value if value is not None else base_types.UninitialisedField(self, 'CurCfgtn', ATMSecurityConfiguration1, False)

	@CurCfgtn.deleter
	def CurCfgtn(self):
		del self._CurCfgtn
		self._CurCfgtn = base_types.UninitialisedField(self, 'CurCfgtn', ATMSecurityConfiguration1, False)

	@property
	def CurSts(self):
		return self._CurSts

	@CurSts.setter
	def CurSts(self, value):
		self._CurSts = value if value is not None else base_types.UninitialisedField(self, 'CurSts', ATMStatus2Code, False)

	@CurSts.deleter
	def CurSts(self):
		del self._CurSts
		self._CurSts = base_types.UninitialisedField(self, 'CurSts', ATMStatus2Code, False)

	@property
	def DvcPrprty(self):
		return self._DvcPrprty

	@DvcPrprty.setter
	def DvcPrprty(self, value):
		self._DvcPrprty = value if value is not None else base_types.UninitialisedField(self, 'DvcPrprty', ATMEquipment2, False)

	@DvcPrprty.deleter
	def DvcPrprty(self):
		del self._DvcPrprty
		self._DvcPrprty = base_types.UninitialisedField(self, 'DvcPrprty', ATMEquipment2, False)

	@property
	def Incdnt(self):
		return self._Incdnt

	@Incdnt.setter
	def Incdnt(self, value):
		self._Incdnt = value if value is not None else base_types.UninitialisedField(self, 'Incdnt', FailureReason5Code, False)

	@Incdnt.deleter
	def Incdnt(self):
		del self._Incdnt
		self._Incdnt = base_types.UninitialisedField(self, 'Incdnt', FailureReason5Code, False)

	@property
	def SpprtdCfgtn(self):
		return self._SpprtdCfgtn

	@SpprtdCfgtn.setter
	def SpprtdCfgtn(self, value):
		self._SpprtdCfgtn = value if value is not None else base_types.UninitialisedField(self, 'SpprtdCfgtn', ATMSecurityConfiguration1, False)

	@SpprtdCfgtn.deleter
	def SpprtdCfgtn(self):
		del self._SpprtdCfgtn
		self._SpprtdCfgtn = base_types.UninitialisedField(self, 'SpprtdCfgtn', ATMSecurityConfiguration1, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='BndgStat', type=TR34Status1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CurCfgtn', type=ATMSecurityConfiguration1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CurSts', type=ATMStatus2Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DvcPrprty', type=ATMEquipment2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Incdnt', type=FailureReason5Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SpprtdCfgtn', type=ATMSecurityConfiguration1, min=0, max=1, mutex_group=None, array=False),
	))