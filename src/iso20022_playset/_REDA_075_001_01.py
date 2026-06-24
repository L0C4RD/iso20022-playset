# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._EligibleSecuritiesDeletionRequestV01 import EligibleSecuritiesDeletionRequestV01

class REDA_075_001_01():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : base_types._BaseDataType_String(None, data="urn:iso:std:iso:20022:tech:xsd:reda.075.001.01"),
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=base_types._BaseDataType_String, required=True),
		))

		__slots__ = ["_ElgblSctiesDeltnReq"]
		@property
		def ElgblSctiesDeltnReq(self):
			return self._ElgblSctiesDeltnReq

		@ElgblSctiesDeltnReq.setter
		def ElgblSctiesDeltnReq(self, value):
			self._ElgblSctiesDeltnReq = value if type(value) != base_types.auto else self.make_default("ElgblSctiesDeltnReq")

		@ElgblSctiesDeltnReq.deleter
		def ElgblSctiesDeltnReq(self):
			del self._ElgblSctiesDeltnReq
			self._ElgblSctiesDeltnReq = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='ElgblSctiesDeltnReq', type=EligibleSecuritiesDeletionRequestV01, min=1, max=1, mutex_group=None, array=False),
		))