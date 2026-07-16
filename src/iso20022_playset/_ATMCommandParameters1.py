# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ATMSecurityConfiguration1
from . import ATMStatus2Code
from . import Max35Text

class ATMCommandParameters1(base_types._BaseFieldType):

	__slots__ = ["_ReqrdCfgtn", "_ReqrdSts", "_SrlNb"]
	@property
	def ReqrdCfgtn(self):
		return self._ReqrdCfgtn

	@ReqrdCfgtn.setter
	def ReqrdCfgtn(self, value):
		self._ReqrdCfgtn = value if value is not None else base_types.UninitialisedField(self, 'ReqrdCfgtn', ATMSecurityConfiguration1, False)

	@ReqrdCfgtn.deleter
	def ReqrdCfgtn(self):
		del self._ReqrdCfgtn
		self._ReqrdCfgtn = base_types.UninitialisedField(self, 'ReqrdCfgtn', ATMSecurityConfiguration1, False)

	@property
	def ReqrdSts(self):
		return self._ReqrdSts

	@ReqrdSts.setter
	def ReqrdSts(self, value):
		self._ReqrdSts = value if value is not None else base_types.UninitialisedField(self, 'ReqrdSts', ATMStatus2Code, False)

	@ReqrdSts.deleter
	def ReqrdSts(self):
		del self._ReqrdSts
		self._ReqrdSts = base_types.UninitialisedField(self, 'ReqrdSts', ATMStatus2Code, False)

	@property
	def SrlNb(self):
		return self._SrlNb

	@SrlNb.setter
	def SrlNb(self, value):
		self._SrlNb = value if value is not None else base_types.UninitialisedField(self, 'SrlNb', Max35Text, False)

	@SrlNb.deleter
	def SrlNb(self):
		del self._SrlNb
		self._SrlNb = base_types.UninitialisedField(self, 'SrlNb', Max35Text, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='ReqrdCfgtn', type=ATMSecurityConfiguration1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ReqrdSts', type=ATMStatus2Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SrlNb', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
	))