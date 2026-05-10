from . import base_types
from ._RequestedIndicator import RequestedIndicator

class StandingOrderReturnCriteria1(base_types._BaseFieldType):

	__slots__ = ["_AssoctdPoolAcct", "_CcyInd", "_CdtrAcctInd", "_DbtrAcctInd", "_ExctnTpInd", "_FrqcyInd", "_LkSetIdInd", "_LkSetOrdrIdInd", "_LkSetOrdrSeqInd", "_RspnsblPtyInd", "_StgOrdrIdInd", "_SysMmbInd", "_TpInd", "_TtlAmtInd", "_VldToInd", "_VldtyFrInd", "_ZeroSweepInd"]
	@property
	def AssoctdPoolAcct(self):
		return self._AssoctdPoolAcct

	@AssoctdPoolAcct.setter
	def AssoctdPoolAcct(self, value):
		self._AssoctdPoolAcct = value if type(value) != base_types.auto else self.make_default("AssoctdPoolAcct")

	@AssoctdPoolAcct.deleter
	def AssoctdPoolAcct(self):
		del self._AssoctdPoolAcct
		self._AssoctdPoolAcct = None

	@property
	def CcyInd(self):
		return self._CcyInd

	@CcyInd.setter
	def CcyInd(self, value):
		self._CcyInd = value if type(value) != base_types.auto else self.make_default("CcyInd")

	@CcyInd.deleter
	def CcyInd(self):
		del self._CcyInd
		self._CcyInd = None

	@property
	def CdtrAcctInd(self):
		return self._CdtrAcctInd

	@CdtrAcctInd.setter
	def CdtrAcctInd(self, value):
		self._CdtrAcctInd = value if type(value) != base_types.auto else self.make_default("CdtrAcctInd")

	@CdtrAcctInd.deleter
	def CdtrAcctInd(self):
		del self._CdtrAcctInd
		self._CdtrAcctInd = None

	@property
	def DbtrAcctInd(self):
		return self._DbtrAcctInd

	@DbtrAcctInd.setter
	def DbtrAcctInd(self, value):
		self._DbtrAcctInd = value if type(value) != base_types.auto else self.make_default("DbtrAcctInd")

	@DbtrAcctInd.deleter
	def DbtrAcctInd(self):
		del self._DbtrAcctInd
		self._DbtrAcctInd = None

	@property
	def ExctnTpInd(self):
		return self._ExctnTpInd

	@ExctnTpInd.setter
	def ExctnTpInd(self, value):
		self._ExctnTpInd = value if type(value) != base_types.auto else self.make_default("ExctnTpInd")

	@ExctnTpInd.deleter
	def ExctnTpInd(self):
		del self._ExctnTpInd
		self._ExctnTpInd = None

	@property
	def FrqcyInd(self):
		return self._FrqcyInd

	@FrqcyInd.setter
	def FrqcyInd(self, value):
		self._FrqcyInd = value if type(value) != base_types.auto else self.make_default("FrqcyInd")

	@FrqcyInd.deleter
	def FrqcyInd(self):
		del self._FrqcyInd
		self._FrqcyInd = None

	@property
	def LkSetIdInd(self):
		return self._LkSetIdInd

	@LkSetIdInd.setter
	def LkSetIdInd(self, value):
		self._LkSetIdInd = value if type(value) != base_types.auto else self.make_default("LkSetIdInd")

	@LkSetIdInd.deleter
	def LkSetIdInd(self):
		del self._LkSetIdInd
		self._LkSetIdInd = None

	@property
	def LkSetOrdrIdInd(self):
		return self._LkSetOrdrIdInd

	@LkSetOrdrIdInd.setter
	def LkSetOrdrIdInd(self, value):
		self._LkSetOrdrIdInd = value if type(value) != base_types.auto else self.make_default("LkSetOrdrIdInd")

	@LkSetOrdrIdInd.deleter
	def LkSetOrdrIdInd(self):
		del self._LkSetOrdrIdInd
		self._LkSetOrdrIdInd = None

	@property
	def LkSetOrdrSeqInd(self):
		return self._LkSetOrdrSeqInd

	@LkSetOrdrSeqInd.setter
	def LkSetOrdrSeqInd(self, value):
		self._LkSetOrdrSeqInd = value if type(value) != base_types.auto else self.make_default("LkSetOrdrSeqInd")

	@LkSetOrdrSeqInd.deleter
	def LkSetOrdrSeqInd(self):
		del self._LkSetOrdrSeqInd
		self._LkSetOrdrSeqInd = None

	@property
	def RspnsblPtyInd(self):
		return self._RspnsblPtyInd

	@RspnsblPtyInd.setter
	def RspnsblPtyInd(self, value):
		self._RspnsblPtyInd = value if type(value) != base_types.auto else self.make_default("RspnsblPtyInd")

	@RspnsblPtyInd.deleter
	def RspnsblPtyInd(self):
		del self._RspnsblPtyInd
		self._RspnsblPtyInd = None

	@property
	def StgOrdrIdInd(self):
		return self._StgOrdrIdInd

	@StgOrdrIdInd.setter
	def StgOrdrIdInd(self, value):
		self._StgOrdrIdInd = value if type(value) != base_types.auto else self.make_default("StgOrdrIdInd")

	@StgOrdrIdInd.deleter
	def StgOrdrIdInd(self):
		del self._StgOrdrIdInd
		self._StgOrdrIdInd = None

	@property
	def SysMmbInd(self):
		return self._SysMmbInd

	@SysMmbInd.setter
	def SysMmbInd(self, value):
		self._SysMmbInd = value if type(value) != base_types.auto else self.make_default("SysMmbInd")

	@SysMmbInd.deleter
	def SysMmbInd(self):
		del self._SysMmbInd
		self._SysMmbInd = None

	@property
	def TpInd(self):
		return self._TpInd

	@TpInd.setter
	def TpInd(self, value):
		self._TpInd = value if type(value) != base_types.auto else self.make_default("TpInd")

	@TpInd.deleter
	def TpInd(self):
		del self._TpInd
		self._TpInd = None

	@property
	def TtlAmtInd(self):
		return self._TtlAmtInd

	@TtlAmtInd.setter
	def TtlAmtInd(self, value):
		self._TtlAmtInd = value if type(value) != base_types.auto else self.make_default("TtlAmtInd")

	@TtlAmtInd.deleter
	def TtlAmtInd(self):
		del self._TtlAmtInd
		self._TtlAmtInd = None

	@property
	def VldToInd(self):
		return self._VldToInd

	@VldToInd.setter
	def VldToInd(self, value):
		self._VldToInd = value if type(value) != base_types.auto else self.make_default("VldToInd")

	@VldToInd.deleter
	def VldToInd(self):
		del self._VldToInd
		self._VldToInd = None

	@property
	def VldtyFrInd(self):
		return self._VldtyFrInd

	@VldtyFrInd.setter
	def VldtyFrInd(self, value):
		self._VldtyFrInd = value if type(value) != base_types.auto else self.make_default("VldtyFrInd")

	@VldtyFrInd.deleter
	def VldtyFrInd(self):
		del self._VldtyFrInd
		self._VldtyFrInd = None

	@property
	def ZeroSweepInd(self):
		return self._ZeroSweepInd

	@ZeroSweepInd.setter
	def ZeroSweepInd(self, value):
		self._ZeroSweepInd = value if type(value) != base_types.auto else self.make_default("ZeroSweepInd")

	@ZeroSweepInd.deleter
	def ZeroSweepInd(self):
		del self._ZeroSweepInd
		self._ZeroSweepInd = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AssoctdPoolAcct', type=RequestedIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CcyInd', type=RequestedIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CdtrAcctInd', type=RequestedIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DbtrAcctInd', type=RequestedIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ExctnTpInd', type=RequestedIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FrqcyInd', type=RequestedIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LkSetIdInd', type=RequestedIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LkSetOrdrIdInd', type=RequestedIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LkSetOrdrSeqInd', type=RequestedIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RspnsblPtyInd', type=RequestedIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StgOrdrIdInd', type=RequestedIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SysMmbInd', type=RequestedIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TpInd', type=RequestedIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlAmtInd', type=RequestedIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='VldToInd', type=RequestedIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='VldtyFrInd', type=RequestedIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ZeroSweepInd', type=RequestedIndicator, min=0, max=1, mutex_group=None, array=False),
	))

