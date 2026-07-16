# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CopyDuplicate1Code
from . import ISONormalisedDateTime
from . import Max35Text
from . import Party9Choice

class OriginalMessage1(base_types._BaseFieldType):

	__slots__ = ["_BizMsgIdr", "_CpyDplct", "_CreDt", "_Fr", "_MsgDefIdr", "_To"]
	@property
	def BizMsgIdr(self):
		return self._BizMsgIdr

	@BizMsgIdr.setter
	def BizMsgIdr(self, value):
		self._BizMsgIdr = value if value is not None else base_types.UninitialisedField(self, 'BizMsgIdr', Max35Text, False)

	@BizMsgIdr.deleter
	def BizMsgIdr(self):
		del self._BizMsgIdr
		self._BizMsgIdr = base_types.UninitialisedField(self, 'BizMsgIdr', Max35Text, False)

	@property
	def CpyDplct(self):
		return self._CpyDplct

	@CpyDplct.setter
	def CpyDplct(self, value):
		self._CpyDplct = value if value is not None else base_types.UninitialisedField(self, 'CpyDplct', CopyDuplicate1Code, False)

	@CpyDplct.deleter
	def CpyDplct(self):
		del self._CpyDplct
		self._CpyDplct = base_types.UninitialisedField(self, 'CpyDplct', CopyDuplicate1Code, False)

	@property
	def CreDt(self):
		return self._CreDt

	@CreDt.setter
	def CreDt(self, value):
		self._CreDt = value if value is not None else base_types.UninitialisedField(self, 'CreDt', ISONormalisedDateTime, False)

	@CreDt.deleter
	def CreDt(self):
		del self._CreDt
		self._CreDt = base_types.UninitialisedField(self, 'CreDt', ISONormalisedDateTime, False)

	@property
	def Fr(self):
		return self._Fr

	@Fr.setter
	def Fr(self, value):
		self._Fr = value if value is not None else base_types.UninitialisedField(self, 'Fr', Party9Choice, False)

	@Fr.deleter
	def Fr(self):
		del self._Fr
		self._Fr = base_types.UninitialisedField(self, 'Fr', Party9Choice, False)

	@property
	def MsgDefIdr(self):
		return self._MsgDefIdr

	@MsgDefIdr.setter
	def MsgDefIdr(self, value):
		self._MsgDefIdr = value if value is not None else base_types.UninitialisedField(self, 'MsgDefIdr', Max35Text, False)

	@MsgDefIdr.deleter
	def MsgDefIdr(self):
		del self._MsgDefIdr
		self._MsgDefIdr = base_types.UninitialisedField(self, 'MsgDefIdr', Max35Text, False)

	@property
	def To(self):
		return self._To

	@To.setter
	def To(self, value):
		self._To = value if value is not None else base_types.UninitialisedField(self, 'To', Party9Choice, False)

	@To.deleter
	def To(self):
		del self._To
		self._To = base_types.UninitialisedField(self, 'To', Party9Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='BizMsgIdr', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CpyDplct', type=CopyDuplicate1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CreDt', type=ISONormalisedDateTime, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Fr', type=Party9Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MsgDefIdr', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='To', type=Party9Choice, min=1, max=1, mutex_group=None, array=False),
	))