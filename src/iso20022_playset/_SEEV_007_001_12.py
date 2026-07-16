# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import MeetingVoteExecutionConfirmationV12

class SEEV_007_001_12():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:seev.007.001.12"
		_docname = "seev.007.001.12"

		__slots__ = ["_MtgVoteExctnConf"]
		@property
		def MtgVoteExctnConf(self):
			return self._MtgVoteExctnConf

		@MtgVoteExctnConf.setter
		def MtgVoteExctnConf(self, value):
			self._MtgVoteExctnConf = value if value is not None else base_types.UninitialisedField(self, 'MtgVoteExctnConf', MeetingVoteExecutionConfirmationV12, False)

		@MtgVoteExctnConf.deleter
		def MtgVoteExctnConf(self):
			del self._MtgVoteExctnConf
			self._MtgVoteExctnConf = base_types.UninitialisedField(self, 'MtgVoteExctnConf', MeetingVoteExecutionConfirmationV12, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='MtgVoteExctnConf', type=MeetingVoteExecutionConfirmationV12, min=1, max=1, mutex_group=None, array=False),
		))