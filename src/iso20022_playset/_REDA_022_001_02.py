# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._PartyModificationRequestV02 import PartyModificationRequestV02

class REDA_022_001_02():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_PtyModReq"]
		@property
		def PtyModReq(self):
			return self._PtyModReq

		@PtyModReq.setter
		def PtyModReq(self, value):
			self._PtyModReq = value if type(value) != base_types.auto else self.make_default("PtyModReq")

		@PtyModReq.deleter
		def PtyModReq(self):
			del self._PtyModReq
			self._PtyModReq = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='PtyModReq', type=PartyModificationRequestV02, min=1, max=1, mutex_group=None, array=False),
		))