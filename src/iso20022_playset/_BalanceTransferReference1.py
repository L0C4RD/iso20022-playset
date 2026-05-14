# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._Max35Text import Max35Text

class BalanceTransferReference1(base_types._BaseFieldType):

	__slots__ = ["_BalTrfRef"]
	@property
	def BalTrfRef(self):
		return self._BalTrfRef

	@BalTrfRef.setter
	def BalTrfRef(self, value):
		self._BalTrfRef = value if type(value) != base_types.auto else self.make_default("BalTrfRef")

	@BalTrfRef.deleter
	def BalTrfRef(self):
		del self._BalTrfRef
		self._BalTrfRef = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='BalTrfRef', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
	))