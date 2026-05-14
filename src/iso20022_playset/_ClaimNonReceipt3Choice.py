# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._ClaimNonReceipt3 import ClaimNonReceipt3
from ._ClaimNonReceiptRejectReason1Choice import ClaimNonReceiptRejectReason1Choice

class ClaimNonReceipt3Choice(base_types._BaseFieldType):

	__slots__ = ["_Accptd", "_Rjctd"]
	@property
	def Accptd(self):
		return self._Accptd

	@Accptd.setter
	def Accptd(self, value):
		self._Accptd = value if type(value) != base_types.auto else self.make_default("Accptd")

	@Accptd.deleter
	def Accptd(self):
		del self._Accptd
		self._Accptd = None

	@property
	def Rjctd(self):
		return self._Rjctd

	@Rjctd.setter
	def Rjctd(self, value):
		self._Rjctd = value if type(value) != base_types.auto else self.make_default("Rjctd")

	@Rjctd.deleter
	def Rjctd(self):
		del self._Rjctd
		self._Rjctd = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Accptd', type=ClaimNonReceipt3, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Rjctd', type=ClaimNonReceiptRejectReason1Choice, min=0, max=1, mutex_group=1, array=False),
	))