# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._IdentificationInformation5 import IdentificationInformation5
from ._Max35Text import Max35Text

class IdentificationVerification5(base_types._BaseFieldType):

	__slots__ = ["_Id", "_PtyAndAcctId"]
	@property
	def Id(self):
		return self._Id

	@Id.setter
	def Id(self, value):
		self._Id = value if type(value) != base_types.auto else self.make_default("Id")

	@Id.deleter
	def Id(self):
		del self._Id
		self._Id = None

	@property
	def PtyAndAcctId(self):
		return self._PtyAndAcctId

	@PtyAndAcctId.setter
	def PtyAndAcctId(self, value):
		self._PtyAndAcctId = value if type(value) != base_types.auto else self.make_default("PtyAndAcctId")

	@PtyAndAcctId.deleter
	def PtyAndAcctId(self):
		del self._PtyAndAcctId
		self._PtyAndAcctId = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Id', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PtyAndAcctId', type=IdentificationInformation5, min=1, max=1, mutex_group=None, array=False),
	))