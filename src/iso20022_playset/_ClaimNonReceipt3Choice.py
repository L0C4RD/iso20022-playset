# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ClaimNonReceipt3
from . import ClaimNonReceiptRejectReason1Choice

class ClaimNonReceipt3Choice(base_types._BaseFieldType):

	__slots__ = ["_Accptd", "_Rjctd"]
	@property
	def Accptd(self):
		return self._Accptd

	@Accptd.setter
	def Accptd(self, value):
		self._Accptd = value if value is not None else base_types.UninitialisedField(self, 'Accptd', ClaimNonReceipt3, False)

	@Accptd.deleter
	def Accptd(self):
		del self._Accptd
		self._Accptd = base_types.UninitialisedField(self, 'Accptd', ClaimNonReceipt3, False)

	@property
	def Rjctd(self):
		return self._Rjctd

	@Rjctd.setter
	def Rjctd(self, value):
		self._Rjctd = value if value is not None else base_types.UninitialisedField(self, 'Rjctd', ClaimNonReceiptRejectReason1Choice, False)

	@Rjctd.deleter
	def Rjctd(self):
		del self._Rjctd
		self._Rjctd = base_types.UninitialisedField(self, 'Rjctd', ClaimNonReceiptRejectReason1Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Accptd', type=ClaimNonReceipt3, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Rjctd', type=ClaimNonReceiptRejectReason1Choice, min=0, max=1, mutex_group=1, array=False),
	))