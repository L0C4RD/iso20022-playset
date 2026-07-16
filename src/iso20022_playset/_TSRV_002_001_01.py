# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import UndertakingIssuanceAdviceV01

class TSRV_002_001_01():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:tsrv.002.001.01"
		_docname = "tsrv.002.001.01"

		__slots__ = ["_UdrtkgIssncAdvc"]
		@property
		def UdrtkgIssncAdvc(self):
			return self._UdrtkgIssncAdvc

		@UdrtkgIssncAdvc.setter
		def UdrtkgIssncAdvc(self, value):
			self._UdrtkgIssncAdvc = value if value is not None else base_types.UninitialisedField(self, 'UdrtkgIssncAdvc', UndertakingIssuanceAdviceV01, False)

		@UdrtkgIssncAdvc.deleter
		def UdrtkgIssncAdvc(self):
			del self._UdrtkgIssncAdvc
			self._UdrtkgIssncAdvc = base_types.UninitialisedField(self, 'UdrtkgIssncAdvc', UndertakingIssuanceAdviceV01, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='UdrtkgIssncAdvc', type=UndertakingIssuanceAdviceV01, min=1, max=1, mutex_group=None, array=False),
		))