# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import RequestedIndicator

class StandingOrderReturnCriteria1(base_types._BaseFieldType):

	__slots__ = ["_AssoctdPoolAcct", "_CcyInd", "_CdtrAcctInd", "_DbtrAcctInd", "_ExctnTpInd", "_FrqcyInd", "_LkSetIdInd", "_LkSetOrdrIdInd", "_LkSetOrdrSeqInd", "_RspnsblPtyInd", "_StgOrdrIdInd", "_SysMmbInd", "_TpInd", "_TtlAmtInd", "_VldToInd", "_VldtyFrInd", "_ZeroSweepInd"]
	@property
	def AssoctdPoolAcct(self):
		return self._AssoctdPoolAcct

	@AssoctdPoolAcct.setter
	def AssoctdPoolAcct(self, value):
		self._AssoctdPoolAcct = value if value is not None else base_types.UninitialisedField(self, 'AssoctdPoolAcct', RequestedIndicator, False)

	@AssoctdPoolAcct.deleter
	def AssoctdPoolAcct(self):
		del self._AssoctdPoolAcct
		self._AssoctdPoolAcct = base_types.UninitialisedField(self, 'AssoctdPoolAcct', RequestedIndicator, False)

	@property
	def CcyInd(self):
		return self._CcyInd

	@CcyInd.setter
	def CcyInd(self, value):
		self._CcyInd = value if value is not None else base_types.UninitialisedField(self, 'CcyInd', RequestedIndicator, False)

	@CcyInd.deleter
	def CcyInd(self):
		del self._CcyInd
		self._CcyInd = base_types.UninitialisedField(self, 'CcyInd', RequestedIndicator, False)

	@property
	def CdtrAcctInd(self):
		return self._CdtrAcctInd

	@CdtrAcctInd.setter
	def CdtrAcctInd(self, value):
		self._CdtrAcctInd = value if value is not None else base_types.UninitialisedField(self, 'CdtrAcctInd', RequestedIndicator, False)

	@CdtrAcctInd.deleter
	def CdtrAcctInd(self):
		del self._CdtrAcctInd
		self._CdtrAcctInd = base_types.UninitialisedField(self, 'CdtrAcctInd', RequestedIndicator, False)

	@property
	def DbtrAcctInd(self):
		return self._DbtrAcctInd

	@DbtrAcctInd.setter
	def DbtrAcctInd(self, value):
		self._DbtrAcctInd = value if value is not None else base_types.UninitialisedField(self, 'DbtrAcctInd', RequestedIndicator, False)

	@DbtrAcctInd.deleter
	def DbtrAcctInd(self):
		del self._DbtrAcctInd
		self._DbtrAcctInd = base_types.UninitialisedField(self, 'DbtrAcctInd', RequestedIndicator, False)

	@property
	def ExctnTpInd(self):
		return self._ExctnTpInd

	@ExctnTpInd.setter
	def ExctnTpInd(self, value):
		self._ExctnTpInd = value if value is not None else base_types.UninitialisedField(self, 'ExctnTpInd', RequestedIndicator, False)

	@ExctnTpInd.deleter
	def ExctnTpInd(self):
		del self._ExctnTpInd
		self._ExctnTpInd = base_types.UninitialisedField(self, 'ExctnTpInd', RequestedIndicator, False)

	@property
	def FrqcyInd(self):
		return self._FrqcyInd

	@FrqcyInd.setter
	def FrqcyInd(self, value):
		self._FrqcyInd = value if value is not None else base_types.UninitialisedField(self, 'FrqcyInd', RequestedIndicator, False)

	@FrqcyInd.deleter
	def FrqcyInd(self):
		del self._FrqcyInd
		self._FrqcyInd = base_types.UninitialisedField(self, 'FrqcyInd', RequestedIndicator, False)

	@property
	def LkSetIdInd(self):
		return self._LkSetIdInd

	@LkSetIdInd.setter
	def LkSetIdInd(self, value):
		self._LkSetIdInd = value if value is not None else base_types.UninitialisedField(self, 'LkSetIdInd', RequestedIndicator, False)

	@LkSetIdInd.deleter
	def LkSetIdInd(self):
		del self._LkSetIdInd
		self._LkSetIdInd = base_types.UninitialisedField(self, 'LkSetIdInd', RequestedIndicator, False)

	@property
	def LkSetOrdrIdInd(self):
		return self._LkSetOrdrIdInd

	@LkSetOrdrIdInd.setter
	def LkSetOrdrIdInd(self, value):
		self._LkSetOrdrIdInd = value if value is not None else base_types.UninitialisedField(self, 'LkSetOrdrIdInd', RequestedIndicator, False)

	@LkSetOrdrIdInd.deleter
	def LkSetOrdrIdInd(self):
		del self._LkSetOrdrIdInd
		self._LkSetOrdrIdInd = base_types.UninitialisedField(self, 'LkSetOrdrIdInd', RequestedIndicator, False)

	@property
	def LkSetOrdrSeqInd(self):
		return self._LkSetOrdrSeqInd

	@LkSetOrdrSeqInd.setter
	def LkSetOrdrSeqInd(self, value):
		self._LkSetOrdrSeqInd = value if value is not None else base_types.UninitialisedField(self, 'LkSetOrdrSeqInd', RequestedIndicator, False)

	@LkSetOrdrSeqInd.deleter
	def LkSetOrdrSeqInd(self):
		del self._LkSetOrdrSeqInd
		self._LkSetOrdrSeqInd = base_types.UninitialisedField(self, 'LkSetOrdrSeqInd', RequestedIndicator, False)

	@property
	def RspnsblPtyInd(self):
		return self._RspnsblPtyInd

	@RspnsblPtyInd.setter
	def RspnsblPtyInd(self, value):
		self._RspnsblPtyInd = value if value is not None else base_types.UninitialisedField(self, 'RspnsblPtyInd', RequestedIndicator, False)

	@RspnsblPtyInd.deleter
	def RspnsblPtyInd(self):
		del self._RspnsblPtyInd
		self._RspnsblPtyInd = base_types.UninitialisedField(self, 'RspnsblPtyInd', RequestedIndicator, False)

	@property
	def StgOrdrIdInd(self):
		return self._StgOrdrIdInd

	@StgOrdrIdInd.setter
	def StgOrdrIdInd(self, value):
		self._StgOrdrIdInd = value if value is not None else base_types.UninitialisedField(self, 'StgOrdrIdInd', RequestedIndicator, False)

	@StgOrdrIdInd.deleter
	def StgOrdrIdInd(self):
		del self._StgOrdrIdInd
		self._StgOrdrIdInd = base_types.UninitialisedField(self, 'StgOrdrIdInd', RequestedIndicator, False)

	@property
	def SysMmbInd(self):
		return self._SysMmbInd

	@SysMmbInd.setter
	def SysMmbInd(self, value):
		self._SysMmbInd = value if value is not None else base_types.UninitialisedField(self, 'SysMmbInd', RequestedIndicator, False)

	@SysMmbInd.deleter
	def SysMmbInd(self):
		del self._SysMmbInd
		self._SysMmbInd = base_types.UninitialisedField(self, 'SysMmbInd', RequestedIndicator, False)

	@property
	def TpInd(self):
		return self._TpInd

	@TpInd.setter
	def TpInd(self, value):
		self._TpInd = value if value is not None else base_types.UninitialisedField(self, 'TpInd', RequestedIndicator, False)

	@TpInd.deleter
	def TpInd(self):
		del self._TpInd
		self._TpInd = base_types.UninitialisedField(self, 'TpInd', RequestedIndicator, False)

	@property
	def TtlAmtInd(self):
		return self._TtlAmtInd

	@TtlAmtInd.setter
	def TtlAmtInd(self, value):
		self._TtlAmtInd = value if value is not None else base_types.UninitialisedField(self, 'TtlAmtInd', RequestedIndicator, False)

	@TtlAmtInd.deleter
	def TtlAmtInd(self):
		del self._TtlAmtInd
		self._TtlAmtInd = base_types.UninitialisedField(self, 'TtlAmtInd', RequestedIndicator, False)

	@property
	def VldToInd(self):
		return self._VldToInd

	@VldToInd.setter
	def VldToInd(self, value):
		self._VldToInd = value if value is not None else base_types.UninitialisedField(self, 'VldToInd', RequestedIndicator, False)

	@VldToInd.deleter
	def VldToInd(self):
		del self._VldToInd
		self._VldToInd = base_types.UninitialisedField(self, 'VldToInd', RequestedIndicator, False)

	@property
	def VldtyFrInd(self):
		return self._VldtyFrInd

	@VldtyFrInd.setter
	def VldtyFrInd(self, value):
		self._VldtyFrInd = value if value is not None else base_types.UninitialisedField(self, 'VldtyFrInd', RequestedIndicator, False)

	@VldtyFrInd.deleter
	def VldtyFrInd(self):
		del self._VldtyFrInd
		self._VldtyFrInd = base_types.UninitialisedField(self, 'VldtyFrInd', RequestedIndicator, False)

	@property
	def ZeroSweepInd(self):
		return self._ZeroSweepInd

	@ZeroSweepInd.setter
	def ZeroSweepInd(self, value):
		self._ZeroSweepInd = value if value is not None else base_types.UninitialisedField(self, 'ZeroSweepInd', RequestedIndicator, False)

	@ZeroSweepInd.deleter
	def ZeroSweepInd(self):
		del self._ZeroSweepInd
		self._ZeroSweepInd = base_types.UninitialisedField(self, 'ZeroSweepInd', RequestedIndicator, False)

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