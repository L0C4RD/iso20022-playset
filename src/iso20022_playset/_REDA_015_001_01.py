# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._PartyQueryV01 import PartyQueryV01

class REDA_015_001_01():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : base_types._BaseDataType_String(None, data="urn:iso:std:iso:20022:tech:xsd:reda.015.001.01"),
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=base_types._BaseDataType_String, required=True),
		))

		__slots__ = ["_PtyQry"]
		@property
		def PtyQry(self):
			return self._PtyQry

		@PtyQry.setter
		def PtyQry(self, value):
			self._PtyQry = value if type(value) != base_types.auto else self.make_default("PtyQry")

		@PtyQry.deleter
		def PtyQry(self):
			del self._PtyQry
			self._PtyQry = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='PtyQry', type=PartyQueryV01, min=1, max=1, mutex_group=None, array=False),
		))