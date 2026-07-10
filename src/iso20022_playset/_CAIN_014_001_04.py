# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._RetrievalFulfilmentInitiationV04 import RetrievalFulfilmentInitiationV04

class CAIN_014_001_04():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:cain.014.001.04"
		_docname = "cain.014.001.04"

		__slots__ = ["_RtrvlFlfmtInitn"]
		@property
		def RtrvlFlfmtInitn(self):
			return self._RtrvlFlfmtInitn

		@RtrvlFlfmtInitn.setter
		def RtrvlFlfmtInitn(self, value):
			self._RtrvlFlfmtInitn = value if type(value) != base_types.auto else self.make_default("RtrvlFlfmtInitn")

		@RtrvlFlfmtInitn.deleter
		def RtrvlFlfmtInitn(self):
			del self._RtrvlFlfmtInitn
			self._RtrvlFlfmtInitn = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='RtrvlFlfmtInitn', type=RetrievalFulfilmentInitiationV04, min=1, max=1, mutex_group=None, array=False),
		))