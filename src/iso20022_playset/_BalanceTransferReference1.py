# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Max35Text

class BalanceTransferReference1(base_types._BaseFieldType):

	__slots__ = ["_BalTrfRef"]
	@property
	def BalTrfRef(self):
		return self._BalTrfRef

	@BalTrfRef.setter
	def BalTrfRef(self, value):
		self._BalTrfRef = value if value is not None else base_types.UninitialisedField(self, 'BalTrfRef', Max35Text, False)

	@BalTrfRef.deleter
	def BalTrfRef(self):
		del self._BalTrfRef
		self._BalTrfRef = base_types.UninitialisedField(self, 'BalTrfRef', Max35Text, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='BalTrfRef', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
	))