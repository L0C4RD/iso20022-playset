# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._MeetingVoteExecutionConfirmationV11 import MeetingVoteExecutionConfirmationV11

class SEEV_007_001_11():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : base_types._BaseDataType_String(None, data="urn:iso:std:iso:20022:tech:xsd:seev.007.001.11"),
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=base_types._BaseDataType_String, required=True),
		))

		__slots__ = ["_MtgVoteExctnConf"]
		@property
		def MtgVoteExctnConf(self):
			return self._MtgVoteExctnConf

		@MtgVoteExctnConf.setter
		def MtgVoteExctnConf(self, value):
			self._MtgVoteExctnConf = value if type(value) != base_types.auto else self.make_default("MtgVoteExctnConf")

		@MtgVoteExctnConf.deleter
		def MtgVoteExctnConf(self):
			del self._MtgVoteExctnConf
			self._MtgVoteExctnConf = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='MtgVoteExctnConf', type=MeetingVoteExecutionConfirmationV11, min=1, max=1, mutex_group=None, array=False),
		))