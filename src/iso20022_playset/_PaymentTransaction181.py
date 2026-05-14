# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._CashInOrOut8Choice import CashInOrOut8Choice

class PaymentTransaction181(base_types._BaseFieldType):

	__slots__ = ["_CshInOrOut"]
	@property
	def CshInOrOut(self):
		return self._CshInOrOut

	@CshInOrOut.setter
	def CshInOrOut(self, value):
		self._CshInOrOut = value if type(value) != base_types.auto else self.make_default("CshInOrOut")

	@CshInOrOut.deleter
	def CshInOrOut(self):
		del self._CshInOrOut
		self._CshInOrOut = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='CshInOrOut', type=CashInOrOut8Choice, min=1, max=1, mutex_group=None, array=False),
	))