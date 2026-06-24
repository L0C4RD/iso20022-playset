# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._EligibleSecuritiesCreationRequestV01 import EligibleSecuritiesCreationRequestV01

class REDA_025_001_01():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : base_types.DataType_String(None, data="urn:iso:std:iso:20022:tech:xsd:reda.025.001.01"),
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=base_types.DataType_String, required=True),
		))

		__slots__ = ["_ElgblSctiesCreReq"]
		@property
		def ElgblSctiesCreReq(self):
			return self._ElgblSctiesCreReq

		@ElgblSctiesCreReq.setter
		def ElgblSctiesCreReq(self, value):
			self._ElgblSctiesCreReq = value if type(value) != base_types.auto else self.make_default("ElgblSctiesCreReq")

		@ElgblSctiesCreReq.deleter
		def ElgblSctiesCreReq(self):
			del self._ElgblSctiesCreReq
			self._ElgblSctiesCreReq = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='ElgblSctiesCreReq', type=EligibleSecuritiesCreationRequestV01, min=1, max=1, mutex_group=None, array=False),
		))