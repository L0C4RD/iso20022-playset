# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._UndertakingAmendmentResponseV01 import UndertakingAmendmentResponseV01

class TSRV_008_001_01():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:tsrv.008.001.01"
		_docname = "tsrv.008.001.01"

		__slots__ = ["_UdrtkgAmdmntRspn"]
		@property
		def UdrtkgAmdmntRspn(self):
			return self._UdrtkgAmdmntRspn

		@UdrtkgAmdmntRspn.setter
		def UdrtkgAmdmntRspn(self, value):
			self._UdrtkgAmdmntRspn = value if type(value) != base_types.auto else self.make_default("UdrtkgAmdmntRspn")

		@UdrtkgAmdmntRspn.deleter
		def UdrtkgAmdmntRspn(self):
			del self._UdrtkgAmdmntRspn
			self._UdrtkgAmdmntRspn = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='UdrtkgAmdmntRspn', type=UndertakingAmendmentResponseV01, min=1, max=1, mutex_group=None, array=False),
		))