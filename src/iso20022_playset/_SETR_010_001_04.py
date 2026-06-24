# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._SubscriptionOrderV04 import SubscriptionOrderV04

class SETR_010_001_04():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : "urn:iso:std:iso:20022:tech:xsd:setr.010.001.04",
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=xs:string, required=True),
		))

		__slots__ = ["_SbcptOrdr"]
		@property
		def SbcptOrdr(self):
			return self._SbcptOrdr

		@SbcptOrdr.setter
		def SbcptOrdr(self, value):
			self._SbcptOrdr = value if type(value) != base_types.auto else self.make_default("SbcptOrdr")

		@SbcptOrdr.deleter
		def SbcptOrdr(self):
			del self._SbcptOrdr
			self._SbcptOrdr = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='SbcptOrdr', type=SubscriptionOrderV04, min=1, max=1, mutex_group=None, array=False),
		))