# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActionMessage4
from . import ActionType6Code
from . import MessageFunction11Code

class Action7(base_types._BaseFieldType):

	__slots__ = ["_ActnTp", "_MsgToPres", "_ReqToPrfrm"]
	@property
	def ActnTp(self):
		return self._ActnTp

	@ActnTp.setter
	def ActnTp(self, value):
		self._ActnTp = value if value is not None else base_types.UninitialisedField(self, 'ActnTp', ActionType6Code, False)

	@ActnTp.deleter
	def ActnTp(self):
		del self._ActnTp
		self._ActnTp = base_types.UninitialisedField(self, 'ActnTp', ActionType6Code, False)

	@property
	def MsgToPres(self):
		return self._MsgToPres

	@MsgToPres.setter
	def MsgToPres(self, value):
		self._MsgToPres = value if value is not None else base_types.UninitialisedField(self, 'MsgToPres', ActionMessage4, False)

	@MsgToPres.deleter
	def MsgToPres(self):
		del self._MsgToPres
		self._MsgToPres = base_types.UninitialisedField(self, 'MsgToPres', ActionMessage4, False)

	@property
	def ReqToPrfrm(self):
		return self._ReqToPrfrm

	@ReqToPrfrm.setter
	def ReqToPrfrm(self, value):
		self._ReqToPrfrm = value if value is not None else base_types.UninitialisedField(self, 'ReqToPrfrm', MessageFunction11Code, False)

	@ReqToPrfrm.deleter
	def ReqToPrfrm(self):
		del self._ReqToPrfrm
		self._ReqToPrfrm = base_types.UninitialisedField(self, 'ReqToPrfrm', MessageFunction11Code, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='ActnTp', type=ActionType6Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MsgToPres', type=ActionMessage4, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ReqToPrfrm', type=MessageFunction11Code, min=0, max=1, mutex_group=None, array=False),
	))