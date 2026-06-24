# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._UndertakingAmendmentRequestV01 import UndertakingAmendmentRequestV01

class TSRV_004_001_01():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : base_types.DataType_String(None, data="urn:iso:std:iso:20022:tech:xsd:tsrv.004.001.01"),
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=base_types.DataType_String, required=True),
		))

		__slots__ = ["_UdrtkgAmdmntReq"]
		@property
		def UdrtkgAmdmntReq(self):
			return self._UdrtkgAmdmntReq

		@UdrtkgAmdmntReq.setter
		def UdrtkgAmdmntReq(self, value):
			self._UdrtkgAmdmntReq = value if type(value) != base_types.auto else self.make_default("UdrtkgAmdmntReq")

		@UdrtkgAmdmntReq.deleter
		def UdrtkgAmdmntReq(self):
			del self._UdrtkgAmdmntReq
			self._UdrtkgAmdmntReq = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='UdrtkgAmdmntReq', type=UndertakingAmendmentRequestV01, min=1, max=1, mutex_group=None, array=False),
		))