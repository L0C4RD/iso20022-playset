# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._AddendumInitiationV03 import AddendumInitiationV03

class CAIN_025_001_03():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_AdddmInitn"]
		@property
		def AdddmInitn(self):
			return self._AdddmInitn

		@AdddmInitn.setter
		def AdddmInitn(self, value):
			self._AdddmInitn = value if type(value) != base_types.auto else self.make_default("AdddmInitn")

		@AdddmInitn.deleter
		def AdddmInitn(self):
			del self._AdddmInitn
			self._AdddmInitn = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='AdddmInitn', type=AddendumInitiationV03, min=1, max=1, mutex_group=None, array=False),
		))