# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import GetMemberV04

class CAMT_013_001_04():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:camt.013.001.04"
		_docname = "camt.013.001.04"

		__slots__ = ["_GetMmb"]
		@property
		def GetMmb(self):
			return self._GetMmb

		@GetMmb.setter
		def GetMmb(self, value):
			self._GetMmb = value if value is not None else base_types.UninitialisedField(self, 'GetMmb', GetMemberV04, False)

		@GetMmb.deleter
		def GetMmb(self):
			del self._GetMmb
			self._GetMmb = base_types.UninitialisedField(self, 'GetMmb', GetMemberV04, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='GetMmb', type=GetMemberV04, min=1, max=1, mutex_group=None, array=False),
		))