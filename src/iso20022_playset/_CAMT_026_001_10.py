# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import UnableToApplyV10

class CAMT_026_001_10():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:camt.026.001.10"
		_docname = "camt.026.001.10"

		__slots__ = ["_UblToApply"]
		@property
		def UblToApply(self):
			return self._UblToApply

		@UblToApply.setter
		def UblToApply(self, value):
			self._UblToApply = value if value is not None else base_types.UninitialisedField(self, 'UblToApply', UnableToApplyV10, False)

		@UblToApply.deleter
		def UblToApply(self):
			del self._UblToApply
			self._UblToApply = base_types.UninitialisedField(self, 'UblToApply', UnableToApplyV10, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='UblToApply', type=UnableToApplyV10, min=1, max=1, mutex_group=None, array=False),
		))