# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AmountOrRate3Choice
from . import ChargeType4Choice

class Charge26(base_types._BaseFieldType):

	__slots__ = ["_ChrgApld", "_Tp"]
	@property
	def ChrgApld(self):
		return self._ChrgApld

	@ChrgApld.setter
	def ChrgApld(self, value):
		self._ChrgApld = value if value is not None else base_types.UninitialisedField(self, 'ChrgApld', AmountOrRate3Choice, False)

	@ChrgApld.deleter
	def ChrgApld(self):
		del self._ChrgApld
		self._ChrgApld = base_types.UninitialisedField(self, 'ChrgApld', AmountOrRate3Choice, False)

	@property
	def Tp(self):
		return self._Tp

	@Tp.setter
	def Tp(self, value):
		self._Tp = value if value is not None else base_types.UninitialisedField(self, 'Tp', ChargeType4Choice, False)

	@Tp.deleter
	def Tp(self):
		del self._Tp
		self._Tp = base_types.UninitialisedField(self, 'Tp', ChargeType4Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='ChrgApld', type=AmountOrRate3Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tp', type=ChargeType4Choice, min=1, max=1, mutex_group=None, array=False),
	))