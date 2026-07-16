# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import IntraPositionMovementConfirmationV10

class SEMT_015_001_10():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:semt.015.001.10"
		_docname = "semt.015.001.10"

		__slots__ = ["_IntraPosMvmntConf"]
		@property
		def IntraPosMvmntConf(self):
			return self._IntraPosMvmntConf

		@IntraPosMvmntConf.setter
		def IntraPosMvmntConf(self, value):
			self._IntraPosMvmntConf = value if value is not None else base_types.UninitialisedField(self, 'IntraPosMvmntConf', IntraPositionMovementConfirmationV10, False)

		@IntraPosMvmntConf.deleter
		def IntraPosMvmntConf(self):
			del self._IntraPosMvmntConf
			self._IntraPosMvmntConf = base_types.UninitialisedField(self, 'IntraPosMvmntConf', IntraPositionMovementConfirmationV10, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='IntraPosMvmntConf', type=IntraPositionMovementConfirmationV10, min=1, max=1, mutex_group=None, array=False),
		))