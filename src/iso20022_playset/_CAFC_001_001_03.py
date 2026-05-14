# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._FeeCollectionInitiationV03 import FeeCollectionInitiationV03

class CAFC_001_001_03():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_FeeColltnInitn"]
		@property
		def FeeColltnInitn(self):
			return self._FeeColltnInitn

		@FeeColltnInitn.setter
		def FeeColltnInitn(self, value):
			self._FeeColltnInitn = value if type(value) != base_types.auto else self.make_default("FeeColltnInitn")

		@FeeColltnInitn.deleter
		def FeeColltnInitn(self):
			del self._FeeColltnInitn
			self._FeeColltnInitn = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='FeeColltnInitn', type=FeeCollectionInitiationV03, min=1, max=1, mutex_group=None, array=False),
		))