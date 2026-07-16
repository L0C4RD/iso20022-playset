# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ReversalInitiationV05

class CAIN_005_001_05():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:cain.005.001.05"
		_docname = "cain.005.001.05"

		__slots__ = ["_RvslInitn"]
		@property
		def RvslInitn(self):
			return self._RvslInitn

		@RvslInitn.setter
		def RvslInitn(self, value):
			self._RvslInitn = value if value is not None else base_types.UninitialisedField(self, 'RvslInitn', ReversalInitiationV05, False)

		@RvslInitn.deleter
		def RvslInitn(self):
			del self._RvslInitn
			self._RvslInitn = base_types.UninitialisedField(self, 'RvslInitn', ReversalInitiationV05, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='RvslInitn', type=ReversalInitiationV05, min=1, max=1, mutex_group=None, array=False),
		))