from . import base_types
from .RiskLevel1Code import RiskLevel1Code
from .OtherTargetMarketRiskTolerance1 import OtherTargetMarketRiskTolerance1
from .TargetMarket2Code import TargetMarket2Code
from .Max1Number import Max1Number

class RiskTolerance1(base_types._BaseFieldType):

	__slots__ = ["_Othr", "_RskTlrnceUCITSMthdlgy", "_RskTlrncePRIIPSMthdlgy", "_NotForInvstrsWthTheLwstRskTlrnceDE", "_RskTlrnceIntl", "_RskTlrnceForNonPRIIPSAndNonUCITSES"]
	@property
	def Othr(self):
		return self._Othr

	@Othr.setter
	def Othr(self, value):
		self._Othr = value if type(value) != auto else self.make_default("Othr")

	@Othr.deleter
	def Othr(self):
		del self._Othr
		self._Othr = None

	@property
	def RskTlrnceUCITSMthdlgy(self):
		return self._RskTlrnceUCITSMthdlgy

	@RskTlrnceUCITSMthdlgy.setter
	def RskTlrnceUCITSMthdlgy(self, value):
		self._RskTlrnceUCITSMthdlgy = value if type(value) != auto else self.make_default("RskTlrnceUCITSMthdlgy")

	@RskTlrnceUCITSMthdlgy.deleter
	def RskTlrnceUCITSMthdlgy(self):
		del self._RskTlrnceUCITSMthdlgy
		self._RskTlrnceUCITSMthdlgy = None

	@property
	def RskTlrncePRIIPSMthdlgy(self):
		return self._RskTlrncePRIIPSMthdlgy

	@RskTlrncePRIIPSMthdlgy.setter
	def RskTlrncePRIIPSMthdlgy(self, value):
		self._RskTlrncePRIIPSMthdlgy = value if type(value) != auto else self.make_default("RskTlrncePRIIPSMthdlgy")

	@RskTlrncePRIIPSMthdlgy.deleter
	def RskTlrncePRIIPSMthdlgy(self):
		del self._RskTlrncePRIIPSMthdlgy
		self._RskTlrncePRIIPSMthdlgy = None

	@property
	def NotForInvstrsWthTheLwstRskTlrnceDE(self):
		return self._NotForInvstrsWthTheLwstRskTlrnceDE

	@NotForInvstrsWthTheLwstRskTlrnceDE.setter
	def NotForInvstrsWthTheLwstRskTlrnceDE(self, value):
		self._NotForInvstrsWthTheLwstRskTlrnceDE = value if type(value) != auto else self.make_default("NotForInvstrsWthTheLwstRskTlrnceDE")

	@NotForInvstrsWthTheLwstRskTlrnceDE.deleter
	def NotForInvstrsWthTheLwstRskTlrnceDE(self):
		del self._NotForInvstrsWthTheLwstRskTlrnceDE
		self._NotForInvstrsWthTheLwstRskTlrnceDE = None

	@property
	def RskTlrnceIntl(self):
		return self._RskTlrnceIntl

	@RskTlrnceIntl.setter
	def RskTlrnceIntl(self, value):
		self._RskTlrnceIntl = value if type(value) != auto else self.make_default("RskTlrnceIntl")

	@RskTlrnceIntl.deleter
	def RskTlrnceIntl(self):
		del self._RskTlrnceIntl
		self._RskTlrnceIntl = None

	@property
	def RskTlrnceForNonPRIIPSAndNonUCITSES(self):
		return self._RskTlrnceForNonPRIIPSAndNonUCITSES

	@RskTlrnceForNonPRIIPSAndNonUCITSES.setter
	def RskTlrnceForNonPRIIPSAndNonUCITSES(self, value):
		self._RskTlrnceForNonPRIIPSAndNonUCITSES = value if type(value) != auto else self.make_default("RskTlrnceForNonPRIIPSAndNonUCITSES")

	@RskTlrnceForNonPRIIPSAndNonUCITSES.deleter
	def RskTlrnceForNonPRIIPSAndNonUCITSES(self):
		del self._RskTlrnceForNonPRIIPSAndNonUCITSES
		self._RskTlrnceForNonPRIIPSAndNonUCITSES = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Othr', type=OtherTargetMarketRiskTolerance1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='RskTlrnceUCITSMthdlgy', type=Max1Number, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RskTlrncePRIIPSMthdlgy', type=Max1Number, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NotForInvstrsWthTheLwstRskTlrnceDE', type=TargetMarket2Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RskTlrnceIntl', type=RiskLevel1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RskTlrnceForNonPRIIPSAndNonUCITSES', type=Max1Number, min=0, max=1, mutex_group=None, array=False),
	))

