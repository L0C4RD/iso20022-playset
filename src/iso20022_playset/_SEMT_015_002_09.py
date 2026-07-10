# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._IntraPositionMovementConfirmation002V09 import IntraPositionMovementConfirmation002V09

class SEMT_015_002_09():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:semt.015.002.09"
		_docname = "semt.015.002.09"

		__slots__ = ["_IntraPosMvmntConf"]
		@property
		def IntraPosMvmntConf(self):
			return self._IntraPosMvmntConf

		@IntraPosMvmntConf.setter
		def IntraPosMvmntConf(self, value):
			self._IntraPosMvmntConf = value if type(value) != base_types.auto else self.make_default("IntraPosMvmntConf")

		@IntraPosMvmntConf.deleter
		def IntraPosMvmntConf(self):
			del self._IntraPosMvmntConf
			self._IntraPosMvmntConf = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='IntraPosMvmntConf', type=IntraPositionMovementConfirmation002V09, min=1, max=1, mutex_group=None, array=False),
		))