# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import UndertakingAmendmentResponseMessage1

class Amendment9(base_types._BaseFieldType):

	__slots__ = ["_UdrtkgAmdmntRspnMsg"]
	@property
	def UdrtkgAmdmntRspnMsg(self):
		return self._UdrtkgAmdmntRspnMsg

	@UdrtkgAmdmntRspnMsg.setter
	def UdrtkgAmdmntRspnMsg(self, value):
		self._UdrtkgAmdmntRspnMsg = value if value is not None else base_types.UninitialisedField(self, 'UdrtkgAmdmntRspnMsg', UndertakingAmendmentResponseMessage1, False)

	@UdrtkgAmdmntRspnMsg.deleter
	def UdrtkgAmdmntRspnMsg(self):
		del self._UdrtkgAmdmntRspnMsg
		self._UdrtkgAmdmntRspnMsg = base_types.UninitialisedField(self, 'UdrtkgAmdmntRspnMsg', UndertakingAmendmentResponseMessage1, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='UdrtkgAmdmntRspnMsg', type=UndertakingAmendmentResponseMessage1, min=1, max=1, mutex_group=None, array=False),
	))