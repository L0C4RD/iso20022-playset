# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import IntraPositionMovementStatusAdviceV08

class SEMT_014_001_08():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:semt.014.001.08"
		_docname = "semt.014.001.08"

		__slots__ = ["_IntraPosMvmntStsAdvc"]
		@property
		def IntraPosMvmntStsAdvc(self):
			return self._IntraPosMvmntStsAdvc

		@IntraPosMvmntStsAdvc.setter
		def IntraPosMvmntStsAdvc(self, value):
			self._IntraPosMvmntStsAdvc = value if value is not None else base_types.UninitialisedField(self, 'IntraPosMvmntStsAdvc', IntraPositionMovementStatusAdviceV08, False)

		@IntraPosMvmntStsAdvc.deleter
		def IntraPosMvmntStsAdvc(self):
			del self._IntraPosMvmntStsAdvc
			self._IntraPosMvmntStsAdvc = base_types.UninitialisedField(self, 'IntraPosMvmntStsAdvc', IntraPositionMovementStatusAdviceV08, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='IntraPosMvmntStsAdvc', type=IntraPositionMovementStatusAdviceV08, min=1, max=1, mutex_group=None, array=False),
		))