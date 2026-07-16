# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import UndertakingIssuanceV01

class TSRV_001_001_01():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:tsrv.001.001.01"
		_docname = "tsrv.001.001.01"

		__slots__ = ["_UdrtkgIssnc"]
		@property
		def UdrtkgIssnc(self):
			return self._UdrtkgIssnc

		@UdrtkgIssnc.setter
		def UdrtkgIssnc(self, value):
			self._UdrtkgIssnc = value if value is not None else base_types.UninitialisedField(self, 'UdrtkgIssnc', UndertakingIssuanceV01, False)

		@UdrtkgIssnc.deleter
		def UdrtkgIssnc(self):
			del self._UdrtkgIssnc
			self._UdrtkgIssnc = base_types.UninitialisedField(self, 'UdrtkgIssnc', UndertakingIssuanceV01, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='UdrtkgIssnc', type=UndertakingIssuanceV01, min=1, max=1, mutex_group=None, array=False),
		))