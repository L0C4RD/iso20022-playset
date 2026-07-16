# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import UndertakingDemandV01

class TSRV_013_001_01():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:tsrv.013.001.01"
		_docname = "tsrv.013.001.01"

		__slots__ = ["_UdrtkgDmnd"]
		@property
		def UdrtkgDmnd(self):
			return self._UdrtkgDmnd

		@UdrtkgDmnd.setter
		def UdrtkgDmnd(self, value):
			self._UdrtkgDmnd = value if value is not None else base_types.UninitialisedField(self, 'UdrtkgDmnd', UndertakingDemandV01, False)

		@UdrtkgDmnd.deleter
		def UdrtkgDmnd(self):
			del self._UdrtkgDmnd
			self._UdrtkgDmnd = base_types.UninitialisedField(self, 'UdrtkgDmnd', UndertakingDemandV01, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='UdrtkgDmnd', type=UndertakingDemandV01, min=1, max=1, mutex_group=None, array=False),
		))