from . import base_types
import Max35Text

class Reference16(base_types._BaseFieldType):

	__slots__ = ["_CollMsgCxlReqId"]
	@property
	def CollMsgCxlReqId(self):
		return self._CollMsgCxlReqId

	@CollMsgCxlReqId.setter
	def CollMsgCxlReqId(self, value):
		self._CollMsgCxlReqId = value if type(value) != auto else self.make_default("CollMsgCxlReqId")

	@CollMsgCxlReqId.deleter
	def CollMsgCxlReqId(self):
		del self._CollMsgCxlReqId
		self._CollMsgCxlReqId = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='CollMsgCxlReqId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
	))

