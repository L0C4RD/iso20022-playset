# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import UndertakingNonExtensionRequestV01

class TSRV_010_001_01():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:tsrv.010.001.01"
		_docname = "tsrv.010.001.01"

		__slots__ = ["_UdrtkgNonXtnsnReq"]
		@property
		def UdrtkgNonXtnsnReq(self):
			return self._UdrtkgNonXtnsnReq

		@UdrtkgNonXtnsnReq.setter
		def UdrtkgNonXtnsnReq(self, value):
			self._UdrtkgNonXtnsnReq = value if value is not None else base_types.UninitialisedField(self, 'UdrtkgNonXtnsnReq', UndertakingNonExtensionRequestV01, False)

		@UdrtkgNonXtnsnReq.deleter
		def UdrtkgNonXtnsnReq(self):
			del self._UdrtkgNonXtnsnReq
			self._UdrtkgNonXtnsnReq = base_types.UninitialisedField(self, 'UdrtkgNonXtnsnReq', UndertakingNonExtensionRequestV01, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='UdrtkgNonXtnsnReq', type=UndertakingNonExtensionRequestV01, min=1, max=1, mutex_group=None, array=False),
		))