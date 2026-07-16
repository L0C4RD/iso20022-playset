# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import RetrievalInitiationV03

class CAIN_021_001_03():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:cain.021.001.03"
		_docname = "cain.021.001.03"

		__slots__ = ["_RtrvlInitn"]
		@property
		def RtrvlInitn(self):
			return self._RtrvlInitn

		@RtrvlInitn.setter
		def RtrvlInitn(self, value):
			self._RtrvlInitn = value if value is not None else base_types.UninitialisedField(self, 'RtrvlInitn', RetrievalInitiationV03, False)

		@RtrvlInitn.deleter
		def RtrvlInitn(self):
			del self._RtrvlInitn
			self._RtrvlInitn = base_types.UninitialisedField(self, 'RtrvlInitn', RetrievalInitiationV03, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='RtrvlInitn', type=RetrievalInitiationV03, min=1, max=1, mutex_group=None, array=False),
		))