# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Max1Number
from . import OtherTargetMarketRiskTolerance1
from . import RiskLevel1Code
from . import TargetMarket2Code

class RiskTolerance1(base_types._BaseFieldType):

	__slots__ = ["_NotForInvstrsWthTheLwstRskTlrnceDE", "_Othr", "_RskTlrnceForNonPRIIPSAndNonUCITSES", "_RskTlrnceIntl", "_RskTlrncePRIIPSMthdlgy", "_RskTlrnceUCITSMthdlgy"]
	@property
	def NotForInvstrsWthTheLwstRskTlrnceDE(self):
		return self._NotForInvstrsWthTheLwstRskTlrnceDE

	@NotForInvstrsWthTheLwstRskTlrnceDE.setter
	def NotForInvstrsWthTheLwstRskTlrnceDE(self, value):
		self._NotForInvstrsWthTheLwstRskTlrnceDE = value if value is not None else base_types.UninitialisedField(self, 'NotForInvstrsWthTheLwstRskTlrnceDE', TargetMarket2Code, False)

	@NotForInvstrsWthTheLwstRskTlrnceDE.deleter
	def NotForInvstrsWthTheLwstRskTlrnceDE(self):
		del self._NotForInvstrsWthTheLwstRskTlrnceDE
		self._NotForInvstrsWthTheLwstRskTlrnceDE = base_types.UninitialisedField(self, 'NotForInvstrsWthTheLwstRskTlrnceDE', TargetMarket2Code, False)

	@property
	def Othr(self):
		return self._Othr

	@Othr.setter
	def Othr(self, value):
		self._Othr = value if value is not None else base_types.UninitialisedField(self, 'Othr', OtherTargetMarketRiskTolerance1, True)

	@Othr.deleter
	def Othr(self):
		del self._Othr
		self._Othr = base_types.UninitialisedField(self, 'Othr', OtherTargetMarketRiskTolerance1, True)

	@property
	def RskTlrnceForNonPRIIPSAndNonUCITSES(self):
		return self._RskTlrnceForNonPRIIPSAndNonUCITSES

	@RskTlrnceForNonPRIIPSAndNonUCITSES.setter
	def RskTlrnceForNonPRIIPSAndNonUCITSES(self, value):
		self._RskTlrnceForNonPRIIPSAndNonUCITSES = value if value is not None else base_types.UninitialisedField(self, 'RskTlrnceForNonPRIIPSAndNonUCITSES', Max1Number, False)

	@RskTlrnceForNonPRIIPSAndNonUCITSES.deleter
	def RskTlrnceForNonPRIIPSAndNonUCITSES(self):
		del self._RskTlrnceForNonPRIIPSAndNonUCITSES
		self._RskTlrnceForNonPRIIPSAndNonUCITSES = base_types.UninitialisedField(self, 'RskTlrnceForNonPRIIPSAndNonUCITSES', Max1Number, False)

	@property
	def RskTlrnceIntl(self):
		return self._RskTlrnceIntl

	@RskTlrnceIntl.setter
	def RskTlrnceIntl(self, value):
		self._RskTlrnceIntl = value if value is not None else base_types.UninitialisedField(self, 'RskTlrnceIntl', RiskLevel1Code, False)

	@RskTlrnceIntl.deleter
	def RskTlrnceIntl(self):
		del self._RskTlrnceIntl
		self._RskTlrnceIntl = base_types.UninitialisedField(self, 'RskTlrnceIntl', RiskLevel1Code, False)

	@property
	def RskTlrncePRIIPSMthdlgy(self):
		return self._RskTlrncePRIIPSMthdlgy

	@RskTlrncePRIIPSMthdlgy.setter
	def RskTlrncePRIIPSMthdlgy(self, value):
		self._RskTlrncePRIIPSMthdlgy = value if value is not None else base_types.UninitialisedField(self, 'RskTlrncePRIIPSMthdlgy', Max1Number, False)

	@RskTlrncePRIIPSMthdlgy.deleter
	def RskTlrncePRIIPSMthdlgy(self):
		del self._RskTlrncePRIIPSMthdlgy
		self._RskTlrncePRIIPSMthdlgy = base_types.UninitialisedField(self, 'RskTlrncePRIIPSMthdlgy', Max1Number, False)

	@property
	def RskTlrnceUCITSMthdlgy(self):
		return self._RskTlrnceUCITSMthdlgy

	@RskTlrnceUCITSMthdlgy.setter
	def RskTlrnceUCITSMthdlgy(self, value):
		self._RskTlrnceUCITSMthdlgy = value if value is not None else base_types.UninitialisedField(self, 'RskTlrnceUCITSMthdlgy', Max1Number, False)

	@RskTlrnceUCITSMthdlgy.deleter
	def RskTlrnceUCITSMthdlgy(self):
		del self._RskTlrnceUCITSMthdlgy
		self._RskTlrnceUCITSMthdlgy = base_types.UninitialisedField(self, 'RskTlrnceUCITSMthdlgy', Max1Number, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='NotForInvstrsWthTheLwstRskTlrnceDE', type=TargetMarket2Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Othr', type=OtherTargetMarketRiskTolerance1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='RskTlrnceForNonPRIIPSAndNonUCITSES', type=Max1Number, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RskTlrnceIntl', type=RiskLevel1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RskTlrncePRIIPSMthdlgy', type=Max1Number, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RskTlrnceUCITSMthdlgy', type=Max1Number, min=0, max=1, mutex_group=None, array=False),
	))