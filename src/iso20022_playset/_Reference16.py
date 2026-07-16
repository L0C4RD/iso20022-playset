# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Max35Text

class Reference16(base_types._BaseFieldType):

	__slots__ = ["_CollMsgCxlReqId"]
	@property
	def CollMsgCxlReqId(self):
		return self._CollMsgCxlReqId

	@CollMsgCxlReqId.setter
	def CollMsgCxlReqId(self, value):
		self._CollMsgCxlReqId = value if value is not None else base_types.UninitialisedField(self, 'CollMsgCxlReqId', Max35Text, False)

	@CollMsgCxlReqId.deleter
	def CollMsgCxlReqId(self):
		del self._CollMsgCxlReqId
		self._CollMsgCxlReqId = base_types.UninitialisedField(self, 'CollMsgCxlReqId', Max35Text, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='CollMsgCxlReqId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
	))