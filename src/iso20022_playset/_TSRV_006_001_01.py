# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._UndertakingAmendmentAdviceV01 import UndertakingAmendmentAdviceV01

class TSRV_006_001_01():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : "urn:iso:std:iso:20022:tech:xsd:tsrv.006.001.01",
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=xs:string, required=True),
		))

		__slots__ = ["_UdrtkgAmdmntAdvc"]
		@property
		def UdrtkgAmdmntAdvc(self):
			return self._UdrtkgAmdmntAdvc

		@UdrtkgAmdmntAdvc.setter
		def UdrtkgAmdmntAdvc(self, value):
			self._UdrtkgAmdmntAdvc = value if type(value) != base_types.auto else self.make_default("UdrtkgAmdmntAdvc")

		@UdrtkgAmdmntAdvc.deleter
		def UdrtkgAmdmntAdvc(self):
			del self._UdrtkgAmdmntAdvc
			self._UdrtkgAmdmntAdvc = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='UdrtkgAmdmntAdvc', type=UndertakingAmendmentAdviceV01, min=1, max=1, mutex_group=None, array=False),
		))