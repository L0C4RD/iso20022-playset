# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import SubscriptionOrderV05

class SETR_010_001_05():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:setr.010.001.05"
		_docname = "setr.010.001.05"

		__slots__ = ["_SbcptOrdr"]
		@property
		def SbcptOrdr(self):
			return self._SbcptOrdr

		@SbcptOrdr.setter
		def SbcptOrdr(self, value):
			self._SbcptOrdr = value if value is not None else base_types.UninitialisedField(self, 'SbcptOrdr', SubscriptionOrderV05, False)

		@SbcptOrdr.deleter
		def SbcptOrdr(self):
			del self._SbcptOrdr
			self._SbcptOrdr = base_types.UninitialisedField(self, 'SbcptOrdr', SubscriptionOrderV05, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='SbcptOrdr', type=SubscriptionOrderV05, min=1, max=1, mutex_group=None, array=False),
		))