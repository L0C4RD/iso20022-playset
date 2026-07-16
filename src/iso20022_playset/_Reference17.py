# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Max35Text

class Reference17(base_types._BaseFieldType):

	__slots__ = ["_CollSbstitnReqId", "_CollSbstitnRspnId"]
	@property
	def CollSbstitnReqId(self):
		return self._CollSbstitnReqId

	@CollSbstitnReqId.setter
	def CollSbstitnReqId(self, value):
		self._CollSbstitnReqId = value if value is not None else base_types.UninitialisedField(self, 'CollSbstitnReqId', Max35Text, False)

	@CollSbstitnReqId.deleter
	def CollSbstitnReqId(self):
		del self._CollSbstitnReqId
		self._CollSbstitnReqId = base_types.UninitialisedField(self, 'CollSbstitnReqId', Max35Text, False)

	@property
	def CollSbstitnRspnId(self):
		return self._CollSbstitnRspnId

	@CollSbstitnRspnId.setter
	def CollSbstitnRspnId(self, value):
		self._CollSbstitnRspnId = value if value is not None else base_types.UninitialisedField(self, 'CollSbstitnRspnId', Max35Text, False)

	@CollSbstitnRspnId.deleter
	def CollSbstitnRspnId(self):
		del self._CollSbstitnRspnId
		self._CollSbstitnRspnId = base_types.UninitialisedField(self, 'CollSbstitnRspnId', Max35Text, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='CollSbstitnReqId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CollSbstitnRspnId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
	))