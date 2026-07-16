# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import RetrievalFulfilmentInitiationV03

class CAIN_014_001_03():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:cain.014.001.03"
		_docname = "cain.014.001.03"

		__slots__ = ["_RtrvlFlfmtInitn"]
		@property
		def RtrvlFlfmtInitn(self):
			return self._RtrvlFlfmtInitn

		@RtrvlFlfmtInitn.setter
		def RtrvlFlfmtInitn(self, value):
			self._RtrvlFlfmtInitn = value if value is not None else base_types.UninitialisedField(self, 'RtrvlFlfmtInitn', RetrievalFulfilmentInitiationV03, False)

		@RtrvlFlfmtInitn.deleter
		def RtrvlFlfmtInitn(self):
			del self._RtrvlFlfmtInitn
			self._RtrvlFlfmtInitn = base_types.UninitialisedField(self, 'RtrvlFlfmtInitn', RetrievalFulfilmentInitiationV03, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='RtrvlFlfmtInitn', type=RetrievalFulfilmentInitiationV03, min=1, max=1, mutex_group=None, array=False),
		))