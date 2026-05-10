from . import base_types
from ._Max20000Text import Max20000Text
from ._OutputFormat1Code import OutputFormat1Code

class ActionMessage5(base_types._BaseFieldType):

	__slots__ = ["_MsgCntt", "_Frmt"]
	@property
	def MsgCntt(self):
		return self._MsgCntt

	@MsgCntt.setter
	def MsgCntt(self, value):
		self._MsgCntt = value if type(value) != base_types.auto else self.make_default("MsgCntt")

	@MsgCntt.deleter
	def MsgCntt(self):
		del self._MsgCntt
		self._MsgCntt = None

	@property
	def Frmt(self):
		return self._Frmt

	@Frmt.setter
	def Frmt(self, value):
		self._Frmt = value if type(value) != base_types.auto else self.make_default("Frmt")

	@Frmt.deleter
	def Frmt(self):
		del self._Frmt
		self._Frmt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='MsgCntt', type=Max20000Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Frmt', type=OutputFormat1Code, min=0, max=1, mutex_group=None, array=False),
	))

