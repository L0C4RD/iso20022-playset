# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._SubscriptionOrderV05 import SubscriptionOrderV05

class SETR_010_001_05():

	class Document(base_types._BaseFieldType):

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
			base_types.FieldEntry(name='SbcptOrdr', type=SubscriptionOrderV05, min=1, max=1, mutex_group=None, array=False),
		))