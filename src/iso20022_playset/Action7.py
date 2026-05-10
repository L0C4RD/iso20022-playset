import base_types
import ActionMessage4
import MessageFunction11Code
import ActionType6Code

class Action7(base_types._BaseFieldType):

	__slots__ = ["_ActnTp", "_ReqToPrfrm", "_MsgToPres"]
	@property
	def ActnTp(self):
		return self._ActnTp

	@ActnTp.setter
	def ActnTp(self, value):
		self._ActnTp = value if type(value) != auto else self.make_default("ActnTp")

	@ActnTp.deleter
	def ActnTp(self):
		del self._ActnTp
		self._ActnTp = None

	@property
	def ReqToPrfrm(self):
		return self._ReqToPrfrm

	@ReqToPrfrm.setter
	def ReqToPrfrm(self, value):
		self._ReqToPrfrm = value if type(value) != auto else self.make_default("ReqToPrfrm")

	@ReqToPrfrm.deleter
	def ReqToPrfrm(self):
		del self._ReqToPrfrm
		self._ReqToPrfrm = None

	@property
	def MsgToPres(self):
		return self._MsgToPres

	@MsgToPres.setter
	def MsgToPres(self, value):
		self._MsgToPres = value if type(value) != auto else self.make_default("MsgToPres")

	@MsgToPres.deleter
	def MsgToPres(self):
		del self._MsgToPres
		self._MsgToPres = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='ActnTp', type=ActionType6Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ReqToPrfrm', type=MessageFunction11Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MsgToPres', type=ActionMessage4, min=0, max=1, mutex_group=None, array=False),
	))

