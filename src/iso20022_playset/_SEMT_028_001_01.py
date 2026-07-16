# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import IntraPositionMovementQueryV01

class SEMT_028_001_01():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:semt.028.001.01"
		_docname = "semt.028.001.01"

		__slots__ = ["_IntraPosMvmntQry"]
		@property
		def IntraPosMvmntQry(self):
			return self._IntraPosMvmntQry

		@IntraPosMvmntQry.setter
		def IntraPosMvmntQry(self, value):
			self._IntraPosMvmntQry = value if value is not None else base_types.UninitialisedField(self, 'IntraPosMvmntQry', IntraPositionMovementQueryV01, False)

		@IntraPosMvmntQry.deleter
		def IntraPosMvmntQry(self):
			del self._IntraPosMvmntQry
			self._IntraPosMvmntQry = base_types.UninitialisedField(self, 'IntraPosMvmntQry', IntraPositionMovementQueryV01, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='IntraPosMvmntQry', type=IntraPositionMovementQueryV01, min=1, max=1, mutex_group=None, array=False),
		))