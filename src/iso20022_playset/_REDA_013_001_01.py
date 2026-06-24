# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._SecurityDeletionRequestV01 import SecurityDeletionRequestV01

class REDA_013_001_01():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : "urn:iso:std:iso:20022:tech:xsd:reda.013.001.01",
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=xs:string, required=True),
		))

		__slots__ = ["_SctyDeltnReq"]
		@property
		def SctyDeltnReq(self):
			return self._SctyDeltnReq

		@SctyDeltnReq.setter
		def SctyDeltnReq(self, value):
			self._SctyDeltnReq = value if type(value) != base_types.auto else self.make_default("SctyDeltnReq")

		@SctyDeltnReq.deleter
		def SctyDeltnReq(self):
			del self._SctyDeltnReq
			self._SctyDeltnReq = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='SctyDeltnReq', type=SecurityDeletionRequestV01, min=1, max=1, mutex_group=None, array=False),
		))