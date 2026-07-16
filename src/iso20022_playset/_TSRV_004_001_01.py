# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import UndertakingAmendmentRequestV01

class TSRV_004_001_01():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:tsrv.004.001.01"
		_docname = "tsrv.004.001.01"

		__slots__ = ["_UdrtkgAmdmntReq"]
		@property
		def UdrtkgAmdmntReq(self):
			return self._UdrtkgAmdmntReq

		@UdrtkgAmdmntReq.setter
		def UdrtkgAmdmntReq(self, value):
			self._UdrtkgAmdmntReq = value if value is not None else base_types.UninitialisedField(self, 'UdrtkgAmdmntReq', UndertakingAmendmentRequestV01, False)

		@UdrtkgAmdmntReq.deleter
		def UdrtkgAmdmntReq(self):
			del self._UdrtkgAmdmntReq
			self._UdrtkgAmdmntReq = base_types.UninitialisedField(self, 'UdrtkgAmdmntReq', UndertakingAmendmentRequestV01, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='UdrtkgAmdmntReq', type=UndertakingAmendmentRequestV01, min=1, max=1, mutex_group=None, array=False),
		))