# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._RetrievalInitiationV03 import RetrievalInitiationV03

class CAIN_021_001_03():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : base_types.DataType_String(None, data="urn:iso:std:iso:20022:tech:xsd:cain.021.001.03"),
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=base_types.DataType_String, required=True),
		))

		__slots__ = ["_RtrvlInitn"]
		@property
		def RtrvlInitn(self):
			return self._RtrvlInitn

		@RtrvlInitn.setter
		def RtrvlInitn(self, value):
			self._RtrvlInitn = value if type(value) != base_types.auto else self.make_default("RtrvlInitn")

		@RtrvlInitn.deleter
		def RtrvlInitn(self):
			del self._RtrvlInitn
			self._RtrvlInitn = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='RtrvlInitn', type=RetrievalInitiationV03, min=1, max=1, mutex_group=None, array=False),
		))