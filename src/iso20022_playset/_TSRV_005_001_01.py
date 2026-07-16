# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import UndertakingAmendmentV01

class TSRV_005_001_01():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:tsrv.005.001.01"
		_docname = "tsrv.005.001.01"

		__slots__ = ["_UdrtkgAmdmnt"]
		@property
		def UdrtkgAmdmnt(self):
			return self._UdrtkgAmdmnt

		@UdrtkgAmdmnt.setter
		def UdrtkgAmdmnt(self, value):
			self._UdrtkgAmdmnt = value if value is not None else base_types.UninitialisedField(self, 'UdrtkgAmdmnt', UndertakingAmendmentV01, False)

		@UdrtkgAmdmnt.deleter
		def UdrtkgAmdmnt(self):
			del self._UdrtkgAmdmnt
			self._UdrtkgAmdmnt = base_types.UninitialisedField(self, 'UdrtkgAmdmnt', UndertakingAmendmentV01, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='UdrtkgAmdmnt', type=UndertakingAmendmentV01, min=1, max=1, mutex_group=None, array=False),
		))