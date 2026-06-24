# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._PartyDeletionRequestV01 import PartyDeletionRequestV01

class REDA_031_001_01():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : base_types._BaseDataType_String(None, data="urn:iso:std:iso:20022:tech:xsd:reda.031.001.01"),
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=base_types._BaseDataType_String, required=True),
		))

		__slots__ = ["_PtyDeltnReq"]
		@property
		def PtyDeltnReq(self):
			return self._PtyDeltnReq

		@PtyDeltnReq.setter
		def PtyDeltnReq(self, value):
			self._PtyDeltnReq = value if type(value) != base_types.auto else self.make_default("PtyDeltnReq")

		@PtyDeltnReq.deleter
		def PtyDeltnReq(self):
			del self._PtyDeltnReq
			self._PtyDeltnReq = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='PtyDeltnReq', type=PartyDeletionRequestV01, min=1, max=1, mutex_group=None, array=False),
		))