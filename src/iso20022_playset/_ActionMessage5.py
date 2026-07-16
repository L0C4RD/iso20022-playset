# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Max20000Text
from . import OutputFormat1Code

class ActionMessage5(base_types._BaseFieldType):

	__slots__ = ["_Frmt", "_MsgCntt"]
	@property
	def Frmt(self):
		return self._Frmt

	@Frmt.setter
	def Frmt(self, value):
		self._Frmt = value if value is not None else base_types.UninitialisedField(self, 'Frmt', OutputFormat1Code, False)

	@Frmt.deleter
	def Frmt(self):
		del self._Frmt
		self._Frmt = base_types.UninitialisedField(self, 'Frmt', OutputFormat1Code, False)

	@property
	def MsgCntt(self):
		return self._MsgCntt

	@MsgCntt.setter
	def MsgCntt(self, value):
		self._MsgCntt = value if value is not None else base_types.UninitialisedField(self, 'MsgCntt', Max20000Text, False)

	@MsgCntt.deleter
	def MsgCntt(self):
		del self._MsgCntt
		self._MsgCntt = base_types.UninitialisedField(self, 'MsgCntt', Max20000Text, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Frmt', type=OutputFormat1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MsgCntt', type=Max20000Text, min=1, max=1, mutex_group=None, array=False),
	))