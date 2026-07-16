# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Max2048Text
from . import TransactionAmendment1Choice

class TransactionAmendment1(base_types._BaseFieldType):

	__slots__ = ["_Pth", "_Rcrd"]
	@property
	def Pth(self):
		return self._Pth

	@Pth.setter
	def Pth(self, value):
		self._Pth = value if value is not None else base_types.UninitialisedField(self, 'Pth', Max2048Text, False)

	@Pth.deleter
	def Pth(self):
		del self._Pth
		self._Pth = base_types.UninitialisedField(self, 'Pth', Max2048Text, False)

	@property
	def Rcrd(self):
		return self._Rcrd

	@Rcrd.setter
	def Rcrd(self, value):
		self._Rcrd = value if value is not None else base_types.UninitialisedField(self, 'Rcrd', TransactionAmendment1Choice, False)

	@Rcrd.deleter
	def Rcrd(self):
		del self._Rcrd
		self._Rcrd = base_types.UninitialisedField(self, 'Rcrd', TransactionAmendment1Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Pth', type=Max2048Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Rcrd', type=TransactionAmendment1Choice, min=1, max=1, mutex_group=None, array=False),
	))