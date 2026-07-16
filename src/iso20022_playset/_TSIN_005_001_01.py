# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import UndertakingApplicationV01

class TSIN_005_001_01():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:tsin.005.001.01"
		_docname = "tsin.005.001.01"

		__slots__ = ["_UdrtkgAppl"]
		@property
		def UdrtkgAppl(self):
			return self._UdrtkgAppl

		@UdrtkgAppl.setter
		def UdrtkgAppl(self, value):
			self._UdrtkgAppl = value if value is not None else base_types.UninitialisedField(self, 'UdrtkgAppl', UndertakingApplicationV01, False)

		@UdrtkgAppl.deleter
		def UdrtkgAppl(self):
			del self._UdrtkgAppl
			self._UdrtkgAppl = base_types.UninitialisedField(self, 'UdrtkgAppl', UndertakingApplicationV01, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='UdrtkgAppl', type=UndertakingApplicationV01, min=1, max=1, mutex_group=None, array=False),
		))