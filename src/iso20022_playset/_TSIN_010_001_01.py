# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._PartyRegistrationAndGuaranteeStatusV01 import PartyRegistrationAndGuaranteeStatusV01

class TSIN_010_001_01():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : base_types._BaseDataType_String(None, data="urn:iso:std:iso:20022:tech:xsd:tsin.010.001.01"),
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=base_types._BaseDataType_String, required=True),
		))

		__slots__ = ["_PtyRegnAndGrntSts"]
		@property
		def PtyRegnAndGrntSts(self):
			return self._PtyRegnAndGrntSts

		@PtyRegnAndGrntSts.setter
		def PtyRegnAndGrntSts(self, value):
			self._PtyRegnAndGrntSts = value if type(value) != base_types.auto else self.make_default("PtyRegnAndGrntSts")

		@PtyRegnAndGrntSts.deleter
		def PtyRegnAndGrntSts(self):
			del self._PtyRegnAndGrntSts
			self._PtyRegnAndGrntSts = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='PtyRegnAndGrntSts', type=PartyRegistrationAndGuaranteeStatusV01, min=1, max=1, mutex_group=None, array=False),
		))