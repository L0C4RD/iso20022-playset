# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActionReminderV03

class TSMT_024_001_03():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:tsmt.024.001.03"
		_docname = "tsmt.024.001.03"

		__slots__ = ["_ActnRmndr"]
		@property
		def ActnRmndr(self):
			return self._ActnRmndr

		@ActnRmndr.setter
		def ActnRmndr(self, value):
			self._ActnRmndr = value if value is not None else base_types.UninitialisedField(self, 'ActnRmndr', ActionReminderV03, False)

		@ActnRmndr.deleter
		def ActnRmndr(self):
			del self._ActnRmndr
			self._ActnRmndr = base_types.UninitialisedField(self, 'ActnRmndr', ActionReminderV03, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='ActnRmndr', type=ActionReminderV03, min=1, max=1, mutex_group=None, array=False),
		))