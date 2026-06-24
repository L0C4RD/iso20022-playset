# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._RemittanceLocationAdviceV03 import RemittanceLocationAdviceV03

class REMT_002_001_03():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : "urn:iso:std:iso:20022:tech:xsd:remt.002.001.03",
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=xs:string, required=True),
		))

		__slots__ = ["_RmtLctnAdvc"]
		@property
		def RmtLctnAdvc(self):
			return self._RmtLctnAdvc

		@RmtLctnAdvc.setter
		def RmtLctnAdvc(self, value):
			self._RmtLctnAdvc = value if type(value) != base_types.auto else self.make_default("RmtLctnAdvc")

		@RmtLctnAdvc.deleter
		def RmtLctnAdvc(self):
			del self._RmtLctnAdvc
			self._RmtLctnAdvc = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='RmtLctnAdvc', type=RemittanceLocationAdviceV03, min=1, max=1, mutex_group=None, array=False),
		))