# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Max35Text

class Reference20(base_types._BaseFieldType):

	__slots__ = ["_IntrstPmtReqId", "_IntrstPmtRspnId"]
	@property
	def IntrstPmtReqId(self):
		return self._IntrstPmtReqId

	@IntrstPmtReqId.setter
	def IntrstPmtReqId(self, value):
		self._IntrstPmtReqId = value if value is not None else base_types.UninitialisedField(self, 'IntrstPmtReqId', Max35Text, False)

	@IntrstPmtReqId.deleter
	def IntrstPmtReqId(self):
		del self._IntrstPmtReqId
		self._IntrstPmtReqId = base_types.UninitialisedField(self, 'IntrstPmtReqId', Max35Text, False)

	@property
	def IntrstPmtRspnId(self):
		return self._IntrstPmtRspnId

	@IntrstPmtRspnId.setter
	def IntrstPmtRspnId(self, value):
		self._IntrstPmtRspnId = value if value is not None else base_types.UninitialisedField(self, 'IntrstPmtRspnId', Max35Text, False)

	@IntrstPmtRspnId.deleter
	def IntrstPmtRspnId(self):
		del self._IntrstPmtRspnId
		self._IntrstPmtRspnId = base_types.UninitialisedField(self, 'IntrstPmtRspnId', Max35Text, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='IntrstPmtReqId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IntrstPmtRspnId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
	))