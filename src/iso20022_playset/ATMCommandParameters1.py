import base_types
import Max35Text
import ATMSecurityConfiguration1
import ATMStatus2Code

class ATMCommandParameters1(base_types._BaseFieldType):

	__slots__ = ["_ReqrdSts", "_SrlNb", "_ReqrdCfgtn"]
	@property
	def ReqrdSts(self):
		return self._ReqrdSts

	@ReqrdSts.setter
	def ReqrdSts(self, value):
		self._ReqrdSts = value if type(value) != auto else self.make_default("ReqrdSts")

	@ReqrdSts.deleter
	def ReqrdSts(self):
		del self._ReqrdSts
		self._ReqrdSts = None

	@property
	def SrlNb(self):
		return self._SrlNb

	@SrlNb.setter
	def SrlNb(self, value):
		self._SrlNb = value if type(value) != auto else self.make_default("SrlNb")

	@SrlNb.deleter
	def SrlNb(self):
		del self._SrlNb
		self._SrlNb = None

	@property
	def ReqrdCfgtn(self):
		return self._ReqrdCfgtn

	@ReqrdCfgtn.setter
	def ReqrdCfgtn(self, value):
		self._ReqrdCfgtn = value if type(value) != auto else self.make_default("ReqrdCfgtn")

	@ReqrdCfgtn.deleter
	def ReqrdCfgtn(self):
		del self._ReqrdCfgtn
		self._ReqrdCfgtn = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='ReqrdSts', type=ATMStatus2Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SrlNb', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ReqrdCfgtn', type=ATMSecurityConfiguration1, min=0, max=1, mutex_group=None, array=False),
	))

