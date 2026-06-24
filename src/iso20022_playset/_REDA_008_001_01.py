# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._SecurityCreationStatusAdviceV01 import SecurityCreationStatusAdviceV01

class REDA_008_001_01():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : "urn:iso:std:iso:20022:tech:xsd:reda.008.001.01",
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=xs:string, required=True),
		))

		__slots__ = ["_SctyCreStsAdvc"]
		@property
		def SctyCreStsAdvc(self):
			return self._SctyCreStsAdvc

		@SctyCreStsAdvc.setter
		def SctyCreStsAdvc(self, value):
			self._SctyCreStsAdvc = value if type(value) != base_types.auto else self.make_default("SctyCreStsAdvc")

		@SctyCreStsAdvc.deleter
		def SctyCreStsAdvc(self):
			del self._SctyCreStsAdvc
			self._SctyCreStsAdvc = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='SctyCreStsAdvc', type=SecurityCreationStatusAdviceV01, min=1, max=1, mutex_group=None, array=False),
		))