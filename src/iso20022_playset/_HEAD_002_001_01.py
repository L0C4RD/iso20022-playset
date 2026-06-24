# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._LaxPayload import LaxPayload
from ._PayloadDescription2 import PayloadDescription2

class HEAD_002_001_01():

	class BusinessFileHeaderV01(base_types._BaseFieldType):

		attrib = {
			"xmlns" : "urn:iso:std:iso:20022:tech:xsd:head.002.001.01",
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=xs:string, required=True),
		))

		__slots__ = ["_Pyld", "_PyldDesc"]
		@property
		def Pyld(self):
			return self._Pyld

		@Pyld.setter
		def Pyld(self, value):
			self._Pyld = value if type(value) != base_types.auto else self.make_default("Pyld")

		@Pyld.deleter
		def Pyld(self):
			del self._Pyld
			self._Pyld = None

		@property
		def PyldDesc(self):
			return self._PyldDesc

		@PyldDesc.setter
		def PyldDesc(self, value):
			self._PyldDesc = value if type(value) != base_types.auto else self.make_default("PyldDesc")

		@PyldDesc.deleter
		def PyldDesc(self):
			del self._PyldDesc
			self._PyldDesc = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='Pyld', type=LaxPayload, min=0, max=None, mutex_group=None, array=True),
			base_types.FieldEntry(name='PyldDesc', type=PayloadDescription2, min=1, max=1, mutex_group=None, array=False),
		))