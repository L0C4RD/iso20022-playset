# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CashInOrOut7Choice

class PaymentTransaction71(base_types._BaseFieldType):

	__slots__ = ["_CshInOrOut"]
	@property
	def CshInOrOut(self):
		return self._CshInOrOut

	@CshInOrOut.setter
	def CshInOrOut(self, value):
		self._CshInOrOut = value if value is not None else base_types.UninitialisedField(self, 'CshInOrOut', CashInOrOut7Choice, False)

	@CshInOrOut.deleter
	def CshInOrOut(self):
		del self._CshInOrOut
		self._CshInOrOut = base_types.UninitialisedField(self, 'CshInOrOut', CashInOrOut7Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='CshInOrOut', type=CashInOrOut7Choice, min=1, max=1, mutex_group=None, array=False),
	))