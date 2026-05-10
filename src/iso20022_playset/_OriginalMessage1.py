from . import base_types
from ._ISONormalisedDateTime import ISONormalisedDateTime
from ._Party9Choice import Party9Choice
from ._Max35Text import Max35Text
from ._CopyDuplicate1Code import CopyDuplicate1Code

class OriginalMessage1(base_types._BaseFieldType):

	__slots__ = ["_MsgDefIdr", "_CpyDplct", "_To", "_CreDt", "_Fr", "_BizMsgIdr"]
	@property
	def BizMsgIdr(self):
		return self._BizMsgIdr

	@BizMsgIdr.setter
	def BizMsgIdr(self, value):
		self._BizMsgIdr = value if type(value) != base_types.auto else self.make_default("BizMsgIdr")

	@BizMsgIdr.deleter
	def BizMsgIdr(self):
		del self._BizMsgIdr
		self._BizMsgIdr = None

	@property
	def CpyDplct(self):
		return self._CpyDplct

	@CpyDplct.setter
	def CpyDplct(self, value):
		self._CpyDplct = value if type(value) != base_types.auto else self.make_default("CpyDplct")

	@CpyDplct.deleter
	def CpyDplct(self):
		del self._CpyDplct
		self._CpyDplct = None

	@property
	def CreDt(self):
		return self._CreDt

	@CreDt.setter
	def CreDt(self, value):
		self._CreDt = value if type(value) != base_types.auto else self.make_default("CreDt")

	@CreDt.deleter
	def CreDt(self):
		del self._CreDt
		self._CreDt = None

	@property
	def Fr(self):
		return self._Fr

	@Fr.setter
	def Fr(self, value):
		self._Fr = value if type(value) != base_types.auto else self.make_default("Fr")

	@Fr.deleter
	def Fr(self):
		del self._Fr
		self._Fr = None

	@property
	def MsgDefIdr(self):
		return self._MsgDefIdr

	@MsgDefIdr.setter
	def MsgDefIdr(self, value):
		self._MsgDefIdr = value if type(value) != base_types.auto else self.make_default("MsgDefIdr")

	@MsgDefIdr.deleter
	def MsgDefIdr(self):
		del self._MsgDefIdr
		self._MsgDefIdr = None

	@property
	def To(self):
		return self._To

	@To.setter
	def To(self, value):
		self._To = value if type(value) != base_types.auto else self.make_default("To")

	@To.deleter
	def To(self):
		del self._To
		self._To = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='BizMsgIdr', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CpyDplct', type=CopyDuplicate1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CreDt', type=ISONormalisedDateTime, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Fr', type=Party9Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MsgDefIdr', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='To', type=Party9Choice, min=1, max=1, mutex_group=None, array=False),
	))

