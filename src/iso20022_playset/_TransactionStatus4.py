# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import BaselineStatus3Code

class TransactionStatus4(base_types._BaseFieldType):

	__slots__ = ["_Sts"]
	@property
	def Sts(self):
		return self._Sts

	@Sts.setter
	def Sts(self, value):
		self._Sts = value if value is not None else base_types.UninitialisedField(self, 'Sts', BaselineStatus3Code, False)

	@Sts.deleter
	def Sts(self):
		del self._Sts
		self._Sts = base_types.UninitialisedField(self, 'Sts', BaselineStatus3Code, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Sts', type=BaselineStatus3Code, min=1, max=1, mutex_group=None, array=False),
	))