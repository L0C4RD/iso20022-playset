# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CreateLimitV02

class CAMT_101_001_02():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:camt.101.001.02"
		_docname = "camt.101.001.02"

		__slots__ = ["_CretLmt"]
		@property
		def CretLmt(self):
			return self._CretLmt

		@CretLmt.setter
		def CretLmt(self, value):
			self._CretLmt = value if value is not None else base_types.UninitialisedField(self, 'CretLmt', CreateLimitV02, False)

		@CretLmt.deleter
		def CretLmt(self):
			del self._CretLmt
			self._CretLmt = base_types.UninitialisedField(self, 'CretLmt', CreateLimitV02, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='CretLmt', type=CreateLimitV02, min=1, max=1, mutex_group=None, array=False),
		))