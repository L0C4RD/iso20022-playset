# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._CardManagementInitiationV04 import CardManagementInitiationV04

class CAIN_023_001_04():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_CardMgmtInitn"]
		@property
		def CardMgmtInitn(self):
			return self._CardMgmtInitn

		@CardMgmtInitn.setter
		def CardMgmtInitn(self, value):
			self._CardMgmtInitn = value if type(value) != base_types.auto else self.make_default("CardMgmtInitn")

		@CardMgmtInitn.deleter
		def CardMgmtInitn(self):
			del self._CardMgmtInitn
			self._CardMgmtInitn = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='CardMgmtInitn', type=CardManagementInitiationV04, min=1, max=1, mutex_group=None, array=False),
		))