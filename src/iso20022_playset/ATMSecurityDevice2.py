import base_types
import ATMStatus2Code
import ATMEquipment2
import TR34Status1Code
import ATMSecurityConfiguration1
import FailureReason5Code

class ATMSecurityDevice2(base_types._BaseFieldType):

	__slots__ = ["_DvcPrprty", "_Incdnt", "_SpprtdCfgtn", "_BndgStat", "_CurSts", "_CurCfgtn"]
	@property
	def DvcPrprty(self):
		return self._DvcPrprty

	@DvcPrprty.setter
	def DvcPrprty(self, value):
		self._DvcPrprty = value if type(value) != auto else self.make_default("DvcPrprty")

	@DvcPrprty.deleter
	def DvcPrprty(self):
		del self._DvcPrprty
		self._DvcPrprty = None

	@property
	def Incdnt(self):
		return self._Incdnt

	@Incdnt.setter
	def Incdnt(self, value):
		self._Incdnt = value if type(value) != auto else self.make_default("Incdnt")

	@Incdnt.deleter
	def Incdnt(self):
		del self._Incdnt
		self._Incdnt = None

	@property
	def SpprtdCfgtn(self):
		return self._SpprtdCfgtn

	@SpprtdCfgtn.setter
	def SpprtdCfgtn(self, value):
		self._SpprtdCfgtn = value if type(value) != auto else self.make_default("SpprtdCfgtn")

	@SpprtdCfgtn.deleter
	def SpprtdCfgtn(self):
		del self._SpprtdCfgtn
		self._SpprtdCfgtn = None

	@property
	def BndgStat(self):
		return self._BndgStat

	@BndgStat.setter
	def BndgStat(self, value):
		self._BndgStat = value if type(value) != auto else self.make_default("BndgStat")

	@BndgStat.deleter
	def BndgStat(self):
		del self._BndgStat
		self._BndgStat = None

	@property
	def CurSts(self):
		return self._CurSts

	@CurSts.setter
	def CurSts(self, value):
		self._CurSts = value if type(value) != auto else self.make_default("CurSts")

	@CurSts.deleter
	def CurSts(self):
		del self._CurSts
		self._CurSts = None

	@property
	def CurCfgtn(self):
		return self._CurCfgtn

	@CurCfgtn.setter
	def CurCfgtn(self, value):
		self._CurCfgtn = value if type(value) != auto else self.make_default("CurCfgtn")

	@CurCfgtn.deleter
	def CurCfgtn(self):
		del self._CurCfgtn
		self._CurCfgtn = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='DvcPrprty', type=ATMEquipment2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Incdnt', type=FailureReason5Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SpprtdCfgtn', type=ATMSecurityConfiguration1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BndgStat', type=TR34Status1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CurSts', type=ATMStatus2Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CurCfgtn', type=ATMSecurityConfiguration1, min=1, max=1, mutex_group=None, array=False),
	))

